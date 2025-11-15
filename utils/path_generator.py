"""
Learning Path Generator
Combines AI generation with database storage and retrieval
"""

from typing import Dict, List, Optional
from .ai_helpers import ClaudeAI
from .database import Database


class LearningPathGenerator:
    def __init__(self, api_key: str = None):
        """Initialize the learning path generator"""
        self.ai = ClaudeAI(api_key=api_key)
        self.db = Database()

    def create_learning_path(self, goal: str, timeframe: int) -> Dict:
        """
        Create a complete learning path with AI generation and database storage

        Args:
            goal: The learning goal
            timeframe: Number of days for completion

        Returns:
            Dictionary containing the learning path with path_id
        """
        # Generate learning path using AI
        learning_path = self.ai.generate_learning_path(goal, timeframe)

        # Save to database
        path_id = self.db.save_learning_path(goal, timeframe)

        # Save curriculum topics
        curriculum = learning_path.get('curriculum', [])
        self.db.save_topics(path_id, curriculum)

        # Add path_id to the response
        learning_path['path_id'] = path_id

        return learning_path

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

    def get_assistance(self, question: str, context: str = "") -> str:
        """Get AI assistance for learning questions"""
        return self.ai.get_learning_assistance(question, context)

    def generate_practice(self, topic: str, difficulty: str = "medium", count: int = 3) -> List[Dict]:
        """Generate practice problems for a topic"""
        return self.ai.generate_practice_problems(topic, difficulty, count)

    def find_resources(self, topic: str, resource_types: List[str] = None) -> List[Dict]:
        """Find learning resources for a topic"""
        return self.ai.find_resources(topic, resource_types)
