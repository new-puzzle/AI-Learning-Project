"""
Learning Path Generator
Combines AI generation with database storage and retrieval
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
from .ai_helpers import ClaudeAI
from .ai_providers import AIProviderManager
from .database import Database
from .date_scheduler import (
    parse_unavailable_dates,
    calculate_calendar_dates,
    format_date_display,
    get_date_status
)


class LearningPathGenerator:
    def __init__(self, api_key: str = None):
        """Initialize the learning path generator"""
        self.ai = ClaudeAI(api_key=api_key)  # Keep for backward compatibility
        self.ai_manager = AIProviderManager()  # New multi-model manager
        self.db = Database()

    def get_ai_client(self) -> ClaudeAI:
        """Returns the underlying AI client."""
        return self.ai

    def create_learning_path(self, goal: str, timeframe: int, goal_type: str = 'learning',
                           start_date: str = None, hours_per_day: float = 2.0,
                           unavailable_dates_input: str = None,
                           skip_weekends: bool = False,
                           skip_weekdays: List[int] = None) -> Dict:
        """
        Create a complete goal plan with AI generation and database storage

        Args:
            goal: The goal to achieve
            timeframe: Number of days for completion
            goal_type: Type of goal (learning, career, freelance, project, personal)
            start_date: Start date in 'YYYY-MM-DD' format
            hours_per_day: Hours available per day
            unavailable_dates_input: String of unavailable dates
            skip_weekends: Whether to skip weekends
            skip_weekdays: List of weekdays to skip (0=Monday, 6=Sunday)

        Returns:
            Dictionary containing the goal plan with path_id
        """
        # Generate goal plan using AI
        learning_path = self.ai.generate_learning_path(goal, timeframe, goal_type, hours_per_day)

        # Parse unavailable dates
        unavailable_dates = []
        if unavailable_dates_input:
            unavailable_dates = parse_unavailable_dates(unavailable_dates_input)

        # Calculate calendar dates for curriculum
        curriculum = learning_path.get('curriculum', [])

        if start_date:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()

            # Calculate calendar dates for all topics
            curriculum_with_dates = calculate_calendar_dates(
                start_date_obj,
                curriculum,
                hours_per_day,
                unavailable_dates,
                weekly_pattern=None,
                skip_weekends=skip_weekends,
                skip_weekdays=skip_weekdays
            )

            learning_path['curriculum'] = curriculum_with_dates

        # Convert unavailable_dates list to JSON for storage
        unavailable_dates_json = None
        if unavailable_dates:
            unavailable_dates_json = json.dumps([d.strftime('%Y-%m-%d') for d in unavailable_dates])

        # Save to database
        path_id = self.db.save_learning_path(
            goal,
            timeframe,
            goal_type,
            start_date=start_date,
            hours_per_day=hours_per_day,
            unavailable_dates=unavailable_dates_json
        )

        # Save action items/milestones with due dates
        self.db.save_topics(path_id, learning_path.get('curriculum', []))

        # Add path_id and goal_type to the response
        learning_path['path_id'] = path_id
        learning_path['goal_type'] = goal_type

        return learning_path

    def save_plan_from_template(self, plan: Dict, goal_name: str, timeframe: int, goal_type: str = 'learning',
                                start_date: str = None, hours_per_day: float = 2.0,
                                unavailable_dates_input: str = None, skip_weekends: bool = False,
                                skip_weekdays: List[int] = None) -> int:
        """
        Save a plan generated from a template to the database
        
        Args:
            plan: The generated plan dict with curriculum, overview, milestones
            goal_name: The goal name/title
            timeframe: Number of days
            goal_type: Type of goal
            start_date: Start date in 'YYYY-MM-DD' format
            hours_per_day: Hours per day
            unavailable_dates_input: String with unavailable dates (e.g., "Nov 20-22, Dec 1")
            skip_weekends: Whether to skip weekends
            skip_weekdays: List of weekday numbers to skip (0=Monday, 6=Sunday)
            
        Returns:
            path_id: The ID of the saved learning path
        """
        # Parse unavailable dates if provided
        unavailable_dates = []
        unavailable_dates_json = None
        if unavailable_dates_input and unavailable_dates_input.strip():
            from utils.date_scheduler import parse_unavailable_dates
            unavailable_dates = parse_unavailable_dates(unavailable_dates_input)
            if unavailable_dates:
                unavailable_dates_json = json.dumps([d.strftime('%Y-%m-%d') for d in unavailable_dates])
        
        # Save learning path to database
        path_id = self.db.save_learning_path(
            goal=goal_name,
            timeframe=timeframe,
            goal_type=goal_type,
            start_date=start_date,
            hours_per_day=hours_per_day,
            unavailable_dates=unavailable_dates_json,
            weekly_pattern=None
        )
        
        # Calculate calendar dates if start_date provided
        curriculum = plan.get('curriculum', [])
        if start_date:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
            curriculum_with_dates = calculate_calendar_dates(
                start_date_obj,
                curriculum,
                hours_per_day,
                unavailable_dates=unavailable_dates,
                weekly_pattern=None,
                skip_weekends=skip_weekends,
                skip_weekdays=skip_weekdays
            )
            curriculum = curriculum_with_dates
        
        # Save topics/curriculum
        self.db.save_topics(path_id, curriculum)
        
        return path_id

    def get_learning_path(self, path_id: int) -> Optional[Dict]:
        """
        Retrieve a learning path from the database

        Args:
            path_id: The ID of the learning path

        Returns:
            Complete learning path with topics and progress
        """
        paths = self.db.get_learning_paths(active_only=False)
        path = next((p for p in paths if p['id'] == path_id), None)

        if not path:
            return None

        # Get topics
        topics = self.db.get_topics(path_id)

        # Get progress stats
        stats = self.db.get_progress_stats(path_id)

        return {
            'path_info': path,
            'curriculum': topics,
            'stats': stats
        }

    def get_all_paths(self, active_only: bool = True) -> List[Dict]:
        """Get all learning paths"""
        return self.db.get_learning_paths(active_only)

    def update_progress(self, topic_id: int, is_completed: bool, time_spent: int = 0):
        """
        Update progress for a topic

        Args:
            topic_id: The topic ID
            is_completed: Whether the topic is completed
            time_spent: Time spent in minutes
        """
        self.db.update_topic_completion(topic_id, is_completed, time_spent)

    def get_progress_stats(self, path_id: int) -> Dict:
        """Get progress statistics for a learning path"""
        return self.db.get_progress_stats(path_id)

    def get_learning_streak(self, path_id: int) -> int:
        """
        Calculate learning streak (consecutive days with completed topics)

        Args:
            path_id: The learning path ID

        Returns:
            Number of consecutive days with activity
        """
        # This is a simplified version
        # In a production app, you'd track daily activity more precisely
        topics = self.db.get_topics(path_id)
        completed_days = set()

        for topic in topics:
            if topic['is_completed'] and topic['completed_at']:
                # Extract just the date part
                date = topic['completed_at'].split(' ')[0]
                completed_days.add(date)

        # Simple streak calculation
        return len(completed_days)

    def delete_path(self, path_id: int):
        """Delete (soft delete) a learning path"""
        self.db.delete_learning_path(path_id)

    def update_path_status(self, path_id: int, status: str):
        """
        Update the status of a learning path

        Args:
            path_id: The learning path ID
            status: New status ('active', 'on_hold', 'archived', 'deleted')
        """
        self.db.update_path_status(path_id, status)

    def get_paths_by_status(self, status: str = None) -> List[Dict]:
        """
        Get learning paths filtered by status

        Args:
            status: Filter by status (None for all paths)

        Returns:
            List of learning paths
        """
        return self.db.get_paths_by_status(status)

    def get_assistance(self, question: str, context: str = "", model_selection: str = "Claude Sonnet 4.5") -> str:
        """
        Get AI assistance for learning questions

        Args:
            question: The user's question
            context: Learning context
            model_selection: Full model selection (e.g., "Claude / Claude Sonnet 4.5" or "Claude Sonnet 4.5" for backward compat)

        Returns:
            AI response
        """
        # Parse model selection
        if " / " in model_selection:
            provider_name, model_name = model_selection.split(" / ", 1)
        else:
            # Backward compatibility - assume Claude
            provider_name = "Claude"
            model_name = model_selection

        # Build the full prompt
        if context:
            full_prompt = f"{context}\n\nQuestion: {question}"
        else:
            full_prompt = question

        system_prompt = "You are a helpful learning assistant. Provide clear, concise explanations that help users understand concepts."

        try:
            response = self.ai_manager.generate_text(
                provider_name=provider_name,
                model_name=model_name,
                prompt=full_prompt,
                system_prompt=system_prompt
            )
            return response
        except Exception as e:
            # Fallback to Claude if configured
            if provider_name != "Claude":
                try:
                    self.ai.set_model(model_name if model_name.startswith("Claude") else "Claude Sonnet 4.5")
                    return self.ai.get_learning_assistance(question, context)
                except:
                    pass
            raise e

    def get_available_models(self) -> Dict:
        """Get all available AI models"""
        return self.ai_manager.get_available_models()

    def analyze_uploaded_image(self, image_data: bytes, question: str, model_selection: str = "Claude Sonnet 4.5") -> str:
        """
        Analyze an uploaded image

        Args:
            image_data: Image bytes
            question: Question about the image
            model_selection: Model to use (format: "Provider / Model")

        Returns:
            AI analysis of the image
        """
        # Parse model selection
        if " / " in model_selection:
            provider_name, model_name = model_selection.split(" / ", 1)
        else:
            provider_name = "Claude"
            model_name = model_selection

        return self.ai_manager.analyze_image(
            provider_name=provider_name,
            model_name=model_name,
            image_data=image_data,
            prompt=question
        )

    def generate_practice(self, topic: str, difficulty: str = "medium", count: int = 3) -> List[Dict]:
        """Generate practice problems for a topic"""
        return self.ai.generate_practice_problems(topic, difficulty, count)

    def find_resources(self, topic: str, resource_types: List[str] = None) -> List[Dict]:
        """Find learning resources for a topic"""
        return self.ai.find_resources(topic, resource_types)
