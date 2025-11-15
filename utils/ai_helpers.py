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

    def _get_prompt_template(self, goal_type: str, goal: str, timeframe: int) -> str:
        """Get the appropriate prompt template based on goal type"""

        # Common JSON format for all types
        json_format = """{{
    "overview": "Brief overview and what will be achieved",
    "milestones": ["Milestone 1", "Milestone 2", "Milestone 3"],
    "curriculum": [
        {{
            "day": 1,
            "topic": "Topic/Task name",
            "subtopics": ["Subtopic/Action 1", "Subtopic/Action 2", "Subtopic/Action 3"],
            "estimated_hours": 2.5,
            "priority": "high|medium|low",
            "resources": [
                {{"type": "course|article|video|tool", "name": "Resource name", "url": "https://example.com"}}
            ]
        }}
    ]
}}"""

        if goal_type == 'learning':
            return f"""You are an expert learning path designer. Create a day-by-day learning curriculum for: {goal} in {timeframe} days.

Include daily topics, subtopics, estimated hours, and recommended resources (courses, articles, videos).
Format as structured learning path with clear progression. Mark foundational topics as "high" priority.

Use this JSON format:
{json_format}"""

        elif goal_type == 'career':
            return f"""You are a career transition coach. Create an action plan to achieve: {goal} in {timeframe} days.

Break down into phases with:
- Skills to acquire (with priority levels)
- Portfolio projects to build
- Networking activities
- Application strategy
- Interview preparation
- Weekly milestones with specific actions

Mark critical career-building actions as "high" priority. Use this JSON format:
{json_format}"""

        elif goal_type == 'freelance':
            return f"""You are a freelance business consultant. Create a step-by-step plan to: {goal} in {timeframe} days.

Include:
- Profile/platform setup tasks (high priority at start)
- Market research and positioning
- Client acquisition strategy
- Service pricing and packages
- Marketing and outreach actions
- Revenue milestones

Mark revenue-generating actions as "high" priority. Use this JSON format:
{json_format}"""

        elif goal_type == 'project':
            return f"""You are a project manager. Create a project plan to: {goal} in {timeframe} days.

Break into phases:
- Planning and research
- Design/architecture decisions
- Implementation milestones
- Testing and refinement
- Launch/delivery checklist
- Specific deliverables per phase

Mark critical path items as "high" priority. Use this JSON format:
{json_format}"""

        elif goal_type == 'personal':
            return f"""You are a personal achievement coach. Create a progressive plan to: {goal} in {timeframe} days.

Include:
- Starting point assessment
- Progressive milestones
- Weekly targets
- Required resources/tools
- Habit formation strategy
- Progress checkpoints

Mark habit-building activities as "high" priority. Use this JSON format:
{json_format}"""

        else:
            # Default to learning
            return self._get_prompt_template('learning', goal, timeframe)

    def generate_learning_path(self, goal: str, timeframe: int, goal_type: str = 'learning') -> Dict:
        """
        Generate a goal plan based on goal type and timeframe

        Args:
            goal: The goal (e.g., "Learn Python", "Get hired as AI engineer")
            timeframe: Number of days to complete the goal
            goal_type: Type of goal (learning, career, freelance, project, personal)

        Returns:
            Dict containing the structured goal plan
        """
        prompt = self._get_prompt_template(goal_type, goal, timeframe)

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
