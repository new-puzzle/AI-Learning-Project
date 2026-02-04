"""
AI Prompt Generation for Learning Paths
Extracted and adapted from utils/ai_helpers.py

This module contains the prompt templates used to generate detailed learning paths
for topics like "prompt engineering", "n8n", etc.
"""

from typing import Dict, Optional


class LearningPathPrompts:
    """Generate system and user prompts for learning path generation"""
    
    @staticmethod
    def get_learning_path_prompt(
        topic: str,
        timeframe: int,
        hours_per_day: float = 2.0,
        proficiency: Optional[str] = None,
        focus_areas: Optional[list] = None,
        additional_requests: Optional[str] = None
    ) -> tuple[str, str]:
        """
        Generate system and user prompts for creating a learning path
        
        Args:
            topic: The topic to learn (e.g., "prompt engineering", "n8n")
            timeframe: Number of days for the learning path
            hours_per_day: Hours available per day
            proficiency: Optional proficiency level (Beginner/Intermediate/Advanced)
            focus_areas: Optional list of specific areas to focus on
            additional_requests: Optional additional requirements/preferences
            
        Returns:
            Tuple of (system_prompt, user_prompt)
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
        }.get(proficiency or 'Intermediate', {
            'approach': 'Practical focus',
            'pace': 'Moderate',
            'resources': 'Varied resources'
        })
        
        # Build system prompt
        system_prompt = f"""You are an expert curriculum architect. Create a {timeframe}-day structured learning plan.

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

7. PROFICIENCY ADAPTATION:
   - Content difficulty matches {proficiency or 'Intermediate'} level
   - Vocabulary: {"simple, explanatory" if proficiency == "Beginner" else "technical, in-depth" if proficiency == "Advanced" else "practical, applied"}
   - Examples: {"step-by-step" if proficiency == "Beginner" else "challenging" if proficiency == "Advanced" else "real-world"}

Return ONLY valid JSON. No markdown code blocks, no explanations."""

        # JSON Schema
        learning_schema = """{
    "overview": "2-3 sentences acknowledging the """ + str(timeframe) + """ days and """ + str(hours_per_day) + """ hours/day, explaining what will be achieved",
    "milestones": [
        "Day X: Foundation complete - Specific achievement",
        "Day Y: First project built - Specific deliverable",
        "Day Z: Advanced topics covered - Specific skill gained",
        "Day """ + str(timeframe) + """: Capstone done - Portfolio-ready outcome"
    ],
    "curriculum": [
        {
            "day": 1,
            "topic": "Specific, clear topic appropriate for """ + str(hours_per_day) + """ hours",
            "learning_objectives": [
                "Build/Create specific tangible thing",
                "Implement specific feature or solve specific problem"
            ],
            "estimated_hours": """ + str(hours_per_day) + """,
            "priority": "high",
            "resources": [
                {"type": "video", "name": "Real YouTube video title", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
                {"type": "article", "name": "Real article from Medium/Dev.to/docs", "url": "https://realpython.com/python-basics/"}
            ]
        }
    ]
}"""

        system_prompt += f"\n\nJSON Schema:\n{learning_schema}"

        # Build user prompt
        focus_text = ""
        if focus_areas:
            focus_text = f"\nFOCUS AREAS (prioritize these):\n- " + "\n- ".join(focus_areas) + "\n"
            focus_text += "- Allocate 60-70% of time to focus areas\n"
            focus_text += "- Introduce focus areas in first 20% of days\n"
            focus_text += "- Provide extra depth and resources for focus areas\n"
            focus_text += "- Still cover other topics at 30-40% depth\n"

        additional_text = ""
        if additional_requests:
            additional_text = f"\nADDITIONAL REQUIREMENTS:\n{additional_requests}\n"
            additional_text += "- Weave naturally throughout (don't just append at end)\n"
            additional_text += "- Integrate where relevant to topics\n"

        user_prompt = f"""Create a {timeframe}-day learning curriculum for: "{topic}"

TIME CONSTRAINTS:
- {hours_per_day} hours available per day
- {total_hours} hours total budget
- Each day must fit in {hours_per_day} hours

{focus_text}{additional_text}REQUIREMENTS:
- EXACTLY {timeframe} days (count them!)
- estimated_hours ≈ {hours_per_day} for each day
- {resource_count} per day (all real URLs)
- {objective_count} per day (all actionable)
- Clear progression: foundation → application → integration → mastery
- Realistic scope for {total_hours} total hours
- Difficulty level: {proficiency or 'Intermediate'}
- Approach: {prof_guide['approach']}
- Pace: {prof_guide['pace']}
- Resources: {prof_guide['resources']}

QUALITY CHECKLIST:
✓ Exactly {timeframe} days?
✓ Each day ≈ {hours_per_day} hours?
✓ All resource URLs real and working?
✓ Objectives use action verbs with deliverables?
✓ Progression from basic to advanced?
✓ Total scope realistic for {total_hours} hours?
{f"✓ Focus areas prioritized: {', '.join(focus_areas)}" if focus_areas else ""}
{f"✓ Additional requests incorporated: {additional_requests}" if additional_requests else ""}

Generate the complete curriculum now."""

        return system_prompt, user_prompt

