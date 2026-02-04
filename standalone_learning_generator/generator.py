"""
Learning Path Generator
Main class that combines AI prompts with scheduling to generate learning paths
"""

import os
import json
from typing import Dict, List, Optional
from datetime import datetime, date

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("Warning: anthropic package not installed. Install with: pip install anthropic")

from ai_prompts import LearningPathPrompts
from scheduler import parse_unavailable_dates, calculate_calendar_dates


class LearningPathGenerator:
    """Generate detailed learning paths using AI"""
    
    def __init__(self, api_key: str = None, model_name: str = "claude-sonnet-4-5-20250929"):
        """
        Initialize the learning path generator
        
        Args:
            api_key: Anthropic API key (or set ANTHROPIC_API_KEY env var)
            model_name: Claude model to use
        """
        if not ANTHROPIC_AVAILABLE:
            raise ImportError("anthropic package is required. Install with: pip install anthropic")
        
        # Get API key from parameter, environment, or streamlit secrets
        if api_key:
            self.api_key = api_key
        else:
            try:
                import streamlit as st
                self.api_key = st.secrets.get("ANTHROPIC_API_KEY")
            except:
                self.api_key = os.getenv("ANTHROPIC_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "Anthropic API key not found. "
                "Set ANTHROPIC_API_KEY environment variable or pass api_key parameter."
            )
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = model_name
        self.prompts = LearningPathPrompts()
    
    def generate_learning_path(
        self,
        topic: str,
        timeframe: int,
        hours_per_day: float = 2.0,
        start_date: Optional[str] = None,
        skip_weekends: bool = False,
        skip_weekdays: Optional[List[int]] = None,
        unavailable_dates_input: Optional[str] = None,
        proficiency: Optional[str] = None,
        focus_areas: Optional[List[str]] = None,
        additional_requests: Optional[str] = None
    ) -> Dict:
        """
        Generate a complete learning path for a topic
        
        Args:
            topic: Topic to learn (e.g., "prompt engineering", "n8n")
            timeframe: Number of days for the learning path
            hours_per_day: Hours available per day
            start_date: Start date in 'YYYY-MM-DD' format (optional)
            skip_weekends: Whether to skip weekends
            skip_weekdays: List of weekdays to skip (0=Monday, 6=Sunday)
            unavailable_dates_input: String of unavailable dates (e.g., "Nov 20-22, Dec 1")
            proficiency: Proficiency level (Beginner/Intermediate/Advanced)
            focus_areas: List of specific areas to focus on
            additional_requests: Additional requirements or preferences
            
        Returns:
            Dictionary containing the complete learning path with curriculum
        """
        # Generate prompts
        system_prompt, user_prompt = self.prompts.get_learning_path_prompt(
            topic=topic,
            timeframe=timeframe,
            hours_per_day=hours_per_day,
            proficiency=proficiency,
            focus_areas=focus_areas,
            additional_requests=additional_requests
        )
        
        # Call AI
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                temperature=0.6,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_prompt}
                ]
            )
            
            # Extract response text
            response_text = message.content[0].text
            
            # Parse JSON from response
            if "```json" in response_text:
                json_start = response_text.find("```json") + 7
                json_end = response_text.rfind("```")
                json_text = response_text[json_start:json_end].strip()
            elif response_text.startswith("{") and response_text.endswith("}"):
                json_text = response_text
            else:
                # Fallback: extract JSON between first { and last }
                json_start = response_text.find("{")
                json_end = response_text.rfind("}") + 1
                json_text = response_text[json_start:json_end]
            
            learning_path = json.loads(json_text)
            
            # Add calendar dates if start_date provided
            if start_date and 'curriculum' in learning_path:
                start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
                
                # Parse unavailable dates
                unavailable_dates = []
                if unavailable_dates_input:
                    unavailable_dates = parse_unavailable_dates(unavailable_dates_input)
                
                # Calculate calendar dates
                curriculum_with_dates = calculate_calendar_dates(
                    start_date_obj,
                    learning_path['curriculum'],
                    hours_per_day,
                    unavailable_dates,
                    skip_weekends,
                    skip_weekdays
                )
                
                learning_path['curriculum'] = curriculum_with_dates
            
            # Add metadata
            learning_path['metadata'] = {
                'topic': topic,
                'timeframe': timeframe,
                'hours_per_day': hours_per_day,
                'start_date': start_date,
                'total_hours': timeframe * hours_per_day,
                'proficiency': proficiency,
                'focus_areas': focus_areas
            }
            
            return learning_path
            
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse AI response as JSON: {str(e)}\nResponse: {response_text[:500]}")
        except Exception as e:
            raise Exception(f"Error generating learning path: {str(e)}")

