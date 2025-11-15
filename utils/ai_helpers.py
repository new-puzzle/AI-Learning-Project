"""
AI Helper functions for LearnPath AI
Handles Claude API integration for generating learning paths and providing assistance
"""

import os
from typing import Dict, List
import anthropic


class ClaudeAI:
    # Model mappings
    MODELS = {
        "Claude Sonnet 4.5": "claude-sonnet-4-5-20250929",
        "Claude Sonnet 3.5": "claude-3-5-sonnet-20241022",
        "Claude Haiku": "claude-3-5-haiku-20241022"
    }

    def __init__(self, api_key: str = None, model_name: str = "Claude Sonnet 4.5"):
        """Initialize Claude AI client"""
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("Anthropic API key not found. Please set ANTHROPIC_API_KEY environment variable.")

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.set_model(model_name)

    def set_model(self, model_name: str):
        """Set the model to use for API calls"""
        self.model = self.MODELS.get(model_name, self.MODELS["Claude Sonnet 4.5"])

    def generate_learning_path(self, goal: str, timeframe: int) -> Dict:
        """
        Generate a comprehensive learning path based on the goal and timeframe

        Args:
            goal: The learning goal (e.g., "Learn Python")
            timeframe: Number of days to complete the goal

        Returns:
            Dict containing the structured learning path
        """
        prompt = f"""You are an expert learning path designer. Create a detailed, day-by-day learning curriculum for the following goal:

Goal: {goal}
Timeframe: {timeframe} days

Please create a comprehensive learning path that includes:

1. Break down the learning into daily topics (one topic per day)
2. For each day, provide:
   - Main topic name
   - 3-5 subtopics to cover
   - Estimated hours needed
   - 2-3 recommended resources (courses, articles, videos, books)

Format your response as a structured JSON with the following format:
{{
    "overview": "Brief overview of the learning path and what the learner will achieve",
    "milestones": ["Milestone 1", "Milestone 2", "Milestone 3"],
    "curriculum": [
        {{
            "day": 1,
            "topic": "Topic name",
            "subtopics": ["Subtopic 1", "Subtopic 2", "Subtopic 3"],
            "estimated_hours": 2.5,
            "resources": [
                {{"type": "course", "name": "Resource name", "url": "https://example.com"}},
                {{"type": "article", "name": "Resource name", "url": "https://example.com"}}
            ]
        }}
    ]
}}

Make the learning path progressive, building knowledge day by day. Keep it practical and achievable within the given timeframe."""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                temperature=0.7,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            # Extract the text content from the response
            response_text = message.content[0].text

            # Parse JSON from the response
            import json

            # Try to extract JSON from the response
            # Sometimes Claude wraps JSON in markdown code blocks
            if "```json" in response_text:
                json_start = response_text.find("```json") + 7
                json_end = response_text.find("```", json_start)
                json_text = response_text[json_start:json_end].strip()
            elif "```" in response_text:
                json_start = response_text.find("```") + 3
                json_end = response_text.find("```", json_start)
                json_text = response_text[json_start:json_end].strip()
            else:
                json_text = response_text

            learning_path = json.loads(json_text)
            return learning_path

        except Exception as e:
            raise Exception(f"Error generating learning path: {str(e)}")

    def get_learning_assistance(self, question: str, context: str = "") -> str:
        """
        Get AI assistance for learning questions

        Args:
            question: The user's question
            context: Optional context about what they're currently learning

        Returns:
            AI-generated response
        """
        prompt = f"""You are a helpful learning assistant.

{f"Context: The user is currently learning about: {context}" if context else ""}

User Question: {question}

Provide a clear, concise explanation that helps the user understand the concept. Use examples where helpful."""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                temperature=0.7,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            return message.content[0].text

        except Exception as e:
            raise Exception(f"Error getting assistance: {str(e)}")

    def generate_practice_problems(self, topic: str, difficulty: str = "medium", count: int = 3) -> List[Dict]:
        """
        Generate practice problems for a given topic

        Args:
            topic: The topic to generate problems for
            difficulty: Difficulty level (easy, medium, hard)
            count: Number of problems to generate

        Returns:
            List of practice problems
        """
        prompt = f"""Generate {count} {difficulty} difficulty practice problems for the topic: {topic}

Format your response as JSON:
[
    {{
        "problem": "Description of the problem",
        "hints": ["Hint 1", "Hint 2"],
        "solution": "Brief solution explanation"
    }}
]

Make the problems practical and help reinforce understanding of the topic."""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                temperature=0.8,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = message.content[0].text

            # Extract JSON
            import json
            if "```json" in response_text:
                json_start = response_text.find("```json") + 7
                json_end = response_text.find("```", json_start)
                json_text = response_text[json_start:json_end].strip()
            elif "```" in response_text:
                json_start = response_text.find("```") + 3
                json_end = response_text.find("```", json_start)
                json_text = response_text[json_start:json_end].strip()
            else:
                json_text = response_text

            problems = json.loads(json_text)
            return problems

        except Exception as e:
            raise Exception(f"Error generating practice problems: {str(e)}")

    def find_resources(self, topic: str, resource_types: List[str] = None) -> List[Dict]:
        """
        Find recommended learning resources for a topic

        Args:
            topic: The topic to find resources for
            resource_types: Types of resources (courses, articles, videos, books)

        Returns:
            List of recommended resources
        """
        if resource_types is None:
            resource_types = ["courses", "articles", "videos"]

        types_str = ", ".join(resource_types)

        prompt = f"""Find the best learning resources for the topic: {topic}

Include these types of resources: {types_str}

Format as JSON:
[
    {{
        "type": "course|article|video|book",
        "name": "Resource name",
        "description": "Brief description",
        "url": "URL if available",
        "difficulty": "beginner|intermediate|advanced",
        "free": true|false
    }}
]

Provide 5-8 high-quality, reputable resources."""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                temperature=0.5,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = message.content[0].text

            # Extract JSON
            import json
            if "```json" in response_text:
                json_start = response_text.find("```json") + 7
                json_end = response_text.find("```", json_start)
                json_text = response_text[json_start:json_end].strip()
            elif "```" in response_text:
                json_start = response_text.find("```") + 3
                json_end = response_text.find("```", json_start)
                json_text = response_text[json_start:json_end].strip()
            else:
                json_text = response_text

            resources = json.loads(json_text)
            return resources

        except Exception as e:
            raise Exception(f"Error finding resources: {str(e)}")
