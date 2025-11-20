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
        # Try to get API key from: 1) parameter, 2) streamlit secrets, 3) environment variable
        if api_key:
            self.api_key = api_key
        else:
            try:
                import streamlit as st
                self.api_key = st.secrets.get("ANTHROPIC_API_KEY")
            except:
                self.api_key = os.getenv("ANTHROPIC_API_KEY")

        if not self.api_key:
            raise ValueError("Anthropic API key not found. Please set ANTHROPIC_API_KEY in .streamlit/secrets.toml or as environment variable.")

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.set_model(model_name)

    def set_model(self, model_name: str):
        """Set the model to use for API calls"""
        self.model = self.MODELS.get(model_name, self.MODELS["Claude Sonnet 4.5"])

    def _get_prompt_template(self, goal_type: str, goal: str, timeframe: int, hours_per_day: float = 2.0, user_context: Dict = None) -> (str, str):
        """
        Get the appropriate system and user prompts based on goal type.

        Returns a tuple of (system_prompt, user_prompt).
        """
        # Calculate time budget
        total_hours = timeframe * hours_per_day
        
        # Content density based on hours
        if hours_per_day <= 1.5:
            content_guide = "Light content, one main topic per day"
            resource_count = "1-2 high-quality resources"
            objective_count = "1-2 specific objectives"
        elif hours_per_day <= 3.0:
            content_guide = "Moderate content with theory + practice"
            resource_count = "2-3 diverse resources"
            objective_count = "2-3 actionable objectives"
        else:
            content_guide = "Deep, comprehensive content with projects"
            resource_count = "3-4 varied resources"
            objective_count = "3-4 challenging objectives"
        
        # Base system prompt
        system_prompt = f"""You are an expert curriculum architect. Create a {timeframe}-day structured plan.

TIME BUDGET (CRITICAL):
- Available: {hours_per_day} hours per day
- Total: {total_hours} hours
- Daily content MUST fit in {hours_per_day} hours
- estimated_hours should be ≈ {hours_per_day} (±0.5)

REQUIREMENTS:

1. EXACT DAY COUNT:
   - Generate EXACTLY {timeframe} days
   - Count: Day 1, 2, 3... {timeframe}
   - Verify before submitting

2. TIME-APPROPRIATE CONTENT:
   - {content_guide}
   - {resource_count} per day
   - {objective_count} per day
   - Respect the {hours_per_day} hour daily limit

3. REAL RESOURCES ONLY:
   - ALL URLs must be real and working
   - NO placeholders: example.com, youtube.com/example, REAL_VIDEO_ID, real-article-slug
   - Use real: YouTube videos (actual video IDs), Medium/Dev.to articles (actual slugs), official docs, GitHub repos
   - Resource length must fit time budget (10-min videos for 1hr plans, 30-min for 4hr plans)

4. ACTIONABLE OBJECTIVES:
   - Use action verbs: "Build", "Create", "Implement", "Debug", "Analyze"
   - NOT vague: "Learn about", "Understand", "Get familiar with"
   - Each objective completable within daily time budget
   - Must produce tangible outcome

5. CLEAR PROGRESSION:
   - Days 1-30% (Days 1-{int(timeframe*0.3)}): Foundation
     * Core concepts, terminology, setup
     * Simple confidence-building exercises
     * Overview of ecosystem
   - Days 31-65% (Days {int(timeframe*0.3)+1}-{int(timeframe*0.65)}): Application
     * Practical projects combining concepts
     * Real-world scenarios
     * Build small complete applications
   - Days 66-85% (Days {int(timeframe*0.65)+1}-{int(timeframe*0.85)}): Integration
     * Complex problems
     * Optimization and refactoring
     * Advanced patterns
   - Days 86-100% (Days {int(timeframe*0.85)+1}-{timeframe}): Mastery
     * Capstone project
     * Production-ready work
     * Portfolio piece

6. REALISTIC SCOPE:
   - Be honest about what's achievable in {total_hours} hours
   - Don't promise mastery if time is insufficient
   - Quality over quantity

Return ONLY valid JSON. No markdown code blocks, no explanations."""

        # --- JSON Schemas ---
        learning_schema = """{{
    "overview": "2-3 sentences acknowledging the """ + str(timeframe) + """ days and """ + str(hours_per_day) + """ hours/day, explaining what will be achieved",
    "milestones": [
        "Day X: Foundation complete - Specific achievement",
        "Day Y: First project built - Specific deliverable",
        "Day Z: Advanced topics covered - Specific skill gained",
        "Day """ + str(timeframe) + """: Capstone done - Portfolio-ready outcome"
    ],
    "curriculum": [
        {{
            "day": 1,
            "topic": "Specific, clear topic appropriate for """ + str(hours_per_day) + """ hours",
            "learning_objectives": [
                "Build/Create specific tangible thing",
                "Implement specific feature or solve specific problem"
            ],
            "estimated_hours": """ + str(hours_per_day) + """,
            "priority": "high",
            "resources": [
                {{"type": "video", "name": "Real YouTube video title", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}},
                {{"type": "article", "name": "Real article from Medium/Dev.to/docs", "url": "https://realpython.com/python-basics/"}}
            ]
        }}
    ]
}}"""

        career_schema = """{{
    "overview": "Career plan for """ + str(timeframe) + """ days at """ + str(hours_per_day) + """ hours/day",
    "phases": [
        "Phase 1: Skill Building (Days 1-X)",
        "Phase 2: Applications & Networking (Days X-Y)", 
        "Phase 3: Interviewing (Days Y-""" + str(timeframe) + """)"
    ],
    "schedule": [
        {{
            "day": 1,
            "focus": "Specific focus achievable in """ + str(hours_per_day) + """ hours",
            "action_items": [
                "Specific action with deliverable",
                "Measurable task with outcome"
            ],
            "deliverable": "Concrete deliverable for the day",
            "priority": "high"
        }}
    ]
}}"""

        freelance_schema = """{{
    "overview": "Freelance plan for """ + str(timeframe) + """ days, """ + str(hours_per_day) + """ hours/day",
    "revenue_milestones": [
        "Realistic milestone 1 given time constraints",
        "Realistic milestone 2 for """ + str(total_hours) + """ total hours"
    ],
    "weekly_focus": [
        {{
            "week": 1,
            "theme": "Weekly theme achievable in """ + str(hours_per_day * 7) + """ hours",
            "tasks": [
                "Specific task with deliverable",
                "Measurable action item"
            ],
            "goal": "Concrete weekly outcome"
        }}
    ]
}}"""

        project_schema = """{{
    "overview": "Project plan: """ + str(timeframe) + """ days, """ + str(hours_per_day) + """ hours/day",
    "deliverables": [
        "Deliverable 1 realistic for time budget",
        "Deliverable 2 achievable in """ + str(total_hours) + """ hours"
    ],
    "timeline": [
        {{
            "day": 1,
            "task": "Main task for """ + str(hours_per_day) + """ hours",
            "sub_tasks": [
                "Specific sub-task 1",
                "Specific sub-task 2"
            ],
            "estimated_hours": """ + str(hours_per_day) + """,
            "priority": "high"
        }}
    ]
}}"""

        personal_schema = """{{
    "overview": "Personal plan: """ + str(timeframe) + """ days, """ + str(hours_per_day) + """ hours/day",
    "key_habits": [
        "Habit 1 sustainable at """ + str(hours_per_day) + """ hrs/day",
        "Habit 2 achievable in available time"
    ],
    "daily_plan": [
        {{
            "day": 1,
            "focus_habit": "Main habit for the day",
            "actions": [
                "Specific action completable in time",
                "Measurable activity"
            ],
            "mindset_tip": "Motivational or practical tip",
            "priority": "high"
        }}
    ]
}}"""

        # --- User Prompts ---
        if goal_type == 'learning':
            system_prompt += f"\n\nJSON Schema:\n{learning_schema}"
            user_prompt = f"""Create a {timeframe}-day learning curriculum for: "{goal}"

TIME CONSTRAINTS:
- {hours_per_day} hours available per day
- {total_hours} hours total budget
- Each day must fit in {hours_per_day} hours

REQUIREMENTS:
- EXACTLY {timeframe} days (count them!)
- estimated_hours ≈ {hours_per_day} for each day
- {resource_count} per day (all real URLs)
- {objective_count} per day (all actionable)
- Clear progression: foundation → application → integration → mastery
- Realistic scope for {total_hours} total hours

QUALITY CHECKLIST:
✓ Exactly {timeframe} days?
✓ Each day ≈ {hours_per_day} hours?
✓ All resource URLs real and working?
✓ Objectives use action verbs with deliverables?
✓ Progression from basic to advanced?
✓ Total scope realistic for {total_hours} hours?

Generate the complete curriculum now."""
        elif goal_type == 'career':
            system_prompt += f"\n\nJSON Schema:\n{career_schema}"
            user_prompt = f"""Create a {timeframe}-day career transition plan for: "{goal}"

TIME: {hours_per_day} hrs/day ({total_hours} hrs total)

REQUIREMENTS:
- EXACTLY {timeframe} days with specific action items
- Mix: skill-building, resume/portfolio, networking, applications
- Each day's actions fit in {hours_per_day} hours
- Concrete deliverables (updated resume, portfolio piece, applications sent)
- Real resources and platforms (LinkedIn, job boards, courses)

PHASES:
- Early days: Skills and portfolio
- Middle days: Applications and networking
- Final days: Interview prep and follow-ups

CHECKLIST:
✓ {timeframe} days with actionable items?
✓ Daily work fits {hours_per_day} hours?
✓ Deliverables are concrete?
✓ Resources are real platforms/links?"""
        elif goal_type == 'freelance':
            system_prompt += f"\n\nJSON Schema:\n{freelance_schema}"
            user_prompt = f"""Create a {timeframe}-day freelance business launch plan for: "{goal}"

TIME: {hours_per_day} hrs/day ({total_hours} hrs total)

REQUIREMENTS:
- Organize by weeks (Week 1, 2, etc.)
- {hours_per_day * 7} hours per week available
- Cover: service definition, pricing, portfolio, marketing, client outreach
- Realistic revenue milestones for available time
- Real platforms (Upwork, Fiverr, LinkedIn, cold email)

PROGRESSION:
- Weeks 1-2: Foundation (services, pricing, portfolio)
- Weeks 3-4: Marketing and outreach
- Remaining: Client work and scaling

CHECKLIST:
✓ Weekly tasks fit {hours_per_day * 7} hours/week?
✓ Revenue goals realistic for time investment?
✓ Platforms and tools are real?"""
        elif goal_type == 'project':
            system_prompt += f"\n\nJSON Schema:\n{project_schema}"
            user_prompt = f"""Create a {timeframe}-day project execution plan for: "{goal}"

TIME: {hours_per_day} hrs/day ({total_hours} hrs total)

REQUIREMENTS:
- EXACTLY {timeframe} days
- Each day ≈ {hours_per_day} hours of work
- Include 20% buffer time for debugging
- Clear phases: Planning → Build → Test → Deploy
- Specific deliverables each day

CHECKLIST:
✓ {timeframe} days counted?
✓ Each day fits {hours_per_day} hours?
✓ Buffer time included for issues?
✓ Deliverables are specific?"""
        elif goal_type == 'personal':
            system_prompt += f"\n\nJSON Schema:\n{personal_schema}"
            user_prompt = f"""Create a {timeframe}-day personal development plan for: "{goal}"

TIME: {hours_per_day} hrs/day

REQUIREMENTS:
- EXACTLY {timeframe} days
- Daily actions fit in {hours_per_day} hours
- Sustainable pace (avoid burnout)
- Reflection checkpoints every 7-10 days
- Motivational support throughout

CHECKLIST:
✓ {timeframe} days?
✓ Actions completable in {hours_per_day} hours?
✓ Pace is sustainable?"""
        else:
            # Default to learning
            return self._get_prompt_template('learning', goal, timeframe, hours_per_day, user_context)

        # Add user context if available
        if user_context:
            context_str = "\n\nUser Context (tailor accordingly):\n"
            for key, value in user_context.items():
                context_str += f"- {key.replace('_', ' ').title()}: {value}\n"
            user_prompt += context_str

        return system_prompt, user_prompt

    def generate_learning_path(self, goal: str, timeframe: int, goal_type: str = 'learning', hours_per_day: float = 2.0, user_context: Dict = None) -> Dict:
        """
        Generate a goal plan based on goal type and timeframe

        Args:
            goal: The goal (e.g., "Learn Python", "Get hired as AI engineer")
            timeframe: Number of days to complete the goal
            goal_type: Type of goal (learning, career, freelance, project, personal)
            hours_per_day: Hours available per day (default: 2.0)
            user_context: Optional dictionary with user-specific context

        Returns:
            Dict containing the structured goal plan
        """
        system_prompt, user_prompt = self._get_prompt_template(goal_type, goal, timeframe, hours_per_day, user_context)

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=4096,  # Increased max_tokens for longer plans
                temperature=0.6, # Slightly lowered temperature for more deterministic output
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_prompt}
                ]
            )

            # Extract the text content from the response
            response_text = message.content[0].text

            # Parse JSON from the response
            import json

            # Try to extract JSON from the response
            # Claude sometimes wraps JSON in markdown code blocks
            if "```json" in response_text:
                json_start = response_text.find("```json") + 7
                json_end = response_text.rfind("```")
                json_text = response_text[json_start:json_end].strip()
            elif response_text.startswith("{") and response_text.endswith("}"):
                json_text = response_text
            else:
                # Fallback for cases where JSON is not perfectly formatted
                json_start = response_text.find("{")
                json_end = response_text.rfind("}") + 1
                json_text = response_text[json_start:json_end]

            learning_path = json.loads(json_text)
            return learning_path

        except Exception as e:
            # Log the error and the response text for debugging
            print(f"Error generating learning path: {str(e)}")
            print(f"LLM Response Text: {response_text if 'response_text' in locals() else 'No response text available'}")
            raise Exception(f"Error generating learning path. Please check the logs for details.")

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

    def get_ai_suggestions_for_focus_areas(self, template: Dict, proficiency: str) -> List[str]:
        """Get AI-suggested focus areas based on the template and user's proficiency."""
        # Build template context from available fields
        subdivisions_text = ""
        if template.get('subdivisions') and len(template['subdivisions']) > 0:
            subdivisions_text = f"- **Subdivisions:** {', '.join(template['subdivisions'])}\n"
        
        subdivision_category_text = ""
        if template.get('subdivision_category'):
            subdivision_category_text = f"- **Category:** {template['subdivision_category']}\n"
        
        tags_text = ""
        if template.get('tags') and len(template['tags']) > 0:
            tags_text = f"- **Tags:** {', '.join(template['tags'])}\n"
        
        prompt = f"""You are an expert learning designer. A user has selected a goal template and specified their proficiency level. Your task is to suggest a list of 5-7 key focus areas (sub-topics) that are most relevant to their proficiency level.

**Template Information:**
- **Goal Name:** {template['name']}
- **Goal Description:** {template.get('description', '')}
{subdivision_category_text}{subdivisions_text}{tags_text}- **Difficulty:** {template.get('difficulty', 'Intermediate')}
- **Timeframe:** {template.get('timeframe', 30)} days

**User's Proficiency Level:** {proficiency}

**Your Task:**
Analyze the template information and the user's proficiency to recommend a list of specific, actionable focus areas that will help them achieve this goal. 
- If the user is a **Beginner**, suggest foundational topics, basics, and entry-level concepts.
- If the user is **Intermediate**, suggest more advanced, practical topics, and real-world applications.
- If the user is an **Expert**, suggest highly advanced, specialized, or strategic topics, and mastery-level concepts.

Make the suggestions specific and actionable. Consider the goal type, description, and category when generating suggestions.

**Output Format:**
Return a simple JSON array of strings (5-7 focus areas).

**Example:**
```json
[
  "Core Topic A for their level",
  "Practical Application B for their level",
  "Advanced Concept C for their level"
]
```"""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                temperature=0.6,
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

            suggestions = json.loads(json_text)
            return suggestions

        except Exception as e:
            # Fallback: generate basic suggestions from description or return empty list
            if template.get('subdivisions') and len(template['subdivisions']) > 0:
                return template['subdivisions']
            # If no subdivisions, create basic suggestions from description
            description = template.get('description', '')
            if description:
                # Split description by commas and take first few items
                parts = [p.strip() for p in description.split(',')[:5]]
                return parts if parts else ["Focus area 1", "Focus area 2", "Focus area 3"]
            return ["Focus area 1", "Focus area 2", "Focus area 3"]

    def generate_plan_from_template(self, template: Dict, proficiency: str, timeframe: int, hours_per_day: float, focus_areas: List[str], other_requests: str) -> Dict:
        """Generate a personalized learning plan from a template and user inputs."""
        # Calculate time budget
        total_hours = timeframe * hours_per_day
        
        # Content density
        if hours_per_day <= 1.5:
            depth_guide = "Light content, one main topic per day"
            resource_count = "1-2 resources"
            objective_count = "1-2 objectives"
        elif hours_per_day <= 3.0:
            depth_guide = "Moderate content with balanced theory/practice"
            resource_count = "2-3 resources"
            objective_count = "2-3 objectives"
        else:
            depth_guide = "Deep content with extensive practice/projects"
            resource_count = "3-4 resources"
            objective_count = "3-4 objectives"
        
        # Build template context
        subdivisions_text = ""
        if template.get('subdivisions') and len(template['subdivisions']) > 0:
            subdivisions_text = f"- **Subdivisions:** {', '.join(template['subdivisions'])}\n"
        
        subdivision_category_text = ""
        if template.get('subdivision_category'):
            subdivision_category_text = f"- **Category:** {template['subdivision_category']}\n"
        
        tags_text = ""
        if template.get('tags') and len(template['tags']) > 0:
            tags_text = f"- **Tags:** {', '.join(template['tags'])}\n"
        
        # Proficiency-specific guidance
        prof_guide = {
            'Beginner': {
                'approach': 'Start with absolute basics, explain every concept thoroughly, use simple language',
                'pace': 'Slow and steady, confidence-building',
                'resources': 'Beginner-friendly videos, interactive tutorials, visual guides'
            },
            'Intermediate': {
                'approach': 'Skip basics, focus on practical application and real-world scenarios',
                'pace': 'Moderate, assume foundational knowledge',
                'resources': 'Mix of videos, articles, hands-on projects'
            },
            'Advanced': {
                'approach': 'Advanced concepts only, optimization, architecture, expert patterns',
                'pace': 'Fast-paced, challenge with complex problems',
                'resources': 'Technical documentation, research papers, open-source projects'
            }
        }.get(proficiency, {
            'approach': 'Practical focus',
            'pace': 'Moderate',
            'resources': 'Varied resources'
        })
        
        system_prompt = f"""You are an expert learning path architect. Create a personalized {timeframe}-day curriculum.

TIME BUDGET (CRITICAL):
- Available: {hours_per_day} hours per day
- Total: {total_hours} hours
- Daily content MUST fit in {hours_per_day} hours
- estimated_hours ≈ {hours_per_day} per day

REQUIREMENTS:

1. EXACT DAY COUNT:
   - Generate EXACTLY {timeframe} days
   - Count: Day 1, 2, 3... {timeframe}
   - Verify before submitting

2. TIME-APPROPRIATE CONTENT:
   - {depth_guide}
   - {resource_count} per day
   - {objective_count} per day
   - Respect {hours_per_day} hour daily limit

3. FOCUS AREA PRIORITIZATION:
   - User chose: {', '.join(focus_areas) if focus_areas else 'comprehensive coverage'}
   - Allocate 60-70% of time to focus areas
   - Introduce focus areas in first 20% of days
   - Provide extra depth and resources for focus areas
   - Still cover other topics at 30-40% depth

4. REAL RESOURCES ONLY:
   - ALL URLs must be real and working
   - NO placeholders: example.com, youtube.com/example, REAL_VIDEO_ID, real-article-slug
   - Use: Real YouTube videos (actual video IDs), Medium/Dev.to articles (actual slugs), official docs, GitHub repos
   - Resource duration must fit time (10-min videos for 1hr, 30-min for 4hr)

5. ACTIONABLE SUBTOPICS:
   - Use imperatives: "Build X", "Implement Y", "Debug Z", "Create W"
   - NOT vague: "Learn about", "Understand", "Explore"
   - Each subtopic completable in 20-40 minutes
   - Must produce tangible mini-outcome

6. CLEAR PROGRESSION:
   - Days 1-30% (Days 1-{int(timeframe*0.3)}): Foundation
     * Core concepts for {proficiency} level
     * Setup and basics
     * Simple exercises
   - Days 31-65% (Days {int(timeframe*0.3)+1}-{int(timeframe*0.65)}): Application  
     * Practical projects
     * Combine multiple concepts
     * Real-world scenarios
   - Days 66-85% (Days {int(timeframe*0.65)+1}-{int(timeframe*0.85)}): Integration
     * Complex problems
     * Optimization
     * Advanced patterns
   - Days 86-100% (Days {int(timeframe*0.85)+1}-{timeframe}): Mastery
     * Capstone project
     * Production-ready work
     * Portfolio piece

7. PROFICIENCY ADAPTATION:
   - Content difficulty matches {proficiency} level
   - Vocabulary: {"simple, explanatory" if proficiency == "Beginner" else "technical, in-depth" if proficiency == "Advanced" else "practical, applied"}
   - Examples: {"step-by-step" if proficiency == "Beginner" else "challenging" if proficiency == "Advanced" else "real-world"}

8. INCORPORATE REQUESTS:
   - User requested: "{other_requests if other_requests else 'Standard curriculum'}"
   - Weave naturally throughout (don't just append at end)
   - Integrate where relevant to topics

Return ONLY valid JSON. No markdown code blocks, no explanations."""

        user_prompt = f"""TEMPLATE: {template['name']}
Description: {template.get('description', '')}
Goal Type: {template.get('goal_type', 'learning')}
Standard Timeframe: {template.get('timeframe', 30)} days
{subdivision_category_text}{subdivisions_text}{tags_text}Difficulty: {template.get('difficulty', 'Intermediate')}

PERSONALIZATION:
- Proficiency: {proficiency}
  * Approach: {prof_guide['approach']}
  * Pace: {prof_guide['pace']}
  * Resources: {prof_guide['resources']}
- Focus Areas: {', '.join(focus_areas) if focus_areas else 'All topics comprehensively'}
- Additional Requests: {other_requests if other_requests else 'None'}

OUTPUT JSON:

{{
    "overview": "2-3 inspiring sentences acknowledging {timeframe} days, {hours_per_day} hrs/day, {proficiency} level, focus on {', '.join(focus_areas) if focus_areas else 'comprehensive coverage'}, and final outcome",
    "milestones": [
        "Day {int(timeframe*0.3)}: Foundation complete - Specific {proficiency}-level achievement",
        "Day {int(timeframe*0.65)}: First major project - Specific deliverable",
        "Day {int(timeframe*0.85)}: Advanced integration - Specific skill",
        "Day {timeframe}: Capstone done - Portfolio-ready work"
    ],
    "curriculum": [
        {{
            "day": 1,
            "topic": "Specific topic appropriate for {proficiency} learner, achievable in {hours_per_day} hours",
            "subtopics": [
                "Build/Create specific thing 1 (20-40 min)",
                "Implement specific feature 2 (20-40 min)",
                "Debug/Analyze specific problem 3 (20-40 min)"
            ],
            "estimated_hours": {hours_per_day},
            "priority": "high",
            "resources": [
                {{"type": "video", "name": "Real YouTube video title", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}},
                {{"type": "article", "name": "Real article title", "url": "https://realpython.com/python-basics/"}}
            ]
        }}
    ]
}}

QUALITY CHECKLIST (verify before submitting):
✓ EXACTLY {timeframe} days? (Count them!)
✓ Each day ≈ {hours_per_day} hours?
✓ Focus areas ({', '.join(focus_areas) if focus_areas else 'all topics'}) prioritized at 60-70%?
✓ ALL resource URLs are real and working? (NO placeholders!)
✓ Subtopics are action-oriented with deliverables?
✓ Progression from foundation → mastery?
✓ Difficulty matches {proficiency} level?
✓ Additional requests incorporated: "{other_requests if other_requests else 'N/A'}"?
✓ Total scope realistic for {total_hours} hours?

Generate the complete {timeframe}-day personalized curriculum now."""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                temperature=0.7,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}]
            )
            response_text = message.content[0].text
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
                json_text = response_text.strip()
            
            return json.loads(json_text)
        except Exception as e:
            raise Exception(f"Error generating personalized plan from template: {str(e)}")

    def generate_personalized_goal(self, proficiency: str, objectives: str, interests: str) -> Dict:
        """Generate a personalized goal using AI"""
        prompt = f"""As an expert goal designer, create a personalized goal based on the user's profile.

User Profile:
- Proficiency: {proficiency}
- Objectives: {objectives}
- Interests: {interests}

Generate a goal that is specific, measurable, achievable, relevant, and time-bound (SMART). 
Output in this JSON format:
{{
    "goal_text": "Your detailed, personalized goal here",
    "timeframe": 30, 
    "hours_per_day": 1.5,
    "description": "A brief summary of the goal and why it's relevant for the user."
}}
"""
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                temperature=0.8,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            response_text = message.content[0].text
            import json
            if "```json" in response_text:
                json_start = response_text.find("```json") + 7
                json_end = response_text.find("```", json_start)
                json_text = response_text[json_start:json_end].strip()
            else:
                json_text = response_text
            
            return json.loads(json_text)
        except Exception as e:
            raise Exception(f"Error generating personalized goal: {str(e)}")
