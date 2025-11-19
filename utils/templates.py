"""
Goal Templates for GoalPath AI - EXPANDED VERSION
Pre-configured goal templates to help users quick-start with proven goal structures
Organized by Category → Subdivision → Goals
"""

from typing import Dict, List


class GoalTemplate:
    """Represents a goal template with pre-filled values"""

    def __init__(self, name: str, goal_type: str, goal_text: str,
                 timeframe: int, hours_per_day: float, description: str,
                 tags: List[str] = None, difficulty: str = "Intermediate",
                 prerequisites: str = None, subdivisions: List[str] = None,
                 subdivision_category: str = None):
        self.name = name
        self.goal_type = goal_type
        self.goal_text = goal_text
        self.timeframe = timeframe
        self.hours_per_day = hours_per_day
        self.description = description
        self.tags = tags or []
        self.difficulty = difficulty
        self.prerequisites = prerequisites
        self.subdivisions = subdivisions or []
        self.subdivision_category = subdivision_category  # NEW: for filtering by subdivision

    def to_dict(self) -> Dict:
        """Convert template to dictionary"""
        return {
            'name': self.name,
            'goal_type': self.goal_type,
            'goal_text': self.goal_text,
            'timeframe': self.timeframe,
            'hours_per_day': self.hours_per_day,
            'description': self.description,
            'tags': self.tags,
            'difficulty': self.difficulty,
            'prerequisites': self.prerequisites,
            'subdivisions': self.subdivisions,
            'subdivision_category': self.subdivision_category
        }


# Template Registry
TEMPLATES = []


# ============================================================================
# PERSONAL CATEGORY - Subdivisions
# ============================================================================
# Subdivisions: Fitness/Health, Habits/Wellness, Creative Skills, 
#               Communication, Mental Health, Relationships


# ============================================================================
# PERSONAL → FITNESS/HEALTH (15 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Run Your First 5K Race",
    goal_type="personal",
    goal_text="Train for and complete first 5K race",
    timeframe=30,
    hours_per_day=1.0,
    description="Couch to 5K training plan, nutrition basics, race registration",
    tags=["Fitness", "Running", "Health", "Beginner-Friendly", "Cardio"],
    difficulty="Beginner",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Run First Half Marathon",
    goal_type="personal",
    goal_text="Train for and complete a half marathon (21.1km)",
    timeframe=90,
    hours_per_day=1.5,
    description="Build endurance from 5K to 21K, nutrition strategy, race day prep",
    tags=["Fitness", "Running", "Health", "Endurance", "Cardio"],
    difficulty="Intermediate",
    prerequisites="Can run 5K comfortably",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Lose 10 Pounds Sustainably",
    goal_type="personal",
    goal_text="Lose 10 pounds through sustainable nutrition and exercise habits",
    timeframe=45,
    hours_per_day=1.0,
    description="Nutrition plan, calorie tracking, exercise routine, habit formation",
    tags=["Fitness", "Health", "Weight Loss", "Nutrition"],
    difficulty="Intermediate",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Gain 10 Pounds of Muscle",
    goal_type="personal",
    goal_text="Build 10 pounds of lean muscle through strength training and nutrition",
    timeframe=90,
    hours_per_day=1.5,
    description="Progressive overload program, high-protein diet, supplement strategy, tracking",
    tags=["Fitness", "Strength Training", "Muscle Building", "Nutrition"],
    difficulty="Intermediate",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Complete 30-Day Strength Training Challenge",
    goal_type="personal",
    goal_text="Complete 30-day strength training program and build muscle",
    timeframe=30,
    hours_per_day=0.75,
    description="Full-body workout plan, progressive overload, nutrition, tracking",
    tags=["Fitness", "Strength Training", "Health", "Challenge"],
    difficulty="Beginner",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Master Calisthenics Fundamentals",
    goal_type="personal",
    goal_text="Master bodyweight exercises: pull-ups, dips, handstand push-ups",
    timeframe=60,
    hours_per_day=1.0,
    description="Progressions for pull-ups, dips, handstands, core strength",
    tags=["Fitness", "Calisthenics", "Bodyweight Training", "Strength"],
    difficulty="Intermediate",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Achieve First Muscle-Up",
    goal_type="personal",
    goal_text="Build strength and technique to perform your first muscle-up",
    timeframe=45,
    hours_per_day=1.0,
    description="Pull-up strength, explosive power, technique drills, progressions",
    tags=["Fitness", "Calisthenics", "Strength", "Skill Goal"],
    difficulty="Advanced",
    prerequisites="Can do 15+ pull-ups",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Improve Flexibility with Daily Yoga",
    goal_type="personal",
    goal_text="Establish daily yoga practice to improve flexibility and mobility",
    timeframe=30,
    hours_per_day=0.5,
    description="Daily yoga routines, flexibility progressions, injury prevention",
    tags=["Fitness", "Yoga", "Flexibility", "Mobility", "Wellness"],
    difficulty="Beginner",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Complete Ironman Triathlon",
    goal_type="personal",
    goal_text="Train for and complete Ironman: 3.8km swim, 180km bike, 42km run",
    timeframe=180,
    hours_per_day=2.5,
    description="Swimming, cycling, running training blocks, nutrition, recovery strategy",
    tags=["Fitness", "Triathlon", "Endurance", "Elite Challenge"],
    difficulty="Advanced",
    prerequisites="Strong base fitness in all three sports",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Master Swimming - Learn All 4 Strokes",
    goal_type="personal",
    goal_text="Learn and master all four competitive swimming strokes",
    timeframe=60,
    hours_per_day=1.0,
    description="Freestyle, backstroke, breaststroke, butterfly technique and endurance",
    tags=["Fitness", "Swimming", "Cardio", "Skill Building"],
    difficulty="Intermediate",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Fix Posture & Eliminate Back Pain",
    goal_type="personal",
    goal_text="Correct posture and eliminate chronic back pain through targeted exercises",
    timeframe=60,
    hours_per_day=0.5,
    description="Posture assessment, corrective exercises, ergonomics, core strengthening",
    tags=["Health", "Posture", "Pain Relief", "Wellness", "Ergonomics"],
    difficulty="Beginner",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Achieve Sub-20 Minute 5K",
    goal_type="personal",
    goal_text="Train to run 5K in under 20 minutes (elite amateur pace)",
    timeframe=90,
    hours_per_day=1.5,
    description="Speed work, interval training, tempo runs, race strategy",
    tags=["Fitness", "Running", "Speed", "Elite Goal", "Cardio"],
    difficulty="Advanced",
    prerequisites="Can run 5K in under 25 minutes",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Optimize Sleep Quality (8+ Hours Nightly)",
    goal_type="personal",
    goal_text="Achieve consistent 8+ hours of quality sleep every night",
    timeframe=30,
    hours_per_day=0.25,
    description="Sleep hygiene, routine establishment, tracking, optimization techniques",
    tags=["Health", "Sleep", "Wellness", "Recovery", "Habits"],
    difficulty="Beginner",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Complete 100 Push-ups Challenge",
    goal_type="personal",
    goal_text="Build up to doing 100 consecutive push-ups",
    timeframe=45,
    hours_per_day=0.5,
    description="Progressive push-up training plan, form perfection, endurance building",
    tags=["Fitness", "Strength", "Bodyweight", "Challenge"],
    difficulty="Intermediate",
    subdivision_category="Fitness/Health"
))

TEMPLATES.append(GoalTemplate(
    name="Train for First Obstacle Course Race",
    goal_type="personal",
    goal_text="Prepare for and complete obstacle course race (Tough Mudder/Spartan)",
    timeframe=60,
    hours_per_day=1.25,
    description="Grip strength, climbing, running endurance, obstacle-specific training",
    tags=["Fitness", "OCR", "Strength", "Endurance", "Adventure"],
    difficulty="Intermediate",
    subdivision_category="Fitness/Health"
))


# ============================================================================
# PERSONAL → HABITS/WELLNESS (15 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Build Bulletproof Morning Routine",
    goal_type="personal",
    goal_text="Establish consistent morning routine for productivity and wellness",
    timeframe=21,
    hours_per_day=0.5,
    description="Design optimal routine, track consistency for 21 days, make it stick",
    tags=["Habits", "Productivity", "Wellness", "Quick-Start", "Morning Routine"],
    difficulty="Beginner",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="Master Daily Meditation Practice",
    goal_type="personal",
    goal_text="Establish daily meditation practice for 30 consecutive days",
    timeframe=30,
    hours_per_day=0.33,
    description="Meditation techniques, apps (Headspace/Calm), consistency, mindfulness",
    tags=["Meditation", "Mental Health", "Habits", "Wellness", "Mindfulness"],
    difficulty="Beginner",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="Quit Social Media for 30 Days",
    goal_type="personal",
    goal_text="Complete 30-day digital detox from all social media platforms",
    timeframe=30,
    hours_per_day=0.25,
    description="Alternative activities, tracking time saved, mental clarity, productivity boost",
    tags=["Habits", "Digital Detox", "Mental Health", "Productivity", "Challenge"],
    difficulty="Intermediate",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="Establish Daily Journaling Habit",
    goal_type="personal",
    goal_text="Write in journal every day for 30 consecutive days",
    timeframe=30,
    hours_per_day=0.33,
    description="Morning pages, gratitude journaling, reflection prompts, consistency",
    tags=["Habits", "Journaling", "Mental Health", "Self-Reflection", "Writing"],
    difficulty="Beginner",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="30-Day No Alcohol Challenge",
    goal_type="personal",
    goal_text="Complete 30 days without consuming any alcohol",
    timeframe=30,
    hours_per_day=0.1,
    description="Health benefits tracking, social strategies, alternative beverages, habit breaking",
    tags=["Health", "Habits", "Challenge", "Wellness", "Sobriety"],
    difficulty="Intermediate",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="Drink 3 Liters of Water Daily",
    goal_type="personal",
    goal_text="Establish habit of drinking 3 liters of water every day for 30 days",
    timeframe=30,
    hours_per_day=0.1,
    description="Hydration tracking, reminder systems, health benefits monitoring",
    tags=["Health", "Habits", "Hydration", "Wellness", "Quick-Start"],
    difficulty="Beginner",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="30-Day Cold Shower Challenge",
    goal_type="personal",
    goal_text="Take cold showers every day for 30 consecutive days",
    timeframe=30,
    hours_per_day=0.16,
    description="Build mental toughness, health benefits, gradual temperature reduction, consistency",
    tags=["Habits", "Challenge", "Mental Toughness", "Wellness", "Health"],
    difficulty="Intermediate",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="Master Time Blocking Method",
    goal_type="personal",
    goal_text="Implement and master time blocking for 21 consecutive days",
    timeframe=21,
    hours_per_day=0.5,
    description="Calendar blocking, deep work sessions, task batching, reflection and optimization",
    tags=["Productivity", "Habits", "Time Management", "Focus", "Quick-Start"],
    difficulty="Beginner",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="Eliminate Phone Use During Meals",
    goal_type="personal",
    goal_text="Break phone addiction by not using phone during any meals for 30 days",
    timeframe=30,
    hours_per_day=0.1,
    description="Mindful eating, family connection, phone-free zones, alternative activities",
    tags=["Habits", "Digital Detox", "Mindfulness", "Family Time", "Wellness"],
    difficulty="Beginner",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="30-Day Gratitude Practice",
    goal_type="personal",
    goal_text="Write down 3 things you're grateful for every day for 30 days",
    timeframe=30,
    hours_per_day=0.16,
    description="Daily gratitude journaling, mental health benefits, positive mindset cultivation",
    tags=["Habits", "Gratitude", "Mental Health", "Wellness", "Journaling"],
    difficulty="Beginner",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="Achieve Inbox Zero Daily",
    goal_type="personal",
    goal_text="Process email to zero inbox every day for 21 consecutive days",
    timeframe=21,
    hours_per_day=0.5,
    description="Email processing system, filters, rules, zero-inbox methodology",
    tags=["Productivity", "Habits", "Organization", "Email Management", "Quick-Start"],
    difficulty="Beginner",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="Wake Up at 5 AM for 30 Days",
    goal_type="personal",
    goal_text="Establish habit of waking up at 5 AM every day for 30 consecutive days",
    timeframe=30,
    hours_per_day=0.16,
    description="Sleep schedule adjustment, morning routine, consistency tracking, optimization",
    tags=["Habits", "Morning Routine", "Productivity", "Challenge", "Discipline"],
    difficulty="Intermediate",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="30-Day Screen Time Reduction",
    goal_type="personal",
    goal_text="Reduce daily screen time by 50% and maintain for 30 days",
    timeframe=30,
    hours_per_day=0.25,
    description="Screen time tracking, alternative activities, app blockers, mindful usage",
    tags=["Habits", "Digital Detox", "Mental Health", "Productivity", "Wellness"],
    difficulty="Intermediate",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="Practice Daily Breathwork",
    goal_type="personal",
    goal_text="Complete daily breathwork exercises for 30 consecutive days",
    timeframe=30,
    hours_per_day=0.25,
    description="Wim Hof method, box breathing, stress reduction, energy optimization",
    tags=["Wellness", "Habits", "Breathwork", "Mental Health", "Stress Management"],
    difficulty="Beginner",
    subdivision_category="Habits/Wellness"
))

TEMPLATES.append(GoalTemplate(
    name="Implement Weekly Review System",
    goal_type="personal",
    goal_text="Conduct comprehensive weekly reviews for 12 consecutive weeks",
    timeframe=84,
    hours_per_day=0.5,
    description="GTD-style weekly reviews, goal tracking, reflection, planning system",
    tags=["Productivity", "Habits", "Planning", "Goal Setting", "Organization"],
    difficulty="Intermediate",
    subdivision_category="Habits/Wellness"
))


# ============================================================================
# PERSONAL → CREATIVE SKILLS (15 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Learn Guitar (Play 10 Songs)",
    goal_type="personal",
    goal_text="Learn guitar basics and master 10 songs",
    timeframe=60,
    hours_per_day=1.0,
    description="Guitar basics, chord progressions, strumming patterns, 10 song mastery",
    tags=["Music", "Creative", "Skill Building", "Guitar", "Beginner-Friendly"],
    difficulty="Beginner",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Master Piano Basics (Grade 1 Level)",
    goal_type="personal",
    goal_text="Learn piano fundamentals and reach Grade 1 performance level",
    timeframe=90,
    hours_per_day=1.0,
    description="Reading sheet music, scales, basic pieces, finger techniques",
    tags=["Music", "Piano", "Creative", "Skill Building"],
    difficulty="Beginner",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Establish Daily Writing Habit (500 Words)",
    goal_type="personal",
    goal_text="Write 500 words daily for 30 consecutive days",
    timeframe=30,
    hours_per_day=0.5,
    description="Daily writing practice, overcome resistance, build consistency, creativity",
    tags=["Writing", "Habits", "Creative", "Quick-Start", "Content Creation"],
    difficulty="Beginner",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Complete Novel Draft (50,000 Words)",
    goal_type="personal",
    goal_text="Write first draft of novel (50,000 words minimum)",
    timeframe=90,
    hours_per_day=2.0,
    description="Outlining, daily writing targets, character development, plot structure",
    tags=["Writing", "Creative", "Novel Writing", "Storytelling", "Long-Term"],
    difficulty="Advanced",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Digital Illustration (Procreate/Photoshop)",
    goal_type="personal",
    goal_text="Master digital illustration using Procreate or Photoshop",
    timeframe=60,
    hours_per_day=1.5,
    description="Digital tools mastery, drawing fundamentals, shading, coloring, portfolio pieces",
    tags=["Art", "Digital Art", "Creative", "Illustration", "Skill Building"],
    difficulty="Intermediate",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Master Photography Fundamentals",
    goal_type="personal",
    goal_text="Learn photography basics: composition, lighting, editing",
    timeframe=45,
    hours_per_day=1.0,
    description="Camera settings, composition rules, lighting, Lightroom editing, portfolio",
    tags=["Photography", "Creative", "Visual Arts", "Skill Building"],
    difficulty="Beginner",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Video Editing (Premiere Pro/DaVinci)",
    goal_type="personal",
    goal_text="Master video editing with Premiere Pro or DaVinci Resolve",
    timeframe=45,
    hours_per_day=1.5,
    description="Software mastery, cutting techniques, color grading, audio editing, effects",
    tags=["Video Editing", "Creative", "Skill Building", "Content Creation"],
    difficulty="Intermediate",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Complete 30-Day Drawing Challenge",
    goal_type="personal",
    goal_text="Draw something every day for 30 consecutive days",
    timeframe=30,
    hours_per_day=0.5,
    description="Daily sketching, fundamentals practice, creativity exercises, progress tracking",
    tags=["Art", "Drawing", "Creative", "Challenge", "Skill Building"],
    difficulty="Beginner",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Learn 3D Modeling (Blender Basics)",
    goal_type="personal",
    goal_text="Master Blender fundamentals and create 5 complete 3D models",
    timeframe=60,
    hours_per_day=2.0,
    description="Blender interface, modeling, texturing, lighting, rendering basics",
    tags=["3D Modeling", "Blender", "Creative", "Digital Art", "Skill Building"],
    difficulty="Intermediate",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Master Calligraphy & Hand Lettering",
    goal_type="personal",
    goal_text="Learn calligraphy and create beautiful hand-lettered pieces",
    timeframe=45,
    hours_per_day=1.0,
    description="Brush pen techniques, letter forms, composition, practice drills",
    tags=["Art", "Calligraphy", "Lettering", "Creative", "Skill Building"],
    difficulty="Beginner",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Singing (Voice Training Basics)",
    goal_type="personal",
    goal_text="Improve singing voice through structured vocal training",
    timeframe=60,
    hours_per_day=0.75,
    description="Breathing techniques, pitch control, vocal exercises, song repertoire",
    tags=["Music", "Singing", "Voice Training", "Creative", "Skill Building"],
    difficulty="Intermediate",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Master Portrait Drawing",
    goal_type="personal",
    goal_text="Learn to draw realistic portraits from photos and life",
    timeframe=90,
    hours_per_day=1.5,
    description="Proportions, shading, features, skin tones, complete 10 portraits",
    tags=["Art", "Drawing", "Portrait", "Creative", "Skill Building"],
    difficulty="Intermediate",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Learn DJ Skills & Music Production",
    goal_type="personal",
    goal_text="Master DJ mixing and basic music production",
    timeframe=60,
    hours_per_day=1.5,
    description="DJ software, mixing techniques, beatmatching, Ableton/FL Studio basics",
    tags=["Music", "DJ", "Production", "Creative", "Electronic Music"],
    difficulty="Intermediate",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Master Pottery/Ceramics Basics",
    goal_type="personal",
    goal_text="Learn pottery wheel throwing and hand-building techniques",
    timeframe=60,
    hours_per_day=2.0,
    description="Wheel throwing, hand-building, glazing, firing, create 10+ pieces",
    tags=["Art", "Pottery", "Ceramics", "Creative", "Hands-On", "Skill Building"],
    difficulty="Beginner",
    subdivision_category="Creative Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Animation Basics (2D/Motion Graphics)",
    goal_type="personal",
    goal_text="Master 2D animation and motion graphics with After Effects",
    timeframe=60,
    hours_per_day=2.0,
    description="Animation principles, After Effects, motion graphics, create 5 animations",
    tags=["Animation", "Motion Graphics", "Creative", "After Effects", "Skill Building"],
    difficulty="Intermediate",
    subdivision_category="Creative Skills"
))


# ============================================================================
# PERSONAL → COMMUNICATION (10 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Improve Public Speaking (10 Presentations)",
    goal_type="personal",
    goal_text="Deliver 10 presentations to improve public speaking skills",
    timeframe=45,
    hours_per_day=1.0,
    description="Toastmasters or practice groups, speaking techniques, deliver 10 talks",
    tags=["Public Speaking", "Communication", "Confidence", "Presentation Skills"],
    difficulty="Intermediate",
    subdivision_category="Communication"
))

TEMPLATES.append(GoalTemplate(
    name="Master Storytelling Skills",
    goal_type="personal",
    goal_text="Learn to craft and deliver compelling stories for personal and professional contexts",
    timeframe=30,
    hours_per_day=1.0,
    description="Story structure, narrative techniques, practice delivery, create story bank",
    tags=["Storytelling", "Communication", "Creative", "Presentation"],
    difficulty="Beginner",
    subdivision_category="Communication"
))

TEMPLATES.append(GoalTemplate(
    name="Achieve Conversational Spanish Fluency",
    goal_type="personal",
    goal_text="Reach conversational fluency in Spanish",
    timeframe=90,
    hours_per_day=1.0,
    description="Duolingo, iTalki tutors, conversation practice, immersion techniques",
    tags=["Language Learning", "Spanish", "Communication", "Fluency"],
    difficulty="Intermediate",
    subdivision_category="Communication"
))

TEMPLATES.append(GoalTemplate(
    name="Learn French Basics (A2 Level)",
    goal_type="personal",
    goal_text="Reach A2 level in French (elementary proficiency)",
    timeframe=60,
    hours_per_day=1.0,
    description="Grammar fundamentals, vocabulary building, conversation practice, DELF A2 prep",
    tags=["Language Learning", "French", "Communication", "Beginner-Friendly"],
    difficulty="Beginner",
    subdivision_category="Communication"
))

TEMPLATES.append(GoalTemplate(
    name="Master Business Email Writing",
    goal_type="personal",
    goal_text="Master professional email communication for business contexts",
    timeframe=14,
    hours_per_day=0.5,
    description="Email structure, tone, clarity, templates, professional correspondence",
    tags=["Communication", "Writing", "Business", "Professional", "Quick-Start"],
    difficulty="Beginner",
    subdivision_category="Communication"
))

TEMPLATES.append(GoalTemplate(
    name="Improve Active Listening Skills",
    goal_type="personal",
    goal_text="Develop active listening skills for better relationships and communication",
    timeframe=30,
    hours_per_day=0.5,
    description="Listening techniques, empathy building, feedback skills, practice exercises",
    tags=["Communication", "Listening", "Relationships", "Soft Skills", "Empathy"],
    difficulty="Beginner",
    subdivision_category="Communication"
))

TEMPLATES.append(GoalTemplate(
    name="Master Negotiation Skills",
    goal_type="personal",
    goal_text="Learn negotiation techniques for business and personal life",
    timeframe=30,
    hours_per_day=1.0,
    description="Negotiation principles, tactics, practice scenarios, win-win outcomes",
    tags=["Negotiation", "Communication", "Business", "Soft Skills", "Persuasion"],
    difficulty="Intermediate",
    subdivision_category="Communication"
))

TEMPLATES.append(GoalTemplate(
    name="Develop Assertiveness Skills",
    goal_type="personal",
    goal_text="Learn to communicate assertively while respecting others",
    timeframe=21,
    hours_per_day=0.5,
    description="Assertiveness techniques, boundary setting, confident communication, practice",
    tags=["Communication", "Assertiveness", "Confidence", "Soft Skills", "Quick-Start"],
    difficulty="Beginner",
    subdivision_category="Communication"
))

TEMPLATES.append(GoalTemplate(
    name="Master LinkedIn Networking",
    goal_type="personal",
    goal_text="Build LinkedIn presence and networking skills to expand professional network",
    timeframe=30,
    hours_per_day=0.5,
    description="Profile optimization, content creation, outreach strategies, relationship building",
    tags=["Networking", "LinkedIn", "Communication", "Professional", "Career"],
    difficulty="Beginner",
    subdivision_category="Communication"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Sign Language Basics",
    goal_type="personal",
    goal_text="Learn basic sign language for communication and accessibility",
    timeframe=60,
    hours_per_day=0.75,
    description="Basic signs, finger spelling, conversational phrases, practice with community",
    tags=["Language Learning", "Sign Language", "Communication", "Accessibility"],
    difficulty="Beginner",
    subdivision_category="Communication"
))


# ============================================================================
# PERSONAL → MENTAL HEALTH (10 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Overcome Anxiety with CBT Techniques",
    goal_type="personal",
    goal_text="Learn and apply Cognitive Behavioral Therapy techniques to manage anxiety",
    timeframe=60,
    hours_per_day=0.5,
    description="CBT principles, thought patterns, exposure therapy, coping strategies, journaling",
    tags=["Mental Health", "Anxiety", "CBT", "Therapy", "Wellness"],
    difficulty="Intermediate",
    subdivision_category="Mental Health"
))

TEMPLATES.append(GoalTemplate(
    name="Build Emotional Intelligence",
    goal_type="personal",
    goal_text="Develop emotional intelligence skills: self-awareness, empathy, regulation",
    timeframe=45,
    hours_per_day=0.75,
    description="Self-awareness exercises, empathy building, emotion regulation, social skills",
    tags=["Emotional Intelligence", "Mental Health", "Soft Skills", "Self-Improvement"],
    difficulty="Intermediate",
    subdivision_category="Mental Health"
))

TEMPLATES.append(GoalTemplate(
    name="Practice Mindfulness for Stress Reduction",
    goal_type="personal",
    goal_text="Establish daily mindfulness practice to reduce stress and increase awareness",
    timeframe=30,
    hours_per_day=0.5,
    description="Mindfulness meditation, body scans, mindful activities, stress tracking",
    tags=["Mindfulness", "Mental Health", "Stress Management", "Meditation", "Wellness"],
    difficulty="Beginner",
    subdivision_category="Mental Health"
))

TEMPLATES.append(GoalTemplate(
    name="Overcome Procrastination Permanently",
    goal_type="personal",
    goal_text="Identify root causes and eliminate procrastination habits",
    timeframe=30,
    hours_per_day=0.75,
    description="Root cause analysis, implementation intentions, accountability systems, habits",
    tags=["Productivity", "Mental Health", "Habits", "Self-Improvement", "Discipline"],
    difficulty="Intermediate",
    subdivision_category="Mental Health"
))

TEMPLATES.append(GoalTemplate(
    name="Develop Growth Mindset",
    goal_type="personal",
    goal_text="Shift from fixed to growth mindset through deliberate practice",
    timeframe=45,
    hours_per_day=0.5,
    description="Mindset awareness, reframing failures, embracing challenges, self-talk",
    tags=["Mental Health", "Growth Mindset", "Self-Improvement", "Psychology"],
    difficulty="Intermediate",
    subdivision_category="Mental Health"
))

TEMPLATES.append(GoalTemplate(
    name="Master Stress Management Techniques",
    goal_type="personal",
    goal_text="Learn and implement effective stress management strategies",
    timeframe=30,
    hours_per_day=0.5,
    description="Stress triggers, coping mechanisms, relaxation techniques, lifestyle changes",
    tags=["Stress Management", "Mental Health", "Wellness", "Coping Skills"],
    difficulty="Beginner",
    subdivision_category="Mental Health"
))

TEMPLATES.append(GoalTemplate(
    name="Build Self-Confidence Through Action",
    goal_type="personal",
    goal_text="Systematically build self-confidence through progressive challenges",
    timeframe=60,
    hours_per_day=1.0,
    description="Confidence-building exercises, progressive exposure, competence development",
    tags=["Confidence", "Mental Health", "Self-Improvement", "Personal Growth"],
    difficulty="Intermediate",
    subdivision_category="Mental Health"
))

TEMPLATES.append(GoalTemplate(
    name="Overcome Perfectionism",
    goal_type="personal",
    goal_text="Break perfectionism patterns and embrace 'good enough'",
    timeframe=30,
    hours_per_day=0.5,
    description="Perfectionism awareness, exposure to imperfection, productivity gains",
    tags=["Mental Health", "Perfectionism", "Self-Improvement", "Productivity"],
    difficulty="Intermediate",
    subdivision_category="Mental Health"
))

TEMPLATES.append(GoalTemplate(
    name="Develop Resilience & Mental Toughness",
    goal_type="personal",
    goal_text="Build resilience to handle setbacks and challenges effectively",
    timeframe=45,
    hours_per_day=0.75,
    description="Resilience skills, reframing adversity, stress inoculation, growth from failure",
    tags=["Resilience", "Mental Health", "Mental Toughness", "Self-Improvement"],
    difficulty="Intermediate",
    subdivision_category="Mental Health"
))

TEMPLATES.append(GoalTemplate(
    name="Practice Self-Compassion Daily",
    goal_type="personal",
    goal_text="Develop self-compassion practice to reduce self-criticism",
    timeframe=30,
    hours_per_day=0.33,
    description="Self-compassion exercises, mindful self-talk, treating yourself kindly",
    tags=["Self-Compassion", "Mental Health", "Mindfulness", "Wellness"],
    difficulty="Beginner",
    subdivision_category="Mental Health"
))


# ============================================================================
# PERSONAL → RELATIONSHIPS (8 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Strengthen Romantic Relationship",
    goal_type="personal",
    goal_text="Improve romantic relationship through intentional practices",
    timeframe=60,
    hours_per_day=0.5,
    description="Communication skills, quality time rituals, conflict resolution, love languages",
    tags=["Relationships", "Romance", "Communication", "Personal Growth"],
    difficulty="Intermediate",
    subdivision_category="Relationships"
))

TEMPLATES.append(GoalTemplate(
    name="Build Deeper Friendships",
    goal_type="personal",
    goal_text="Cultivate 3-5 deep, meaningful friendships",
    timeframe=90,
    hours_per_day=0.75,
    description="Regular connection, vulnerability, quality time, friendship maintenance",
    tags=["Relationships", "Friendship", "Social Skills", "Connection"],
    difficulty="Intermediate",
    subdivision_category="Relationships"
))

TEMPLATES.append(GoalTemplate(
    name="Improve Family Relationships",
    goal_type="personal",
    goal_text="Strengthen bonds with family members through intentional connection",
    timeframe=60,
    hours_per_day=0.5,
    description="Regular communication, quality time, conflict resolution, boundaries",
    tags=["Relationships", "Family", "Communication", "Personal Growth"],
    difficulty="Intermediate",
    subdivision_category="Relationships"
))

TEMPLATES.append(GoalTemplate(
    name="Master Conflict Resolution",
    goal_type="personal",
    goal_text="Learn to resolve conflicts constructively in all relationships",
    timeframe=30,
    hours_per_day=0.5,
    description="Conflict resolution frameworks, de-escalation, active listening, compromise",
    tags=["Relationships", "Conflict Resolution", "Communication", "Soft Skills"],
    difficulty="Intermediate",
    subdivision_category="Relationships"
))

TEMPLATES.append(GoalTemplate(
    name="Set Healthy Boundaries",
    goal_type="personal",
    goal_text="Learn to set and maintain healthy boundaries in all relationships",
    timeframe=30,
    hours_per_day=0.5,
    description="Boundary identification, assertive communication, maintaining boundaries, self-care",
    tags=["Relationships", "Boundaries", "Self-Care", "Communication", "Mental Health"],
    difficulty="Intermediate",
    subdivision_category="Relationships"
))

TEMPLATES.append(GoalTemplate(
    name="Expand Social Circle",
    goal_type="personal",
    goal_text="Meet 20+ new people and build new friendships",
    timeframe=60,
    hours_per_day=1.0,
    description="Meetup groups, events, hobbies, conversation skills, follow-up strategies",
    tags=["Relationships", "Networking", "Social Skills", "Friendship", "Connection"],
    difficulty="Beginner",
    subdivision_category="Relationships"
))

TEMPLATES.append(GoalTemplate(
    name="Become Better Parent/Caregiver",
    goal_type="personal",
    goal_text="Develop parenting/caregiving skills for better relationships with children",
    timeframe=60,
    hours_per_day=1.0,
    description="Parenting strategies, quality time, communication, discipline approaches",
    tags=["Relationships", "Parenting", "Family", "Personal Growth", "Caregiving"],
    difficulty="Intermediate",
    subdivision_category="Relationships"
))

TEMPLATES.append(GoalTemplate(
    name="Reconnect with Old Friends",
    goal_type="personal",
    goal_text="Reconnect with 10 old friends and rebuild relationships",
    timeframe=30,
    hours_per_day=0.5,
    description="Reach out strategies, conversation starters, meeting planning, relationship rebuilding",
    tags=["Relationships", "Friendship", "Reconnection", "Social Skills"],
    difficulty="Beginner",
    subdivision_category="Relationships"
))


# ============================================================================
# LEARNING CATEGORY - Subdivisions
# ============================================================================
# Subdivisions: Tech Skills, STEM, Arts/Creative, Languages,
#               Business/Finance, Mental Practices, Personality Development


# ============================================================================
# LEARNING → TECH SKILLS (20 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Master Prompt Engineering",
    goal_type="learning",
    goal_text="Master prompt engineering for Claude, GPT, and modern AI models",
    timeframe=30,
    hours_per_day=2.0,
    description="Learn prompt design, Claude/GPT best practices, build portfolio of prompts",
    tags=["AI", "Prompt Engineering", "Remote-Friendly", "Beginner-Friendly", "In-Demand"],
    difficulty="Beginner",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Python for Data Science",
    goal_type="learning",
    goal_text="Learn Python data science stack: NumPy, Pandas, Matplotlib, and build real-world projects",
    timeframe=60,
    hours_per_day=2.0,
    description="NumPy, Pandas, Matplotlib, Seaborn, scikit-learn, real-world data projects",
    tags=["Python", "Data Science", "Portfolio-Building", "Analytics"],
    difficulty="Intermediate",
    prerequisites="Basic Python knowledge recommended",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Full-Stack Web Development (MERN)",
    goal_type="learning",
    goal_text="Master full-stack web development with MongoDB, Express, React, and Node.js",
    timeframe=90,
    hours_per_day=3.0,
    description="MongoDB, Express, React, Node.js - build 3 full-stack apps",
    tags=["Web Development", "Full-Stack", "Portfolio-Building", "JavaScript"],
    difficulty="Intermediate",
    prerequisites="HTML, CSS, JavaScript basics",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="AI/ML Fundamentals for Career Switchers",
    goal_type="learning",
    goal_text="Learn AI and machine learning fundamentals to switch into AI engineering",
    timeframe=45,
    hours_per_day=2.5,
    description="Machine learning basics, scikit-learn, neural networks, practical projects",
    tags=["AI", "Machine Learning", "Career Switch", "Portfolio-Building"],
    difficulty="Intermediate",
    prerequisites="Python basics, high school math",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="No-Code App Builder Mastery",
    goal_type="learning",
    goal_text="Master no-code platforms: Bubble, Webflow, and Airtable automation",
    timeframe=21,
    hours_per_day=1.5,
    description="Bubble, Webflow, Airtable automation - launch 2 apps",
    tags=["No-Code", "Beginner-Friendly", "Quick-Start", "Portfolio-Building"],
    difficulty="Beginner",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="FastAPI & Modern Python Backend",
    goal_type="learning",
    goal_text="Master FastAPI for building production-ready Python APIs",
    timeframe=30,
    hours_per_day=2.0,
    description="REST APIs, async Python, authentication, testing, deployment",
    tags=["Python", "Backend", "API Development", "FastAPI"],
    difficulty="Intermediate",
    prerequisites="Python basics",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="DevOps for Python Developers",
    goal_type="learning",
    goal_text="Learn DevOps essentials: Docker, CI/CD, and cloud deployment for Python apps",
    timeframe=45,
    hours_per_day=2.0,
    description="Docker, GitHub Actions, AWS/GCP deployment, monitoring",
    tags=["DevOps", "Python", "Cloud", "Career-Boost", "CI/CD"],
    difficulty="Intermediate",
    prerequisites="Python development experience",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="LangChain & AI Application Development",
    goal_type="learning",
    goal_text="Build AI applications with LangChain, vector databases, and RAG systems",
    timeframe=30,
    hours_per_day=2.0,
    description="Build AI apps with LangChain, vector databases, RAG systems",
    tags=["AI", "LangChain", "In-Demand", "Portfolio-Building", "RAG"],
    difficulty="Intermediate",
    prerequisites="Python basics, basic AI understanding",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Master React & Modern Frontend",
    goal_type="learning",
    goal_text="Master React, hooks, state management, and modern frontend development",
    timeframe=60,
    hours_per_day=2.5,
    description="React, hooks, Redux/Context, Next.js, Tailwind CSS, build 5 projects",
    tags=["React", "Frontend", "JavaScript", "Web Development", "Portfolio-Building"],
    difficulty="Intermediate",
    prerequisites="JavaScript fundamentals",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Cybersecurity Fundamentals & Ethical Hacking",
    goal_type="learning",
    goal_text="Learn cybersecurity basics and ethical hacking principles",
    timeframe=60,
    hours_per_day=2.0,
    description="Network security, penetration testing, Kali Linux, certifications prep",
    tags=["Cybersecurity", "Ethical Hacking", "Security", "Career-Boost", "In-Demand"],
    difficulty="Intermediate",
    prerequisites="Basic networking knowledge",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Master SQL & Database Design",
    goal_type="learning",
    goal_text="Master SQL querying and relational database design principles",
    timeframe=30,
    hours_per_day=1.5,
    description="SQL queries, joins, indexes, normalization, PostgreSQL/MySQL, projects",
    tags=["SQL", "Database", "Backend", "Data Analysis", "Essential Skill"],
    difficulty="Beginner",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Rust Programming Language",
    goal_type="learning",
    goal_text="Master Rust for systems programming and performance-critical applications",
    timeframe=60,
    hours_per_day=2.0,
    description="Rust syntax, ownership model, error handling, build CLI tools and projects",
    tags=["Rust", "Systems Programming", "Performance", "Advanced", "In-Demand"],
    difficulty="Advanced",
    prerequisites="Programming experience in another language",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Master Git & GitHub Workflows",
    goal_type="learning",
    goal_text="Master Git version control and GitHub collaboration workflows",
    timeframe=14,
    hours_per_day=1.0,
    description="Git commands, branching, pull requests, GitHub Actions, best practices",
    tags=["Git", "GitHub", "Version Control", "Essential Skill", "Quick-Start"],
    difficulty="Beginner",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Learn TypeScript for Modern Web Dev",
    goal_type="learning",
    goal_text="Master TypeScript for type-safe JavaScript development",
    timeframe=30,
    hours_per_day=1.5,
    description="TypeScript syntax, types, interfaces, generics, React with TypeScript",
    tags=["TypeScript", "JavaScript", "Web Development", "Type Safety"],
    difficulty="Intermediate",
    prerequisites="JavaScript proficiency",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Master AWS Cloud Practitioner",
    goal_type="learning",
    goal_text="Learn AWS fundamentals and pass Cloud Practitioner certification",
    timeframe=45,
    hours_per_day=1.5,
    description="AWS services, cloud concepts, pricing, security, certification exam prep",
    tags=["AWS", "Cloud", "Certification", "Career-Boost", "In-Demand"],
    difficulty="Beginner",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Mobile App Development (React Native)",
    goal_type="learning",
    goal_text="Build cross-platform mobile apps with React Native",
    timeframe=60,
    hours_per_day=2.5,
    description="React Native, navigation, state management, API integration, build 3 apps",
    tags=["Mobile Development", "React Native", "Portfolio-Building", "Cross-Platform"],
    difficulty="Intermediate",
    prerequisites="JavaScript and React basics",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Master Data Visualization (D3.js, Plotly)",
    goal_type="learning",
    goal_text="Create interactive data visualizations with D3.js and Plotly",
    timeframe=45,
    hours_per_day=2.0,
    description="D3.js fundamentals, charts, interactive dashboards, storytelling with data",
    tags=["Data Visualization", "D3.js", "JavaScript", "Analytics", "Portfolio-Building"],
    difficulty="Intermediate",
    prerequisites="JavaScript basics, data analysis familiarity",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Kubernetes & Container Orchestration",
    goal_type="learning",
    goal_text="Master Kubernetes for container orchestration and deployment",
    timeframe=45,
    hours_per_day=2.0,
    description="Kubernetes concepts, pods, services, deployments, Helm, production setup",
    tags=["Kubernetes", "DevOps", "Containers", "Cloud", "Advanced"],
    difficulty="Advanced",
    prerequisites="Docker experience, basic cloud knowledge",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Master GraphQL API Development",
    goal_type="learning",
    goal_text="Learn GraphQL for modern API development",
    timeframe=30,
    hours_per_day=1.5,
    description="GraphQL basics, schema design, resolvers, Apollo Server, client integration",
    tags=["GraphQL", "API", "Backend", "Web Development", "Modern Stack"],
    difficulty="Intermediate",
    prerequisites="REST API knowledge",
    subdivision_category="Tech Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Blockchain & Web3 Development",
    goal_type="learning",
    goal_text="Master blockchain fundamentals and smart contract development",
    timeframe=60,
    hours_per_day=2.5,
    description="Blockchain concepts, Solidity, Ethereum, smart contracts, dApp development",
    tags=["Blockchain", "Web3", "Solidity", "Cryptocurrency", "Emerging Tech"],
    difficulty="Advanced",
    prerequisites="Programming experience, preferably JavaScript",
    subdivision_category="Tech Skills"
))


# ============================================================================
# LEARNING → STEM (15 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Master Calculus I (Single Variable)",
    goal_type="learning",
    goal_text="Master single-variable calculus: limits, derivatives, integrals",
    timeframe=90,
    hours_per_day=2.0,
    description="Limits, differentiation, integration, applications, problem-solving",
    tags=["Math", "Calculus", "STEM", "Academic", "Foundational"],
    difficulty="Intermediate",
    prerequisites="Algebra and trigonometry",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Linear Algebra for ML",
    goal_type="learning",
    goal_text="Master linear algebra concepts essential for machine learning",
    timeframe=45,
    hours_per_day=1.5,
    description="Vectors, matrices, eigenvalues, transformations, ML applications",
    tags=["Math", "Linear Algebra", "Machine Learning", "STEM"],
    difficulty="Intermediate",
    prerequisites="Basic algebra",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Master Statistics & Probability",
    goal_type="learning",
    goal_text="Learn statistics and probability for data science and research",
    timeframe=60,
    hours_per_day=2.0,
    description="Descriptive stats, probability, distributions, hypothesis testing, regression",
    tags=["Statistics", "Math", "Data Science", "STEM", "Analytics"],
    difficulty="Intermediate",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Physics I (Mechanics)",
    goal_type="learning",
    goal_text="Master classical mechanics: Newton's laws, energy, momentum",
    timeframe=90,
    hours_per_day=2.5,
    description="Kinematics, dynamics, work-energy, momentum, rotational motion",
    tags=["Physics", "Mechanics", "STEM", "Science", "Foundational"],
    difficulty="Intermediate",
    prerequisites="Calculus basics",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Master Organic Chemistry Fundamentals",
    goal_type="learning",
    goal_text="Learn organic chemistry: structure, reactions, mechanisms",
    timeframe=90,
    hours_per_day=2.5,
    description="Molecular structure, nomenclature, reactions, stereochemistry, mechanisms",
    tags=["Chemistry", "Organic Chemistry", "STEM", "Science"],
    difficulty="Advanced",
    prerequisites="General chemistry background",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Molecular Biology Basics",
    goal_type="learning",
    goal_text="Master molecular biology: DNA, RNA, proteins, gene expression",
    timeframe=60,
    hours_per_day=2.0,
    description="DNA structure, replication, transcription, translation, gene regulation",
    tags=["Biology", "Molecular Biology", "STEM", "Science", "Genetics"],
    difficulty="Intermediate",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Master Differential Equations",
    goal_type="learning",
    goal_text="Learn ordinary differential equations and applications",
    timeframe=60,
    hours_per_day=2.0,
    description="First/second order ODEs, systems, Laplace transforms, applications",
    tags=["Math", "Differential Equations", "STEM", "Engineering", "Physics"],
    difficulty="Advanced",
    prerequisites="Calculus II",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Electronics & Circuit Design",
    goal_type="learning",
    goal_text="Master electronics fundamentals and circuit design",
    timeframe=60,
    hours_per_day=2.0,
    description="Circuit theory, components, breadboarding, Arduino projects, troubleshooting",
    tags=["Electronics", "Engineering", "STEM", "Hardware", "Hands-On"],
    difficulty="Intermediate",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Master Python for Scientific Computing",
    goal_type="learning",
    goal_text="Learn Python for scientific computing: NumPy, SciPy, simulations",
    timeframe=45,
    hours_per_day=2.0,
    description="NumPy, SciPy, symbolic math, simulations, scientific applications",
    tags=["Python", "Scientific Computing", "STEM", "Programming", "Research"],
    difficulty="Intermediate",
    prerequisites="Python basics, calculus knowledge",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Thermodynamics Fundamentals",
    goal_type="learning",
    goal_text="Master classical thermodynamics: laws, entropy, heat engines",
    timeframe=60,
    hours_per_day=2.0,
    description="Laws of thermodynamics, entropy, heat engines, phase transitions",
    tags=["Physics", "Thermodynamics", "STEM", "Engineering", "Science"],
    difficulty="Intermediate",
    prerequisites="Calculus, basic physics",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Master Astronomy & Astrophysics Basics",
    goal_type="learning",
    goal_text="Learn astronomy and astrophysics fundamentals",
    timeframe=60,
    hours_per_day=1.5,
    description="Celestial mechanics, stars, galaxies, cosmology, observational techniques",
    tags=["Astronomy", "Physics", "STEM", "Science", "Space"],
    difficulty="Intermediate",
    prerequisites="Basic physics knowledge",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Quantum Mechanics Introduction",
    goal_type="learning",
    goal_text="Master introductory quantum mechanics concepts",
    timeframe=90,
    hours_per_day=2.5,
    description="Wave functions, Schrödinger equation, quantum states, measurement",
    tags=["Physics", "Quantum Mechanics", "STEM", "Advanced", "Science"],
    difficulty="Advanced",
    prerequisites="Calculus III, linear algebra, classical mechanics",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Master Discrete Mathematics",
    goal_type="learning",
    goal_text="Learn discrete math for computer science: logic, sets, graphs",
    timeframe=60,
    hours_per_day=2.0,
    description="Logic, sets, combinatorics, graph theory, algorithms",
    tags=["Math", "Discrete Math", "STEM", "Computer Science", "Logic"],
    difficulty="Intermediate",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Materials Science Fundamentals",
    goal_type="learning",
    goal_text="Master materials science: structure, properties, applications",
    timeframe=60,
    hours_per_day=2.0,
    description="Atomic structure, bonding, mechanical properties, phase diagrams",
    tags=["Materials Science", "Engineering", "STEM", "Science"],
    difficulty="Intermediate",
    prerequisites="Chemistry and physics basics",
    subdivision_category="STEM"
))

TEMPLATES.append(GoalTemplate(
    name="Master Neuroscience Basics",
    goal_type="learning",
    goal_text="Learn neuroscience fundamentals: brain structure, neurons, cognition",
    timeframe=60,
    hours_per_day=2.0,
    description="Neuroanatomy, neural signaling, sensory systems, cognitive functions",
    tags=["Neuroscience", "Biology", "STEM", "Science", "Brain"],
    difficulty="Intermediate",
    subdivision_category="STEM"
))


# ============================================================================
# LEARNING → ARTS/CREATIVE (10 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Master Music Theory Fundamentals",
    goal_type="learning",
    goal_text="Learn music theory: scales, chords, harmony, composition",
    timeframe=60,
    hours_per_day=1.0,
    description="Scales, intervals, chords, progressions, ear training, composition basics",
    tags=["Music", "Music Theory", "Arts", "Creative", "Foundational"],
    difficulty="Beginner",
    subdivision_category="Arts/Creative"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Classical Drawing Techniques",
    goal_type="learning",
    goal_text="Master classical drawing: perspective, anatomy, shading",
    timeframe=90,
    hours_per_day=2.0,
    description="Perspective, anatomy, light and shadow, composition, master studies",
    tags=["Art", "Drawing", "Creative", "Classical Techniques", "Skill Building"],
    difficulty="Intermediate",
    subdivision_category="Arts/Creative"
))

TEMPLATES.append(GoalTemplate(
    name="Master Color Theory for Artists",
    goal_type="learning",
    goal_text="Learn color theory principles for visual arts",
    timeframe=30,
    hours_per_day=1.5,
    description="Color wheels, harmony, mixing, temperature, emotional impact",
    tags=["Art", "Color Theory", "Creative", "Visual Arts", "Design"],
    difficulty="Beginner",
    subdivision_category="Arts/Creative"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Film Analysis & Criticism",
    goal_type="learning",
    goal_text="Master film analysis: cinematography, narrative, themes",
    timeframe=45,
    hours_per_day=2.0,
    description="Film language, analysis frameworks, auteur theory, genre study",
    tags=["Film", "Arts", "Analysis", "Creative", "Critical Thinking"],
    difficulty="Intermediate",
    subdivision_category="Arts/Creative"
))

TEMPLATES.append(GoalTemplate(
    name="Master Creative Writing Techniques",
    goal_type="learning",
    goal_text="Learn creative writing: character, plot, voice, style",
    timeframe=60,
    hours_per_day=1.5,
    description="Story structure, character development, dialogue, voice, workshopping",
    tags=["Writing", "Creative Writing", "Arts", "Storytelling", "Literature"],
    difficulty="Intermediate",
    subdivision_category="Arts/Creative"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Art History (Renaissance to Modern)",
    goal_type="learning",
    goal_text="Master art history from Renaissance through modern movements",
    timeframe=60,
    hours_per_day=1.5,
    description="Major periods, artists, movements, cultural context, analysis skills",
    tags=["Art History", "Arts", "History", "Cultural Studies", "Visual Arts"],
    difficulty="Beginner",
    subdivision_category="Arts/Creative"
))

TEMPLATES.append(GoalTemplate(
    name="Master Typography & Font Design",
    goal_type="learning",
    goal_text="Learn typography principles and basic font design",
    timeframe=30,
    hours_per_day=1.5,
    description="Type anatomy, pairing, hierarchy, readability, font creation basics",
    tags=["Typography", "Design", "Arts", "Graphic Design", "Visual Communication"],
    difficulty="Intermediate",
    subdivision_category="Arts/Creative"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Poetry Writing & Analysis",
    goal_type="learning",
    goal_text="Master poetry writing: forms, devices, contemporary practice",
    timeframe=45,
    hours_per_day=1.0,
    description="Poetic forms, devices, imagery, voice, contemporary styles, workshopping",
    tags=["Poetry", "Writing", "Arts", "Literature", "Creative"],
    difficulty="Intermediate",
    subdivision_category="Arts/Creative"
))

TEMPLATES.append(GoalTemplate(
    name="Master UI/UX Design Principles",
    goal_type="learning",
    goal_text="Learn user interface and experience design fundamentals",
    timeframe=60,
    hours_per_day=2.0,
    description="UX research, wireframing, prototyping, Figma, usability testing",
    tags=["UI/UX", "Design", "Creative", "Digital Design", "User Experience"],
    difficulty="Intermediate",
    subdivision_category="Arts/Creative"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Acting & Performance Techniques",
    goal_type="learning",
    goal_text="Master acting fundamentals: method, voice, movement",
    timeframe=60,
    hours_per_day=2.0,
    description="Acting methods, voice training, movement, scene work, character development",
    tags=["Acting", "Theater", "Arts", "Performance", "Creative"],
    difficulty="Intermediate",
    subdivision_category="Arts/Creative"
))


# ============================================================================
# LEARNING → LANGUAGES (8 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Master Spanish to B2 Fluency",
    goal_type="learning",
    goal_text="Achieve B2 level Spanish fluency for advanced conversations",
    timeframe=180,
    hours_per_day=1.5,
    description="Grammar mastery, vocabulary expansion, conversation practice, media immersion",
    tags=["Language Learning", "Spanish", "Fluency", "Communication", "Long-Term"],
    difficulty="Advanced",
    prerequisites="Basic Spanish (A2 level)",
    subdivision_category="Languages"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Japanese to JLPT N5",
    goal_type="learning",
    goal_text="Master Japanese basics and pass JLPT N5 exam",
    timeframe=90,
    hours_per_day=2.0,
    description="Hiragana, katakana, basic kanji, grammar patterns, JLPT N5 prep",
    tags=["Language Learning", "Japanese", "JLPT", "Communication", "Beginner-Friendly"],
    difficulty="Beginner",
    subdivision_category="Languages"
))

TEMPLATES.append(GoalTemplate(
    name="Master German to B1 Level",
    goal_type="learning",
    goal_text="Achieve B1 German proficiency for independent usage",
    timeframe=120,
    hours_per_day=1.5,
    description="Grammar, vocabulary, conversation practice, listening comprehension",
    tags=["Language Learning", "German", "Communication", "Fluency"],
    difficulty="Intermediate",
    subdivision_category="Languages"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Mandarin Chinese Basics (HSK 2)",
    goal_type="learning",
    goal_text="Master Mandarin basics and pass HSK Level 2 exam",
    timeframe=90,
    hours_per_day=2.0,
    description="Pinyin, tones, basic characters, grammar, HSK 2 vocabulary and patterns",
    tags=["Language Learning", "Mandarin", "Chinese", "HSK", "Communication"],
    difficulty="Beginner",
    subdivision_category="Languages"
))

TEMPLATES.append(GoalTemplate(
    name="Master Italian to A2 Level",
    goal_type="learning",
    goal_text="Learn Italian basics to A2 elementary proficiency",
    timeframe=60,
    hours_per_day=1.5,
    description="Pronunciation, grammar fundamentals, vocabulary, conversation practice",
    tags=["Language Learning", "Italian", "Communication", "Beginner-Friendly"],
    difficulty="Beginner",
    subdivision_category="Languages"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Korean to TOPIK Level 1",
    goal_type="learning",
    goal_text="Master Korean basics and pass TOPIK Level 1 exam",
    timeframe=90,
    hours_per_day=2.0,
    description="Hangul, grammar patterns, vocabulary, TOPIK 1 preparation",
    tags=["Language Learning", "Korean", "TOPIK", "Communication"],
    difficulty="Beginner",
    subdivision_category="Languages"
))

TEMPLATES.append(GoalTemplate(
    name="Master Portuguese to B1 Level",
    goal_type="learning",
    goal_text="Achieve B1 Portuguese for independent communication",
    timeframe=90,
    hours_per_day=1.5,
    description="Brazilian or European Portuguese, grammar, conversation, media immersion",
    tags=["Language Learning", "Portuguese", "Communication", "Fluency"],
    difficulty="Intermediate",
    subdivision_category="Languages"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Arabic Fundamentals (MSA)",
    goal_type="learning",
    goal_text="Master Modern Standard Arabic basics: script, grammar, vocabulary",
    timeframe=90,
    hours_per_day=2.0,
    description="Arabic script, pronunciation, grammar fundamentals, vocabulary building",
    tags=["Language Learning", "Arabic", "Communication", "MSA"],
    difficulty="Intermediate",
    subdivision_category="Languages"
))


# ============================================================================
# LEARNING → BUSINESS/FINANCE (12 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Master Financial Analysis & Modeling",
    goal_type="learning",
    goal_text="Learn financial analysis and Excel modeling for business decisions",
    timeframe=60,
    hours_per_day=2.0,
    description="Financial statements, ratios, DCF models, Excel mastery, business valuation",
    tags=["Finance", "Business", "Excel", "Analysis", "Career-Boost"],
    difficulty="Intermediate",
    subdivision_category="Business/Finance"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Stock Market Investing Fundamentals",
    goal_type="learning",
    goal_text="Master stock investing: analysis, portfolio management, strategy",
    timeframe=45,
    hours_per_day=1.5,
    description="Fundamental analysis, technical analysis, portfolio theory, risk management",
    tags=["Finance", "Investing", "Stock Market", "Personal Finance", "Wealth Building"],
    difficulty="Intermediate",
    subdivision_category="Business/Finance"
))

TEMPLATES.append(GoalTemplate(
    name="Master Digital Marketing Fundamentals",
    goal_type="learning",
    goal_text="Learn digital marketing: SEO, social media, ads, analytics",
    timeframe=45,
    hours_per_day=2.0,
    description="SEO, content marketing, social media, PPC ads, Google Analytics",
    tags=["Marketing", "Digital Marketing", "Business", "Career-Boost", "In-Demand"],
    difficulty="Beginner",
    subdivision_category="Business/Finance"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Personal Finance & Wealth Building",
    goal_type="learning",
    goal_text="Master personal finance: budgeting, investing, wealth building",
    timeframe=30,
    hours_per_day=1.0,
    description="Budgeting, saving, investing, retirement planning, debt management",
    tags=["Personal Finance", "Finance", "Wealth Building", "Life Skills", "Money Management"],
    difficulty="Beginner",
    subdivision_category="Business/Finance"
))

TEMPLATES.append(GoalTemplate(
    name="Master Project Management (PMP Prep)",
    goal_type="learning",
    goal_text="Learn project management and prepare for PMP certification",
    timeframe=90,
    hours_per_day=2.0,
    description="PMBOK guide, project lifecycle, agile, risk management, PMP exam prep",
    tags=["Project Management", "Business", "PMP", "Certification", "Career-Boost"],
    difficulty="Intermediate",
    subdivision_category="Business/Finance"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Business Strategy & Frameworks",
    goal_type="learning",
    goal_text="Master business strategy frameworks for consulting and management",
    timeframe=45,
    hours_per_day=1.5,
    description="Porter's 5 Forces, SWOT, BCG matrix, case interview frameworks",
    tags=["Business Strategy", "Consulting", "Business", "Frameworks", "MBA-Level"],
    difficulty="Intermediate",
    subdivision_category="Business/Finance"
))

TEMPLATES.append(GoalTemplate(
    name="Master Accounting Fundamentals",
    goal_type="learning",
    goal_text="Learn accounting basics: financial statements, journal entries, principles",
    timeframe=60,
    hours_per_day=1.5,
    description="Debits/credits, financial statements, GAAP principles, basic bookkeeping",
    tags=["Accounting", "Finance", "Business", "Foundational", "Career-Relevant"],
    difficulty="Beginner",
    subdivision_category="Business/Finance"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Business Analytics & Data-Driven Decisions",
    goal_type="learning",
    goal_text="Master business analytics: data analysis, visualization, insights",
    timeframe=45,
    hours_per_day=2.0,
    description="Excel analytics, Tableau/Power BI, statistical analysis, business metrics",
    tags=["Business Analytics", "Data Analysis", "Business", "Career-Boost", "In-Demand"],
    difficulty="Intermediate",
    subdivision_category="Business/Finance"
))

TEMPLATES.append(GoalTemplate(
    name="Master Entrepreneurship Fundamentals",
    goal_type="learning",
    goal_text="Learn how to start and grow a business from scratch",
    timeframe=60,
    hours_per_day=2.0,
    description="Business ideas, validation, MVP, marketing, fundraising, growth strategies",
    tags=["Entrepreneurship", "Business", "Startup", "Founder Skills", "Innovation"],
    difficulty="Intermediate",
    subdivision_category="Business/Finance"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Supply Chain Management",
    goal_type="learning",
    goal_text="Master supply chain fundamentals: logistics, procurement, optimization",
    timeframe=45,
    hours_per_day=1.5,
    description="Supply chain concepts, logistics, inventory management, procurement",
    tags=["Supply Chain", "Operations", "Business", "Logistics", "Management"],
    difficulty="Intermediate",
    subdivision_category="Business/Finance"
))

TEMPLATES.append(GoalTemplate(
    name="Master Sales Skills & Techniques",
    goal_type="learning",
    goal_text="Learn modern sales techniques for B2B and B2C contexts",
    timeframe=30,
    hours_per_day=1.5,
    description="Sales psychology, prospecting, objection handling, closing, CRM",
    tags=["Sales", "Business", "Communication", "Career-Boost", "Revenue Generation"],
    difficulty="Beginner",
    subdivision_category="Business/Finance"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Product Management Fundamentals",
    goal_type="learning",
    goal_text="Master product management: discovery, roadmaps, metrics, launches",
    timeframe=60,
    hours_per_day=2.0,
    description="Product discovery, roadmapping, user research, metrics, stakeholder management",
    tags=["Product Management", "Business", "Tech", "Career-Boost", "In-Demand"],
    difficulty="Intermediate",
    subdivision_category="Business/Finance"
))


# ============================================================================
# LEARNING → MENTAL PRACTICES (8 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Master Vipassana Meditation",
    goal_type="learning",
    goal_text="Learn Vipassana meditation technique for deep insight",
    timeframe=60,
    hours_per_day=1.0,
    description="Body scanning, breath awareness, equanimity, sustained practice",
    tags=["Meditation", "Mindfulness", "Mental Practices", "Buddhist Practices", "Wellness"],
    difficulty="Intermediate",
    subdivision_category="Mental Practices"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Stoic Philosophy & Practices",
    goal_type="learning",
    goal_text="Master Stoic philosophy and daily practices for resilience",
    timeframe=30,
    hours_per_day=0.75,
    description="Stoic principles, negative visualization, journaling, dichotomy of control",
    tags=["Philosophy", "Stoicism", "Mental Practices", "Resilience", "Life Skills"],
    difficulty="Beginner",
    subdivision_category="Mental Practices"
))

TEMPLATES.append(GoalTemplate(
    name="Master Transcendental Meditation",
    goal_type="learning",
    goal_text="Learn and establish Transcendental Meditation practice",
    timeframe=21,
    hours_per_day=0.5,
    description="TM technique, mantra practice, twice-daily sessions, stress reduction",
    tags=["Meditation", "TM", "Mental Practices", "Stress Management", "Quick-Start"],
    difficulty="Beginner",
    subdivision_category="Mental Practices"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Lucid Dreaming Techniques",
    goal_type="learning",
    goal_text="Master lucid dreaming for conscious dream control",
    timeframe=60,
    hours_per_day=0.5,
    description="Reality checks, dream journaling, WILD/MILD techniques, dream control",
    tags=["Lucid Dreaming", "Mental Practices", "Consciousness", "Sleep", "Skill Building"],
    difficulty="Intermediate",
    subdivision_category="Mental Practices"
))

TEMPLATES.append(GoalTemplate(
    name="Master Memory Palace Technique",
    goal_type="learning",
    goal_text="Learn memory palace method for exceptional recall",
    timeframe=30,
    hours_per_day=1.0,
    description="Method of loci, memory encoding, spatial memory, practical applications",
    tags=["Memory", "Mental Practices", "Cognitive Skills", "Learning", "Mnemonics"],
    difficulty="Beginner",
    subdivision_category="Mental Practices"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Speed Reading Techniques",
    goal_type="learning",
    goal_text="Master speed reading to double or triple reading speed",
    timeframe=21,
    hours_per_day=1.0,
    description="Subvocalization elimination, peripheral vision, chunking, comprehension",
    tags=["Speed Reading", "Reading", "Mental Practices", "Productivity", "Quick-Start"],
    difficulty="Beginner",
    subdivision_category="Mental Practices"
))

TEMPLATES.append(GoalTemplate(
    name="Master Mind Mapping for Learning",
    goal_type="learning",
    goal_text="Learn mind mapping for enhanced learning and creativity",
    timeframe=14,
    hours_per_day=0.75,
    description="Mind map creation, tools, applications, learning optimization",
    tags=["Mind Mapping", "Learning", "Mental Practices", "Creativity", "Organization"],
    difficulty="Beginner",
    subdivision_category="Mental Practices"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Cognitive Behavioral Techniques",
    goal_type="learning",
    goal_text="Master CBT techniques for mental health and cognitive reframing",
    timeframe=45,
    hours_per_day=0.75,
    description="Thought records, cognitive distortions, behavioral experiments, reframing",
    tags=["CBT", "Mental Health", "Mental Practices", "Psychology", "Self-Improvement"],
    difficulty="Intermediate",
    subdivision_category="Mental Practices"
))


# ============================================================================
# LEARNING → PERSONALITY DEVELOPMENT (10 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Develop Leadership Presence",
    goal_type="learning",
    goal_text="Build authentic leadership presence and executive presence",
    timeframe=60,
    hours_per_day=1.0,
    description="Body language, voice, confidence, gravitas, authenticity, communication",
    tags=["Leadership", "Personality Development", "Soft Skills", "Executive Presence"],
    difficulty="Intermediate",
    subdivision_category="Personality Development"
))

TEMPLATES.append(GoalTemplate(
    name="Master Time Management & Productivity",
    goal_type="learning",
    goal_text="Learn advanced time management and productivity systems",
    timeframe=30,
    hours_per_day=1.0,
    description="GTD, time blocking, Pomodoro, energy management, productivity systems",
    tags=["Time Management", "Productivity", "Personality Development", "Life Skills"],
    difficulty="Beginner",
    subdivision_category="Personality Development"
))

TEMPLATES.append(GoalTemplate(
    name="Build Unwavering Discipline",
    goal_type="learning",
    goal_text="Develop iron discipline through progressive challenges",
    timeframe=90,
    hours_per_day=1.0,
    description="Habit stacking, delayed gratification, willpower training, consistency",
    tags=["Discipline", "Personality Development", "Habits", "Self-Control", "Mental Toughness"],
    difficulty="Advanced",
    subdivision_category="Personality Development"
))

TEMPLATES.append(GoalTemplate(
    name="Master Critical Thinking",
    goal_type="learning",
    goal_text="Develop critical thinking and logical reasoning skills",
    timeframe=45,
    hours_per_day=1.0,
    description="Logic, fallacies, argumentation, analysis, problem-solving frameworks",
    tags=["Critical Thinking", "Logic", "Personality Development", "Cognitive Skills"],
    difficulty="Intermediate",
    subdivision_category="Personality Development"
))

TEMPLATES.append(GoalTemplate(
    name="Develop Creative Problem-Solving",
    goal_type="learning",
    goal_text="Master creative thinking and innovative problem-solving",
    timeframe=30,
    hours_per_day=1.0,
    description="Lateral thinking, brainstorming, SCAMPER, design thinking, creativity exercises",
    tags=["Creativity", "Problem-Solving", "Personality Development", "Innovation"],
    difficulty="Beginner",
    subdivision_category="Personality Development"
))

TEMPLATES.append(GoalTemplate(
    name="Master Decision-Making Under Uncertainty",
    goal_type="learning",
    goal_text="Learn frameworks for making better decisions with incomplete information",
    timeframe=30,
    hours_per_day=1.0,
    description="Decision frameworks, probabilistic thinking, biases, risk assessment",
    tags=["Decision Making", "Personality Development", "Critical Thinking", "Life Skills"],
    difficulty="Intermediate",
    subdivision_category="Personality Development"
))

TEMPLATES.append(GoalTemplate(
    name="Build Authentic Charisma",
    goal_type="learning",
    goal_text="Develop genuine charisma and likability",
    timeframe=60,
    hours_per_day=1.0,
    description="Presence, storytelling, active listening, warmth, confidence, social skills",
    tags=["Charisma", "Personality Development", "Social Skills", "Communication"],
    difficulty="Intermediate",
    subdivision_category="Personality Development"
))

TEMPLATES.append(GoalTemplate(
    name="Master Strategic Thinking",
    goal_type="learning",
    goal_text="Develop strategic thinking for long-term planning and vision",
    timeframe=45,
    hours_per_day=1.0,
    description="Systems thinking, scenario planning, strategic frameworks, vision development",
    tags=["Strategic Thinking", "Personality Development", "Business", "Planning"],
    difficulty="Intermediate",
    subdivision_category="Personality Development"
))

TEMPLATES.append(GoalTemplate(
    name="Develop Cultural Intelligence",
    goal_type="learning",
    goal_text="Build cultural intelligence for global effectiveness",
    timeframe=45,
    hours_per_day=1.0,
    description="Cultural awareness, adaptation strategies, communication across cultures",
    tags=["Cultural Intelligence", "Personality Development", "Global Skills", "Communication"],
    difficulty="Intermediate",
    subdivision_category="Personality Development"
))

TEMPLATES.append(GoalTemplate(
    name="Master Influence & Persuasion",
    goal_type="learning",
    goal_text="Learn ethical influence and persuasion techniques",
    timeframe=30,
    hours_per_day=1.0,
    description="Cialdini principles, rhetoric, framing, storytelling, ethical persuasion",
    tags=["Influence", "Persuasion", "Personality Development", "Communication"],
    difficulty="Intermediate",
    subdivision_category="Personality Development"
))


# ============================================================================
# CAREER CATEGORY
# ============================================================================
# We'll keep the existing career templates and add subdivision_category


TEMPLATES.append(GoalTemplate(
    name="Land Remote AI Engineering Role (International)",
    goal_type="career",
    goal_text="Get hired as AI engineer at international company with remote work",
    timeframe=90,
    hours_per_day=3.0,
    description="Build AI skills, portfolio projects, target global companies, ace interviews",
    tags=["AI", "Remote-Friendly", "Career Switch", "International", "Engineering"],
    difficulty="Advanced",
    prerequisites="Python programming experience",
    subdivision_category="Tech Roles"
))

TEMPLATES.append(GoalTemplate(
    name="Transition from Teaching to EdTech Product Role",
    goal_type="career",
    goal_text="Transition from teaching to product management role at international EdTech company",
    timeframe=75,
    hours_per_day=2.5,
    description="EdTech industry knowledge, product skills, portfolio, international EdTech applications",
    tags=["EdTech", "Remote-Friendly", "Career Switch", "Teaching Background", "Product"],
    difficulty="Intermediate",
    prerequisites="Teaching experience",
    subdivision_category="Tech Roles"
))

TEMPLATES.append(GoalTemplate(
    name="Break Into Developer Relations (Remote)",
    goal_type="career",
    goal_text="Land remote Developer Relations role at tech company",
    timeframe=60,
    hours_per_day=2.5,
    description="Technical content, community building, DevRel portfolio, global opportunities",
    tags=["DevRel", "Remote-Friendly", "Content Creation", "Community", "Tech"],
    difficulty="Intermediate",
    prerequisites="Technical background and communication skills",
    subdivision_category="Tech Roles"
))

TEMPLATES.append(GoalTemplate(
    name="Get Hired as Remote Python Developer",
    goal_type="career",
    goal_text="Land remote Python developer position at international software company",
    timeframe=90,
    hours_per_day=3.0,
    description="Python mastery, portfolio projects, interview prep, international job applications",
    tags=["Python", "Remote-Friendly", "Software Engineering", "Career Switch"],
    difficulty="Intermediate",
    prerequisites="Python basics",
    subdivision_category="Tech Roles"
))

TEMPLATES.append(GoalTemplate(
    name="Become Data Analyst (Entry-Level)",
    goal_type="career",
    goal_text="Land entry-level data analyst role at tech or analytics company",
    timeframe=75,
    hours_per_day=2.5,
    description="SQL, Python, Excel, data visualization, portfolio, job applications",
    tags=["Data Analysis", "Career Switch", "Entry-Level", "Remote-Friendly"],
    difficulty="Intermediate",
    subdivision_category="Tech Roles"
))

TEMPLATES.append(GoalTemplate(
    name="Land UX/UI Designer Role (Remote)",
    goal_type="career",
    goal_text="Get hired as UX/UI designer at remote-friendly company",
    timeframe=90,
    hours_per_day=3.0,
    description="UI/UX skills, Figma mastery, portfolio projects, design challenges, applications",
    tags=["UI/UX", "Design", "Remote-Friendly", "Creative", "Career Switch"],
    difficulty="Intermediate",
    subdivision_category="Creative Roles"
))

TEMPLATES.append(GoalTemplate(
    name="Become Technical Writer (Remote)",
    goal_type="career",
    goal_text="Land technical writing role at international tech company",
    timeframe=60,
    hours_per_day=2.5,
    description="Technical writing skills, portfolio, API docs, applications to tech companies",
    tags=["Technical Writing", "Remote-Friendly", "Career Switch", "Documentation"],
    difficulty="Beginner",
    subdivision_category="Creative Roles"
))

TEMPLATES.append(GoalTemplate(
    name="Transition to Product Manager Role",
    goal_type="career",
    goal_text="Land product manager position at tech company",
    timeframe=90,
    hours_per_day=2.5,
    description="Product management skills, case studies, networking, PM interview prep",
    tags=["Product Management", "Career Switch", "Tech", "Remote-Friendly"],
    difficulty="Advanced",
    prerequisites="Some business or technical experience",
    subdivision_category="Business Roles"
))

TEMPLATES.append(GoalTemplate(
    name="Break Into Management Consulting",
    goal_type="career",
    goal_text="Land consulting role at top-tier firm (MBB or boutique)",
    timeframe=90,
    hours_per_day=3.0,
    description="Case interview mastery, business frameworks, networking, applications",
    tags=["Consulting", "Career Switch", "Business", "High-Earning"],
    difficulty="Advanced",
    prerequisites="Strong analytical and communication skills",
    subdivision_category="Business Roles"
))

TEMPLATES.append(GoalTemplate(
    name="Become Financial Analyst (Entry)",
    goal_type="career",
    goal_text="Land entry-level financial analyst role",
    timeframe=75,
    hours_per_day=2.5,
    description="Financial modeling, Excel mastery, certifications, networking, applications",
    tags=["Finance", "Career Switch", "Business", "Entry-Level"],
    difficulty="Intermediate",
    subdivision_category="Business Roles"
))


# ============================================================================
# PROJECT CATEGORY
# ============================================================================
# Keep existing project templates and add subdivision_category


TEMPLATES.append(GoalTemplate(
    name="Build SaaS MVP and Get First 10 Paying Users",
    goal_type="project",
    goal_text="Build SaaS minimum viable product and acquire first 10 paying customers",
    timeframe=60,
    hours_per_day=3.0,
    description="SaaS idea validation, MVP development, landing page, marketing, first customers",
    tags=["SaaS", "Startup", "Product Launch", "Income-Generating", "Entrepreneurship"],
    difficulty="Advanced",
    prerequisites="Programming skills or no-code proficiency",
    subdivision_category="Tech Development"
))

TEMPLATES.append(GoalTemplate(
    name="Launch E-Commerce Store (First $5K Revenue)",
    goal_type="project",
    goal_text="Launch e-commerce store and reach first $5,000 in revenue",
    timeframe=60,
    hours_per_day=2.5,
    description="Product sourcing, Shopify store, marketing, ads, first sales",
    tags=["E-Commerce", "Business", "Income-Generating", "Product Launch", "Entrepreneurship"],
    difficulty="Intermediate",
    subdivision_category="Income Generation"
))

TEMPLATES.append(GoalTemplate(
    name="Start Freelance Writing Business (First $1K)",
    goal_type="project",
    goal_text="Launch freelance writing business and earn first $1,000",
    timeframe=45,
    hours_per_day=2.0,
    description="Portfolio, Upwork/Fiverr profiles, pitching, first clients, revenue",
    tags=["Freelancing", "Writing", "Income-Generating", "Quick-Start", "Remote-Friendly"],
    difficulty="Beginner",
    subdivision_category="Freelancing"
))

TEMPLATES.append(GoalTemplate(
    name="Launch YouTube Channel (1K Subscribers)",
    goal_type="project",
    goal_text="Launch YouTube channel and grow to 1,000 subscribers",
    timeframe=90,
    hours_per_day=2.5,
    description="Niche selection, content creation, editing, SEO, consistency, growth strategies",
    tags=["YouTube", "Content Creation", "Video", "Income-Generating", "Creator Economy"],
    difficulty="Intermediate",
    subdivision_category="Content Creation"
))

TEMPLATES.append(GoalTemplate(
    name="Build AI-Powered Web App",
    goal_type="project",
    goal_text="Create AI-powered web application using modern tech stack",
    timeframe=45,
    hours_per_day=3.0,
    description="React, FastAPI, LangChain/OpenAI API, deployment, user-ready product",
    tags=["AI", "Web Development", "Full-Stack", "Portfolio-Building", "Modern Tech"],
    difficulty="Advanced",
    prerequisites="Web development experience",
    subdivision_category="Tech Development"
))

TEMPLATES.append(GoalTemplate(
    name="Create and Sell Online Course (First $500)",
    goal_type="project",
    goal_text="Create online course and earn first $500 in revenue",
    timeframe=60,
    hours_per_day=2.5,
    description="Course creation, Teachable/Gumroad, marketing, first sales",
    tags=["Online Course", "Teaching", "Income-Generating", "Digital Products", "Creator Economy"],
    difficulty="Intermediate",
    subdivision_category="Tutoring/Teaching"
))

TEMPLATES.append(GoalTemplate(
    name="Launch Premium Newsletter (100 Subscribers)",
    goal_type="project",
    goal_text="Start premium newsletter and grow to 100 paying subscribers",
    timeframe=90,
    hours_per_day=2.0,
    description="Niche selection, Substack setup, content strategy, growth, monetization",
    tags=["Newsletter", "Content Creation", "Writing", "Income-Generating", "Creator Economy"],
    difficulty="Intermediate",
    subdivision_category="Content Creation"
))

TEMPLATES.append(GoalTemplate(
    name="Build Chrome Extension with 1K Users",
    goal_type="project",
    goal_text="Create useful Chrome extension and reach 1,000+ users",
    timeframe=45,
    hours_per_day=2.5,
    description="JavaScript, Chrome API, development, Chrome Store launch, growth",
    tags=["Chrome Extension", "JavaScript", "Product Launch", "Portfolio-Building"],
    difficulty="Intermediate",
    prerequisites="JavaScript knowledge",
    subdivision_category="Tech Development"
))

TEMPLATES.append(GoalTemplate(
    name="Start Podcast (20 Episodes Published)",
    goal_type="project",
    goal_text="Launch podcast and publish first 20 quality episodes",
    timeframe=60,
    hours_per_day=2.0,
    description="Format development, recording setup, editing, publishing, guest outreach",
    tags=["Podcast", "Content Creation", "Audio", "Creator Economy", "Storytelling"],
    difficulty="Beginner",
    subdivision_category="Content Creation"
))

TEMPLATES.append(GoalTemplate(
    name="Develop Mobile App & Launch on Stores",
    goal_type="project",
    goal_text="Build mobile app and launch on App Store and Play Store",
    timeframe=60,
    hours_per_day=3.0,
    description="Flutter/React Native, development, testing, App/Play Store submission",
    tags=["Mobile Development", "Product Launch", "Portfolio-Building", "App Development"],
    difficulty="Advanced",
    prerequisites="Programming experience",
    subdivision_category="Tech Development"
))

TEMPLATES.append(GoalTemplate(
    name="Create Notion Templates Business (First $200)",
    goal_type="project",
    goal_text="Create and sell premium Notion templates earning first $200",
    timeframe=21,
    hours_per_day=1.5,
    description="Template creation, Gumroad setup, marketing, first sales",
    tags=["Notion", "Digital Products", "Income-Generating", "Quick-Start", "Creator Economy"],
    difficulty="Beginner",
    prerequisites="Notion knowledge",
    subdivision_category="Digital Products"
))

TEMPLATES.append(GoalTemplate(
    name="Start Tutoring Business Online (First 10 Students)",
    goal_type="project",
    goal_text="Launch online tutoring business and acquire first 10 students",
    timeframe=30,
    hours_per_day=2.0,
    description="Subject specialization, platform setup, marketing, first clients",
    tags=["Tutoring", "Teaching", "Income-Generating", "Remote-Friendly", "Education"],
    difficulty="Beginner",
    subdivision_category="Tutoring/Teaching"
))


# ============================================================================
# FREELANCE & BUSINESS CATEGORY
# ============================================================================
# Subdivisions: Platform-Based, Consulting, Digital Products, 
#               SaaS & Products, Passive Income


# ============================================================================
# FREELANCE → PLATFORM-BASED (10 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="First 5 Fiverr Clients in 30 Days",
    goal_type="freelance",
    goal_text="Get first 5 clients on Fiverr and earn first reviews",
    timeframe=30,
    hours_per_day=2.0,
    description="Profile optimization, gig creation, international client targeting, first reviews",
    tags=["Fiverr", "Beginner-Friendly", "Income-Generating", "Quick-Start"],
    difficulty="Beginner",
    subdivision_category="Platform-Based"
))

TEMPLATES.append(GoalTemplate(
    name="Earn $1000/Month on Upwork (International Clients)",
    goal_type="freelance",
    goal_text="Build Upwork freelance business earning $1000/month from international clients",
    timeframe=60,
    hours_per_day=3.0,
    description="Profile mastery, proposal strategy, client acquisition, upselling",
    tags=["Upwork", "Income-Generating", "Remote-Friendly", "International"],
    difficulty="Intermediate",
    prerequisites="Marketable skill (writing, design, development, etc.)",
    subdivision_category="Platform-Based"
))

TEMPLATES.append(GoalTemplate(
    name="Get Accepted to Toptal (Top 3%)",
    goal_type="freelance",
    goal_text="Pass Toptal screening and join elite freelance platform",
    timeframe=45,
    hours_per_day=3.0,
    description="Skills assessment prep, portfolio polishing, screening process",
    tags=["Toptal", "Elite Platform", "High-Income", "Remote-Friendly"],
    difficulty="Advanced",
    prerequisites="Expert-level skills in development/design/finance",
    subdivision_category="Platform-Based"
))

TEMPLATES.append(GoalTemplate(
    name="Build $500/Month Online Tutoring Business",
    goal_type="freelance",
    goal_text="Create online tutoring business earning $500/month from international students",
    timeframe=30,
    hours_per_day=2.0,
    description="Platforms (Preply, iTalki), marketing, student acquisition, scaling",
    tags=["Tutoring", "Income-Generating", "Remote-Friendly", "Teaching Background"],
    difficulty="Beginner",
    prerequisites="Teaching/tutoring experience",
    subdivision_category="Platform-Based"
))

TEMPLATES.append(GoalTemplate(
    name="Start Freelance Writing on Medium (First $100)",
    goal_type="freelance",
    goal_text="Build Medium writing presence and earn first $100 from articles",
    timeframe=30,
    hours_per_day=1.5,
    description="Article writing, Medium Partner Program, SEO, audience building",
    tags=["Writing", "Medium", "Content Creation", "Income-Generating", "Beginner-Friendly"],
    difficulty="Beginner",
    subdivision_category="Platform-Based"
))

TEMPLATES.append(GoalTemplate(
    name="Launch Freelance Design Business on 99designs",
    goal_type="freelance",
    goal_text="Start freelance design business on 99designs and win first 5 contests",
    timeframe=45,
    hours_per_day=2.5,
    description="Portfolio building, contest participation, client communication, winning strategies",
    tags=["Design", "99designs", "Freelancing", "Income-Generating", "Creative"],
    difficulty="Intermediate",
    prerequisites="Design skills (graphic, logo, web design)",
    subdivision_category="Platform-Based"
))

TEMPLATES.append(GoalTemplate(
    name="Build Freelance Translation Business (First $500)",
    goal_type="freelance",
    goal_text="Start freelance translation business and earn first $500",
    timeframe=30,
    hours_per_day=2.0,
    description="Platform setup, language pair specialization, client acquisition, quality standards",
    tags=["Translation", "Freelancing", "Language Skills", "Income-Generating", "Remote-Friendly"],
    difficulty="Beginner",
    prerequisites="Bilingual or multilingual proficiency",
    subdivision_category="Platform-Based"
))

TEMPLATES.append(GoalTemplate(
    name="Start Virtual Assistant Business (First 3 Clients)",
    goal_type="freelance",
    goal_text="Launch virtual assistant business and acquire first 3 clients",
    timeframe=21,
    hours_per_day=2.0,
    description="Service packages, client outreach, task management, client retention",
    tags=["Virtual Assistant", "Freelancing", "Remote-Friendly", "Beginner-Friendly", "Quick-Start"],
    difficulty="Beginner",
    subdivision_category="Platform-Based"
))

TEMPLATES.append(GoalTemplate(
    name="Build Freelance Social Media Management Business",
    goal_type="freelance",
    goal_text="Start social media management freelance business with first 3 clients",
    timeframe=30,
    hours_per_day=2.5,
    description="Service packages, content creation, analytics, client acquisition",
    tags=["Social Media", "Freelancing", "Marketing", "Income-Generating", "Remote-Friendly"],
    difficulty="Beginner",
    subdivision_category="Platform-Based"
))

TEMPLATES.append(GoalTemplate(
    name="Start Freelance Bookkeeping Business",
    goal_type="freelance",
    goal_text="Launch freelance bookkeeping business and acquire first 5 clients",
    timeframe=45,
    hours_per_day=2.0,
    description="QuickBooks/Xero certification, client acquisition, service packages, compliance",
    tags=["Bookkeeping", "Freelancing", "Finance", "Remote-Friendly", "Income-Generating"],
    difficulty="Intermediate",
    prerequisites="Accounting/bookkeeping knowledge",
    subdivision_category="Platform-Based"
))


# ============================================================================
# FREELANCE → CONSULTING (8 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Launch AI Consulting Practice",
    goal_type="freelance",
    goal_text="Start AI consulting business and land first 3 clients",
    timeframe=45,
    hours_per_day=2.5,
    description="Positioning, pricing, first 3 clients, service packages",
    tags=["AI", "Consulting", "Income-Generating", "High-Value"],
    difficulty="Advanced",
    prerequisites="AI/ML expertise",
    subdivision_category="Consulting"
))

TEMPLATES.append(GoalTemplate(
    name="Start Business Strategy Consulting Practice",
    goal_type="freelance",
    goal_text="Launch business strategy consulting and acquire first 3 clients",
    timeframe=60,
    hours_per_day=2.5,
    description="Consulting frameworks, client acquisition, proposal writing, service packages",
    tags=["Consulting", "Business Strategy", "High-Value", "Income-Generating"],
    difficulty="Advanced",
    prerequisites="Business experience or MBA",
    subdivision_category="Consulting"
))

TEMPLATES.append(GoalTemplate(
    name="Launch Marketing Consulting Business",
    goal_type="freelance",
    goal_text="Start marketing consulting practice and land first 3 clients",
    timeframe=45,
    hours_per_day=2.5,
    description="Marketing strategy, client acquisition, service packages, case studies",
    tags=["Marketing", "Consulting", "Income-Generating", "Business"],
    difficulty="Intermediate",
    prerequisites="Marketing experience",
    subdivision_category="Consulting"
))

TEMPLATES.append(GoalTemplate(
    name="Start HR Consulting Business",
    goal_type="freelance",
    goal_text="Launch HR consulting practice and acquire first 3 clients",
    timeframe=45,
    hours_per_day=2.0,
    description="HR services, client outreach, compliance knowledge, service packages",
    tags=["HR", "Consulting", "Business", "Income-Generating", "Remote-Friendly"],
    difficulty="Intermediate",
    prerequisites="HR experience or certification",
    subdivision_category="Consulting"
))

TEMPLATES.append(GoalTemplate(
    name="Launch Financial Planning Consulting",
    goal_type="freelance",
    goal_text="Start financial planning consulting and acquire first 5 clients",
    timeframe=60,
    hours_per_day=2.5,
    description="Certification prep, client acquisition, financial planning services, compliance",
    tags=["Finance", "Consulting", "Financial Planning", "High-Value", "Income-Generating"],
    difficulty="Advanced",
    prerequisites="Finance background, certification preferred",
    subdivision_category="Consulting"
))

TEMPLATES.append(GoalTemplate(
    name="Start Web Development Consulting",
    goal_type="freelance",
    goal_text="Launch web development consulting and land first 3 clients",
    timeframe=30,
    hours_per_day=2.5,
    description="Technical consulting, client acquisition, project scoping, proposals",
    tags=["Web Development", "Consulting", "Tech", "Income-Generating", "Remote-Friendly"],
    difficulty="Intermediate",
    prerequisites="Web development experience",
    subdivision_category="Consulting"
))

TEMPLATES.append(GoalTemplate(
    name="Launch SEO Consulting Business",
    goal_type="freelance",
    goal_text="Start SEO consulting practice and acquire first 5 clients",
    timeframe=30,
    hours_per_day=2.0,
    description="SEO audits, client acquisition, service packages, reporting",
    tags=["SEO", "Consulting", "Marketing", "Income-Generating", "Remote-Friendly"],
    difficulty="Intermediate",
    prerequisites="SEO knowledge and experience",
    subdivision_category="Consulting"
))

TEMPLATES.append(GoalTemplate(
    name="Start Data Analytics Consulting",
    goal_type="freelance",
    goal_text="Launch data analytics consulting and land first 3 clients",
    timeframe=45,
    hours_per_day=2.5,
    description="Analytics services, client acquisition, dashboard creation, insights delivery",
    tags=["Data Analytics", "Consulting", "Tech", "Income-Generating", "High-Value"],
    difficulty="Advanced",
    prerequisites="Data analytics expertise",
    subdivision_category="Consulting"
))


# ============================================================================
# FREELANCE → DIGITAL PRODUCTS (6 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Earn First $500 from Digital Products",
    goal_type="freelance",
    goal_text="Create and sell digital products earning first $500 in revenue",
    timeframe=30,
    hours_per_day=2.0,
    description="Create templates/courses, market on Gumroad/Etsy, first sales",
    tags=["Digital Products", "Income-Generating", "Passive Income", "Beginner-Friendly"],
    difficulty="Beginner",
    subdivision_category="Digital Products"
))

TEMPLATES.append(GoalTemplate(
    name="Create & Sell Notion Templates (First $200)",
    goal_type="freelance",
    goal_text="Create and sell premium Notion templates earning first $200",
    timeframe=21,
    hours_per_day=1.5,
    description="Template creation, Gumroad setup, marketing, first sales",
    tags=["Notion", "Digital Products", "Income-Generating", "Quick-Start"],
    difficulty="Beginner",
    prerequisites="Notion knowledge",
    subdivision_category="Digital Products"
))

TEMPLATES.append(GoalTemplate(
    name="Launch Canva Template Store (First $100)",
    goal_type="freelance",
    goal_text="Create and sell Canva templates earning first $100",
    timeframe=21,
    hours_per_day=1.5,
    description="Template design, Canva marketplace, marketing, first sales",
    tags=["Canva", "Digital Products", "Design", "Income-Generating", "Beginner-Friendly"],
    difficulty="Beginner",
    subdivision_category="Digital Products"
))

TEMPLATES.append(GoalTemplate(
    name="Create & Sell Stock Photos (First $200)",
    goal_type="freelance",
    goal_text="Build stock photography portfolio and earn first $200",
    timeframe=30,
    hours_per_day=2.0,
    description="Photo shooting, editing, Shutterstock/Adobe Stock, keyword optimization",
    tags=["Photography", "Stock Photos", "Digital Products", "Passive Income", "Creative"],
    difficulty="Beginner",
    prerequisites="Photography skills",
    subdivision_category="Digital Products"
))

TEMPLATES.append(GoalTemplate(
    name="Launch Digital Art Prints Business",
    goal_type="freelance",
    goal_text="Create and sell digital art prints earning first $300",
    timeframe=30,
    hours_per_day=2.0,
    description="Art creation, Etsy/Redbubble setup, marketing, first sales",
    tags=["Art", "Digital Products", "Creative", "Income-Generating", "Passive Income"],
    difficulty="Beginner",
    prerequisites="Digital art skills",
    subdivision_category="Digital Products"
))

TEMPLATES.append(GoalTemplate(
    name="Create & Sell Fonts/Typefaces",
    goal_type="freelance",
    goal_text="Design and sell fonts earning first $200",
    timeframe=45,
    hours_per_day=2.0,
    description="Font design, MyFonts/Creative Market, licensing, marketing",
    tags=["Typography", "Fonts", "Digital Products", "Design", "Income-Generating"],
    difficulty="Intermediate",
    prerequisites="Typography/design skills",
    subdivision_category="Digital Products"
))


# ============================================================================
# FREELANCE → SAAS & PRODUCTS (6 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Launch SaaS Product MVP",
    goal_type="freelance",
    goal_text="Build and launch SaaS product MVP with first 10 paying customers",
    timeframe=90,
    hours_per_day=3.0,
    description="Idea validation, MVP development, beta launch, first customers",
    tags=["SaaS", "Product Launch", "Income-Generating", "Entrepreneurship"],
    difficulty="Advanced",
    prerequisites="Technical skills or no-code expertise",
    subdivision_category="SaaS & Products"
))

TEMPLATES.append(GoalTemplate(
    name="Build & Launch API Service",
    goal_type="freelance",
    goal_text="Build API service and acquire first 10 paying customers",
    timeframe=45,
    hours_per_day=2.5,
    description="API development, documentation, monetization, first customers",
    tags=["API", "Income-Generating", "Developer Tools"],
    difficulty="Advanced",
    prerequisites="Backend development experience",
    subdivision_category="SaaS & Products"
))

TEMPLATES.append(GoalTemplate(
    name="Launch No-Code SaaS Product",
    goal_type="freelance",
    goal_text="Build and launch no-code SaaS product with first 5 paying customers",
    timeframe=60,
    hours_per_day=2.5,
    description="Bubble/Webflow development, idea validation, marketing, first customers",
    tags=["SaaS", "No-Code", "Product Launch", "Income-Generating", "Beginner-Friendly"],
    difficulty="Intermediate",
    prerequisites="No-code platform knowledge",
    subdivision_category="SaaS & Products"
))

TEMPLATES.append(GoalTemplate(
    name="Create & Launch Chrome Extension Business",
    goal_type="freelance",
    goal_text="Build Chrome extension and monetize with first 100 paying users",
    timeframe=45,
    hours_per_day=2.5,
    description="Extension development, Chrome Store launch, monetization, marketing",
    tags=["Chrome Extension", "Product Launch", "Income-Generating", "Tech"],
    difficulty="Intermediate",
    prerequisites="JavaScript knowledge",
    subdivision_category="SaaS & Products"
))

TEMPLATES.append(GoalTemplate(
    name="Launch WordPress Plugin Business",
    goal_type="freelance",
    goal_text="Create and sell WordPress plugin with first 50 paying customers",
    timeframe=60,
    hours_per_day=2.5,
    description="Plugin development, WordPress marketplace, marketing, support setup",
    tags=["WordPress", "Plugin", "Product Launch", "Income-Generating", "Tech"],
    difficulty="Intermediate",
    prerequisites="PHP/WordPress development",
    subdivision_category="SaaS & Products"
))

TEMPLATES.append(GoalTemplate(
    name="Build & Launch Mobile App (Freemium Model)",
    goal_type="freelance",
    goal_text="Create mobile app with freemium model and acquire first 100 paying users",
    timeframe=60,
    hours_per_day=3.0,
    description="App development, App/Play Store launch, freemium strategy, monetization",
    tags=["Mobile App", "Product Launch", "Income-Generating", "Freemium"],
    difficulty="Advanced",
    prerequisites="Mobile development experience",
    subdivision_category="SaaS & Products"
))


# ============================================================================
# FREELANCE → PASSIVE INCOME (5 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Build Passive Income Stream ($200/Month)",
    goal_type="freelance",
    goal_text="Create passive income stream generating $200/month",
    timeframe=60,
    hours_per_day=2.0,
    description="Choose model (affiliate, digital products, API), build, monetize",
    tags=["Passive Income", "Income-Generating", "Automation"],
    difficulty="Intermediate",
    prerequisites="Marketing or technical skills",
    subdivision_category="Passive Income"
))

TEMPLATES.append(GoalTemplate(
    name="Start Affiliate Marketing Business (First $300)",
    goal_type="freelance",
    goal_text="Build affiliate marketing business earning first $300/month",
    timeframe=45,
    hours_per_day=2.0,
    description="Niche selection, content creation, affiliate programs, SEO, monetization",
    tags=["Affiliate Marketing", "Passive Income", "Income-Generating", "Marketing"],
    difficulty="Beginner",
    subdivision_category="Passive Income"
))

TEMPLATES.append(GoalTemplate(
    name="Launch Print-on-Demand Business (First $200)",
    goal_type="freelance",
    goal_text="Start print-on-demand business and earn first $200",
    timeframe=30,
    hours_per_day=1.5,
    description="Design creation, Redbubble/Printful setup, marketing, first sales",
    tags=["Print-on-Demand", "Passive Income", "Creative", "Income-Generating", "Beginner-Friendly"],
    difficulty="Beginner",
    subdivision_category="Passive Income"
))

TEMPLATES.append(GoalTemplate(
    name="Create YouTube Channel (Monetize First $100)",
    goal_type="freelance",
    goal_text="Build YouTube channel and earn first $100 from monetization",
    timeframe=90,
    hours_per_day=2.0,
    description="Content creation, SEO, consistency, monetization requirements, first revenue",
    tags=["YouTube", "Passive Income", "Content Creation", "Income-Generating"],
    difficulty="Intermediate",
    subdivision_category="Passive Income"
))

TEMPLATES.append(GoalTemplate(
    name="Build Blog with Affiliate Income (First $200)",
    goal_type="freelance",
    goal_text="Create blog and earn first $200 from affiliate marketing",
    timeframe=60,
    hours_per_day=2.0,
    description="Blog setup, content creation, SEO, affiliate programs, monetization",
    tags=["Blogging", "Affiliate Marketing", "Passive Income", "Content Creation", "Income-Generating"],
    difficulty="Beginner",
    subdivision_category="Passive Income"
))


# ============================================================================
# LEARNING → COOKING & NUTRITION (New subdivision - 4 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Master Meal Prep for Healthy Eating",
    goal_type="learning",
    goal_text="Learn meal prep strategies and cook healthy meals efficiently",
    timeframe=30,
    hours_per_day=1.5,
    description="Meal planning, batch cooking, nutrition basics, grocery shopping, food storage",
    tags=["Cooking", "Nutrition", "Health", "Meal Prep", "Life Skills"],
    difficulty="Beginner",
    subdivision_category="Cooking & Nutrition"
))

TEMPLATES.append(GoalTemplate(
    name="Learn Baking Fundamentals",
    goal_type="learning",
    goal_text="Master bread, pastries, and cake baking techniques",
    timeframe=45,
    hours_per_day=2.0,
    description="Bread making, pastries, cakes, cookies, baking science, techniques",
    tags=["Baking", "Cooking", "Life Skills", "Creative", "Beginner-Friendly"],
    difficulty="Beginner",
    subdivision_category="Cooking & Nutrition"
))

TEMPLATES.append(GoalTemplate(
    name="Plant-Based Cooking Mastery",
    goal_type="learning",
    goal_text="Learn to cook delicious and nutritious plant-based meals",
    timeframe=30,
    hours_per_day=1.0,
    description="Vegan recipes, nutrition, protein sources, flavor techniques, meal ideas",
    tags=["Cooking", "Nutrition", "Health", "Vegan", "Plant-Based"],
    difficulty="Beginner",
    subdivision_category="Cooking & Nutrition"
))

TEMPLATES.append(GoalTemplate(
    name="Master Nutrition Fundamentals",
    goal_type="learning",
    goal_text="Understand nutrition science and make informed food choices",
    timeframe=30,
    hours_per_day=1.0,
    description="Macronutrients, micronutrients, calorie tracking, meal planning, diet optimization",
    tags=["Nutrition", "Health", "Science", "Wellness", "Education"],
    difficulty="Beginner",
    subdivision_category="Cooking & Nutrition"
))


# ============================================================================
# LEARNING → HOME & LIFE MANAGEMENT (New subdivision - 4 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Master Home Organization & Decluttering",
    goal_type="learning",
    goal_text="Transform your home with organization systems and decluttering methods",
    timeframe=30,
    hours_per_day=1.5,
    description="KonMari method, organization systems, decluttering, minimalism, home efficiency",
    tags=["Organization", "Home", "Decluttering", "Life Skills", "Minimalism"],
    difficulty="Beginner",
    subdivision_category="Home & Life Management"
))

TEMPLATES.append(GoalTemplate(
    name="Basic Home Repairs & Maintenance",
    goal_type="learning",
    goal_text="Learn essential home repair skills and routine maintenance",
    timeframe=45,
    hours_per_day=2.0,
    description="Plumbing basics, electrical safety, wall repairs, tool usage, preventive maintenance",
    tags=["Home Repair", "DIY", "Life Skills", "Practical", "Hands-On"],
    difficulty="Beginner",
    subdivision_category="Home & Life Management"
))

TEMPLATES.append(GoalTemplate(
    name="Personal Budgeting & Financial Management",
    goal_type="learning",
    goal_text="Master personal budgeting and money management skills",
    timeframe=21,
    hours_per_day=1.0,
    description="Budget creation, expense tracking, saving strategies, debt management, financial goals",
    tags=["Finance", "Budgeting", "Life Skills", "Money Management", "Quick-Start"],
    difficulty="Beginner",
    subdivision_category="Home & Life Management"
))

TEMPLATES.append(GoalTemplate(
    name="Time Management for Busy Professionals",
    goal_type="learning",
    goal_text="Learn effective time management and productivity systems",
    timeframe=30,
    hours_per_day=1.0,
    description="Calendar management, prioritization, task management, work-life balance, efficiency",
    tags=["Time Management", "Productivity", "Life Skills", "Organization", "Professional"],
    difficulty="Beginner",
    subdivision_category="Home & Life Management"
))


# ============================================================================
# LEARNING → PARENTING & FAMILY SKILLS (New subdivision - 4 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Positive Parenting Fundamentals",
    goal_type="learning",
    goal_text="Learn positive parenting strategies and child development basics",
    timeframe=30,
    hours_per_day=1.0,
    description="Child development stages, positive discipline, communication, emotional regulation, family dynamics",
    tags=["Parenting", "Family", "Child Development", "Life Skills", "Relationships"],
    difficulty="Beginner",
    subdivision_category="Parenting & Family Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Effective Communication with Teens",
    goal_type="learning",
    goal_text="Build better communication and connection with teenage children",
    timeframe=30,
    hours_per_day=1.0,
    description="Teen psychology, active listening, conflict resolution, boundaries, trust building",
    tags=["Parenting", "Teens", "Communication", "Family", "Relationships"],
    difficulty="Intermediate",
    subdivision_category="Parenting & Family Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Quality Family Time Activities",
    goal_type="learning",
    goal_text="Create meaningful family experiences and strengthen bonds",
    timeframe=30,
    hours_per_day=1.0,
    description="Family activities, rituals, game nights, outdoor activities, tradition building",
    tags=["Family", "Parenting", "Relationships", "Quality Time", "Life Skills"],
    difficulty="Beginner",
    subdivision_category="Parenting & Family Skills"
))

TEMPLATES.append(GoalTemplate(
    name="Supporting Child's Learning at Home",
    goal_type="learning",
    goal_text="Help your child succeed academically with effective home support",
    timeframe=45,
    hours_per_day=1.0,
    description="Homework help, learning styles, motivation, study skills, educational resources",
    tags=["Parenting", "Education", "Child Development", "Learning", "Family"],
    difficulty="Beginner",
    subdivision_category="Parenting & Family Skills"
))


# ============================================================================
# CAREER → HEALTHCARE & EDUCATION CAREERS (New subdivision - 4 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Transition to Teaching Career",
    goal_type="career",
    goal_text="Successfully transition into a teaching role in K-12 or higher education",
    timeframe=90,
    hours_per_day=2.0,
    description="Teaching certification, curriculum design, classroom management, interview prep, first job",
    tags=["Teaching", "Education", "Career Switch", "Remote-Possible", "Fulfilling"],
    difficulty="Intermediate",
    subdivision_category="Healthcare & Education Careers"
))

TEMPLATES.append(GoalTemplate(
    name="Become School Counselor",
    goal_type="career",
    goal_text="Launch career as school counselor or educational advisor",
    timeframe=120,
    hours_per_day=2.0,
    description="Counseling certification, student psychology, college prep advising, mental health support",
    tags=["Counseling", "Education", "Career Switch", "Mental Health", "Fulfilling"],
    difficulty="Intermediate",
    subdivision_category="Healthcare & Education Careers"
))

TEMPLATES.append(GoalTemplate(
    name="Healthcare Administration Entry",
    goal_type="career",
    goal_text="Break into healthcare administration and management",
    timeframe=90,
    hours_per_day=2.0,
    description="Healthcare systems, administration, compliance, operations, management skills",
    tags=["Healthcare", "Administration", "Management", "Career Switch", "Stable"],
    difficulty="Intermediate",
    subdivision_category="Healthcare & Education Careers"
))

TEMPLATES.append(GoalTemplate(
    name="Online Tutoring Career Launch",
    goal_type="career",
    goal_text="Start successful online tutoring career with consistent clients",
    timeframe=60,
    hours_per_day=1.5,
    description="Platform selection, profile optimization, pricing, teaching methods, client acquisition",
    tags=["Tutoring", "Education", "Remote-Friendly", "Flexible", "Income-Generating"],
    difficulty="Beginner",
    subdivision_category="Healthcare & Education Careers"
))


# ============================================================================
# CAREER → TRADES & SERVICE CAREERS (New subdivision - 4 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Real Estate Agent Certification",
    goal_type="career",
    goal_text="Get real estate license and launch agent career",
    timeframe=90,
    hours_per_day=2.0,
    description="License exam prep, market knowledge, client acquisition, first transactions",
    tags=["Real Estate", "Sales", "License", "High-Earning", "Entrepreneurial"],
    difficulty="Intermediate",
    subdivision_category="Trades & Service Careers"
))

TEMPLATES.append(GoalTemplate(
    name="Insurance Sales Career Launch",
    goal_type="career",
    goal_text="Start career in insurance sales with established client base",
    timeframe=60,
    hours_per_day=2.0,
    description="Insurance products, sales techniques, licensing, client acquisition, relationship building",
    tags=["Insurance", "Sales", "Career Launch", "Income-Generating", "People-Oriented"],
    difficulty="Beginner",
    subdivision_category="Trades & Service Careers"
))

TEMPLATES.append(GoalTemplate(
    name="Skilled Trade Apprenticeship Entry",
    goal_type="career",
    goal_text="Enter skilled trade (plumbing, electrical, HVAC) apprenticeship",
    timeframe=90,
    hours_per_day=3.0,
    description="Trade selection, safety training, tool skills, apprenticeship application, hands-on learning",
    tags=["Skilled Trade", "Hands-On", "High-Demand", "Stable", "Career Launch"],
    difficulty="Beginner",
    subdivision_category="Trades & Service Careers"
))

TEMPLATES.append(GoalTemplate(
    name="Customer Success Manager Role",
    goal_type="career",
    goal_text="Land customer success or account management position",
    timeframe=60,
    hours_per_day=2.0,
    description="Customer success skills, CRM tools, communication, problem-solving, interview prep",
    tags=["Customer Success", "Service", "Remote-Friendly", "Tech-Adjacent", "People-Oriented"],
    difficulty="Intermediate",
    subdivision_category="Trades & Service Careers"
))


# ============================================================================
# FREELANCE → CRAFTS & HANDMADE BUSINESS (New subdivision - 4 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Launch Etsy Shop (First 20 Sales)",
    goal_type="freelance",
    goal_text="Create Etsy shop and make first 20 sales with handmade products",
    timeframe=60,
    hours_per_day=2.0,
    description="Product creation, photography, shop setup, SEO, pricing, customer service",
    tags=["Etsy", "Handmade", "Crafts", "Income-Generating", "Creative"],
    difficulty="Beginner",
    subdivision_category="Crafts & Handmade Business"
))

TEMPLATES.append(GoalTemplate(
    name="Jewelry Making Business (First $500)",
    goal_type="freelance",
    goal_text="Start handmade jewelry business and earn first $500",
    timeframe=60,
    hours_per_day=2.5,
    description="Jewelry techniques, materials sourcing, branding, online sales, marketing",
    tags=["Jewelry", "Handmade", "Crafts", "Income-Generating", "Creative"],
    difficulty="Beginner",
    subdivision_category="Crafts & Handmade Business"
))

TEMPLATES.append(GoalTemplate(
    name="Custom Artwork & Commissions",
    goal_type="freelance",
    goal_text="Build custom art commission business with steady clients",
    timeframe=60,
    hours_per_day=2.0,
    description="Portfolio building, pricing, commission workflow, client communication, art marketing",
    tags=["Art", "Commissions", "Custom Work", "Income-Generating", "Creative"],
    difficulty="Intermediate",
    subdivision_category="Crafts & Handmade Business"
))

TEMPLATES.append(GoalTemplate(
    name="Handmade Soap & Cosmetics Business",
    goal_type="freelance",
    goal_text="Create and sell handmade soaps and cosmetics online",
    timeframe=60,
    hours_per_day=2.0,
    description="Soap making, safety regulations, branding, packaging, online sales, marketing",
    tags=["Handmade", "Cosmetics", "Soap", "Income-Generating", "Creative"],
    difficulty="Beginner",
    subdivision_category="Crafts & Handmade Business"
))


# ============================================================================
# FREELANCE → E-COMMERCE & PHYSICAL PRODUCTS (New subdivision - 3 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Amazon FBA Business Launch",
    goal_type="freelance",
    goal_text="Launch Amazon FBA business with first profitable product",
    timeframe=90,
    hours_per_day=3.0,
    description="Product research, supplier sourcing, FBA setup, listing optimization, marketing",
    tags=["Amazon FBA", "E-Commerce", "Physical Products", "Income-Generating", "Scalable"],
    difficulty="Intermediate",
    subdivision_category="E-Commerce & Physical Products"
))

TEMPLATES.append(GoalTemplate(
    name="Local Service Business Launch",
    goal_type="freelance",
    goal_text="Start local service business (cleaning, landscaping, pet care)",
    timeframe=60,
    hours_per_day=2.5,
    description="Business setup, licensing, marketing, pricing, client acquisition, operations",
    tags=["Local Business", "Service", "Physical", "Income-Generating", "Entrepreneurial"],
    difficulty="Beginner",
    subdivision_category="E-Commerce & Physical Products"
))

TEMPLATES.append(GoalTemplate(
    name="Thrift Flipping Business",
    goal_type="freelance",
    goal_text="Build profitable thrift store flipping business online",
    timeframe=60,
    hours_per_day=2.0,
    description="Sourcing strategies, product photography, pricing, platform selection, shipping",
    tags=["Thrift Flipping", "Reselling", "E-Commerce", "Income-Generating", "Low-Cost Start"],
    difficulty="Beginner",
    subdivision_category="E-Commerce & Physical Products"
))


# ============================================================================
# PROJECT → CREATIVE PROJECTS (New subdivision - 4 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Complete Art Portfolio",
    goal_type="project",
    goal_text="Create comprehensive art portfolio showcasing 20+ finished pieces",
    timeframe=90,
    hours_per_day=2.0,
    description="Portfolio pieces, photography, presentation, online gallery, artist statement",
    tags=["Art", "Portfolio", "Creative", "Exhibition", "Career-Building"],
    difficulty="Intermediate",
    subdivision_category="Creative Projects"
))

TEMPLATES.append(GoalTemplate(
    name="Record Music Album/EP",
    goal_type="project",
    goal_text="Write, record, and release original music album or EP",
    timeframe=120,
    hours_per_day=2.5,
    description="Songwriting, recording, mixing, mastering, album art, distribution",
    tags=["Music", "Recording", "Creative", "Album", "Original Work"],
    difficulty="Intermediate",
    subdivision_category="Creative Projects"
))

TEMPLATES.append(GoalTemplate(
    name="Photography Book Project",
    goal_type="project",
    goal_text="Create and publish photography book or exhibition",
    timeframe=90,
    hours_per_day=2.0,
    description="Theme development, photo shoots, curation, editing, book design, publishing",
    tags=["Photography", "Book", "Creative", "Portfolio", "Publishing"],
    difficulty="Intermediate",
    subdivision_category="Creative Projects"
))

TEMPLATES.append(GoalTemplate(
    name="Short Film Production",
    goal_type="project",
    goal_text="Write, film, and edit short film from concept to completion",
    timeframe=90,
    hours_per_day=3.0,
    description="Screenwriting, production planning, filming, editing, sound design, distribution",
    tags=["Film", "Video", "Creative", "Storytelling", "Production"],
    difficulty="Advanced",
    subdivision_category="Creative Projects"
))


# ============================================================================
# PROJECT → HOME & LIFE PROJECTS (New subdivision - 3 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Home Renovation Project",
    goal_type="project",
    goal_text="Complete major home renovation (kitchen, bathroom, or room makeover)",
    timeframe=120,
    hours_per_day=3.0,
    description="Planning, budgeting, contractor management, design, DIY tasks, project completion",
    tags=["Home Improvement", "Renovation", "DIY", "Project", "Home"],
    difficulty="Intermediate",
    subdivision_category="Home & Life Projects"
))

TEMPLATES.append(GoalTemplate(
    name="Garden Transformation Project",
    goal_type="project",
    goal_text="Transform outdoor space into beautiful, functional garden",
    timeframe=90,
    hours_per_day=2.0,
    description="Garden design, plant selection, hardscaping, installation, maintenance planning",
    tags=["Gardening", "Outdoor", "Home", "Project", "Nature"],
    difficulty="Beginner",
    subdivision_category="Home & Life Projects"
))

TEMPLATES.append(GoalTemplate(
    name="Family History Documentation",
    goal_type="project",
    goal_text="Research and document complete family history for future generations",
    timeframe=90,
    hours_per_day=1.5,
    description="Genealogy research, interviews, photo collection, story writing, documentation",
    tags=["Family", "Genealogy", "History", "Legacy", "Documentation"],
    difficulty="Beginner",
    subdivision_category="Home & Life Projects"
))


# ============================================================================
# PERSONAL → GARDENING & PLANTS (New subdivision - 4 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Start Indoor Garden Collection",
    goal_type="personal",
    goal_text="Build thriving indoor garden with 15+ healthy houseplants",
    timeframe=60,
    hours_per_day=0.5,
    description="Plant selection, care routines, troubleshooting, propagation, indoor environment",
    tags=["Gardening", "Plants", "Indoor", "Hobby", "Wellness"],
    difficulty="Beginner",
    subdivision_category="Gardening & Plants"
))

TEMPLATES.append(GoalTemplate(
    name="Grow Vegetable Garden from Seed",
    goal_type="personal",
    goal_text="Successfully grow vegetables from seed to harvest",
    timeframe=120,
    hours_per_day=1.0,
    description="Seed starting, transplanting, garden maintenance, pest control, harvesting",
    tags=["Gardening", "Vegetables", "Outdoor", "Food", "Sustainable"],
    difficulty="Beginner",
    subdivision_category="Gardening & Plants"
))

TEMPLATES.append(GoalTemplate(
    name="Master Herb Gardening",
    goal_type="personal",
    goal_text="Grow and maintain kitchen herb garden year-round",
    timeframe=90,
    hours_per_day=0.5,
    description="Herb selection, growing conditions, harvesting, preservation, culinary use",
    tags=["Gardening", "Herbs", "Cooking", "Indoor/Outdoor", "Practical"],
    difficulty="Beginner",
    subdivision_category="Gardening & Plants"
))

TEMPLATES.append(GoalTemplate(
    name="Urban Gardening Mastery",
    goal_type="personal",
    goal_text="Create productive urban garden in limited space",
    timeframe=90,
    hours_per_day=1.0,
    description="Container gardening, vertical gardening, balcony setup, space optimization, urban techniques",
    tags=["Gardening", "Urban", "Small Space", "Sustainable", "Creative"],
    difficulty="Intermediate",
    subdivision_category="Gardening & Plants"
))


# ============================================================================
# PERSONAL → PUZZLES & GAMES (New subdivision - 4 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Chess Rating 1500 Achievement",
    goal_type="personal",
    goal_text="Reach 1500 chess rating through systematic study and practice",
    timeframe=180,
    hours_per_day=1.0,
    description="Opening repertoire, tactics training, endgame study, game analysis, online play",
    tags=["Chess", "Strategy", "Games", "Mental", "Skill Building"],
    difficulty="Intermediate",
    subdivision_category="Puzzles & Games"
))

TEMPLATES.append(GoalTemplate(
    name="Master Sudoku Techniques",
    goal_type="personal",
    goal_text="Solve expert-level Sudoku puzzles consistently",
    timeframe=60,
    hours_per_day=0.5,
    description="Advanced techniques, pattern recognition, speed solving, puzzle types",
    tags=["Sudoku", "Puzzles", "Logic", "Mental", "Quick-Start"],
    difficulty="Beginner",
    subdivision_category="Puzzles & Games"
))

TEMPLATES.append(GoalTemplate(
    name="Complete Jigsaw Puzzle Collection",
    goal_type="personal",
    goal_text="Assemble 10 challenging jigsaw puzzles (1000+ pieces)",
    timeframe=90,
    hours_per_day=1.0,
    description="Sorting strategies, edge techniques, pattern recognition, mindfulness practice",
    tags=["Puzzles", "Jigsaw", "Relaxation", "Mindfulness", "Hobby"],
    difficulty="Beginner",
    subdivision_category="Puzzles & Games"
))

TEMPLATES.append(GoalTemplate(
    name="Board Game Mastery Challenge",
    goal_type="personal",
    goal_text="Master 5 complex strategy board games",
    timeframe=120,
    hours_per_day=1.5,
    description="Game rules, strategies, regular play sessions, game group building, tournaments",
    tags=["Board Games", "Strategy", "Social", "Games", "Hobby"],
    difficulty="Intermediate",
    subdivision_category="Puzzles & Games"
))


# ============================================================================
# PERSONAL → COOKING & BAKING (HOBBY) (New subdivision - 4 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Master Sourdough Bread Baking",
    goal_type="personal",
    goal_text="Consistently bake perfect sourdough bread from scratch",
    timeframe=60,
    hours_per_day=1.5,
    description="Starter maintenance, fermentation, shaping, baking techniques, troubleshooting",
    tags=["Baking", "Sourdough", "Bread", "Hobby", "Creative"],
    difficulty="Intermediate",
    subdivision_category="Cooking & Baking"
))

TEMPLATES.append(GoalTemplate(
    name="Advanced Pastry Techniques",
    goal_type="personal",
    goal_text="Master advanced pastry techniques (croissants, puff pastry, éclairs)",
    timeframe=90,
    hours_per_day=2.0,
    description="Laminated dough, pastry cream, precise techniques, temperature control, presentation",
    tags=["Baking", "Pastry", "Advanced", "Hobby", "Creative"],
    difficulty="Advanced",
    subdivision_category="Cooking & Baking"
))

TEMPLATES.append(GoalTemplate(
    name="Explore World Cuisine (10 Countries)",
    goal_type="personal",
    goal_text="Master signature dishes from 10 different cuisines",
    timeframe=90,
    hours_per_day=1.5,
    description="Recipe research, ingredient sourcing, technique learning, cultural context, flavor profiles",
    tags=["Cooking", "World Cuisine", "Cultural", "Hobby", "Creative"],
    difficulty="Intermediate",
    subdivision_category="Cooking & Baking"
))

TEMPLATES.append(GoalTemplate(
    name="Fermentation Mastery",
    goal_type="personal",
    goal_text="Master fermentation techniques (kimchi, kombucha, sauerkraut, yogurt)",
    timeframe=60,
    hours_per_day=1.0,
    description="Fermentation science, safety, recipes, flavor development, preservation",
    tags=["Fermentation", "Cooking", "Health", "Hobby", "Science"],
    difficulty="Intermediate",
    subdivision_category="Cooking & Baking"
))


# ============================================================================
# PERSONAL → COMMUNITY & VOLUNTEERING (New subdivision - 4 templates)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Regular Volunteering Commitment",
    goal_type="personal",
    goal_text="Establish consistent volunteering habit at local organization",
    timeframe=90,
    hours_per_day=1.0,
    description="Organization research, application, training, regular commitment, impact measurement",
    tags=["Volunteering", "Community", "Giving Back", "Social Impact", "Fulfillment"],
    difficulty="Beginner",
    subdivision_category="Community & Volunteering"
))

TEMPLATES.append(GoalTemplate(
    name="Community Project Leadership",
    goal_type="personal",
    goal_text="Lead community improvement project from conception to completion",
    timeframe=120,
    hours_per_day=2.0,
    description="Project planning, team building, fundraising, execution, community engagement",
    tags=["Community", "Leadership", "Project", "Social Impact", "Activism"],
    difficulty="Intermediate",
    subdivision_category="Community & Volunteering"
))

TEMPLATES.append(GoalTemplate(
    name="Local Activism Campaign",
    goal_type="personal",
    goal_text="Organize and run local advocacy campaign for community issue",
    timeframe=90,
    hours_per_day=2.0,
    description="Issue research, coalition building, strategy, advocacy, community organizing",
    tags=["Activism", "Community", "Advocacy", "Social Change", "Leadership"],
    difficulty="Intermediate",
    subdivision_category="Community & Volunteering"
))

TEMPLATES.append(GoalTemplate(
    name="Mentor Youth Program",
    goal_type="personal",
    goal_text="Become mentor in youth program and support 1-3 mentees",
    timeframe=180,
    hours_per_day=1.0,
    description="Mentor training, relationship building, guidance, support, long-term commitment",
    tags=["Mentoring", "Youth", "Community", "Giving Back", "Relationships"],
    difficulty="Beginner",
    subdivision_category="Community & Volunteering"
))


# ============================================================================
# TEMPLATE UTILITIES
# ============================================================================

def get_all_templates() -> List[GoalTemplate]:
    """Get all available templates"""
    return TEMPLATES


def get_templates_by_type(goal_type: str) -> List[GoalTemplate]:
    """Get templates filtered by goal type"""
    return [t for t in TEMPLATES if t.goal_type == goal_type]


def get_templates_by_subdivision(subdivision: str) -> List[GoalTemplate]:
    """Get templates filtered by subdivision category"""
    return [t for t in TEMPLATES if t.subdivision_category == subdivision]


def get_templates_by_tag(tag: str) -> List[GoalTemplate]:
    """Get templates filtered by tag"""
    return [t for t in TEMPLATES if tag in t.tags]


def search_templates(query: str) -> List[GoalTemplate]:
    """Search templates by name, description, or tags"""
    query_lower = query.lower()
    results = []
    for template in TEMPLATES:
        if (query_lower in template.name.lower() or
            query_lower in template.description.lower() or
            query_lower in template.goal_text.lower() or
            any(query_lower in tag.lower() for tag in template.tags)):
            results.append(template)
    return results


def get_template_by_name(name: str) -> GoalTemplate:
    """Get a specific template by name"""
    for template in TEMPLATES:
        if template.name == name:
            return template
    return None


def get_all_tags() -> List[str]:
    """Get all unique tags from templates"""
    tags = set()
    for template in TEMPLATES:
        tags.update(template.tags)
    return sorted(list(tags))


def get_all_subdivisions() -> List[str]:
    """Get all unique subdivision categories"""
    subdivisions = set()
    for template in TEMPLATES:
        if template.subdivision_category:
            subdivisions.add(template.subdivision_category)
    return sorted(list(subdivisions))


def get_templates_by_timeframe(min_days: int = None, max_days: int = None) -> List[GoalTemplate]:
    """Get templates filtered by timeframe range"""
    results = []
    for template in TEMPLATES:
        if min_days and template.timeframe < min_days:
            continue
        if max_days and template.timeframe > max_days:
            continue
        results.append(template)
    return results


def get_templates_by_intensity(min_hours: float = None, max_hours: float = None) -> List[GoalTemplate]:
    """Get templates filtered by hours per day"""
    results = []
    for template in TEMPLATES:
        if min_hours and template.hours_per_day < min_hours:
            continue
        if max_hours and template.hours_per_day > max_hours:
            continue
        results.append(template)
    return results


def get_templates_by_difficulty(difficulty: str) -> List[GoalTemplate]:
    """Get templates filtered by difficulty level"""
    return [t for t in TEMPLATES if t.difficulty == difficulty]


# ============================================================================
# SUMMARY STATISTICS
# ============================================================================

def get_template_statistics() -> Dict:
    """Get statistics about the template library"""
    stats = {
        'total_templates': len(TEMPLATES),
        'by_type': {},
        'by_subdivision': {},
        'by_difficulty': {},
        'avg_timeframe_days': sum(t.timeframe for t in TEMPLATES) / len(TEMPLATES),
        'avg_hours_per_day': sum(t.hours_per_day for t in TEMPLATES) / len(TEMPLATES),
    }
    
    # Count by type
    for template in TEMPLATES:
        goal_type = template.goal_type
        stats['by_type'][goal_type] = stats['by_type'].get(goal_type, 0) + 1
        
        # Count by subdivision
        if template.subdivision_category:
            sub = template.subdivision_category
            stats['by_subdivision'][sub] = stats['by_subdivision'].get(sub, 0) + 1
        
        # Count by difficulty
        diff = template.difficulty
        stats['by_difficulty'][diff] = stats['by_difficulty'].get(diff, 0) + 1
    
    return stats


# Print summary when module is run directly
if __name__ == "__main__":
    stats = get_template_statistics()
    print("=" * 60)
    print("GOAL TEMPLATES LIBRARY - SUMMARY")
    print("=" * 60)
    print(f"\nTotal Templates: {stats['total_templates']}")
    print(f"\nAverage Timeframe: {stats['avg_timeframe_days']:.1f} days")
    print(f"Average Daily Commitment: {stats['avg_hours_per_day']:.1f} hours")
    
    print("\n" + "=" * 60)
    print("BY CATEGORY")
    print("=" * 60)
    for goal_type, count in sorted(stats['by_type'].items()):
        print(f"{goal_type.upper():20} {count:3} templates")
    
    print("\n" + "=" * 60)
    print("BY SUBDIVISION")
    print("=" * 60)
    for subdivision, count in sorted(stats['by_subdivision'].items()):
        print(f"{subdivision:30} {count:3} templates")
    
    print("\n" + "=" * 60)
    print("BY DIFFICULTY")
    print("=" * 60)
    for difficulty, count in sorted(stats['by_difficulty'].items()):
        print(f"{difficulty:20} {count:3} templates")
    
    print("\n" + "=" * 60)
    print("AVAILABLE SUBDIVISIONS")
    print("=" * 60)
    for subdivision in get_all_subdivisions():
        print(f"  • {subdivision}")
    
    print("\n" + "=" * 60)
