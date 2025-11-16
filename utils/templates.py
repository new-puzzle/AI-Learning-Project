"""
Goal Templates for GoalPath AI
Pre-configured goal templates to help users quick-start with proven goal structures
"""

from typing import Dict, List


class GoalTemplate:
    """Represents a goal template with pre-filled values"""

    def __init__(self, name: str, goal_type: str, goal_text: str,
                 timeframe: int, hours_per_day: float, description: str,
                 tags: List[str] = None, difficulty: str = "Intermediate",
                 prerequisites: str = None):
        self.name = name
        self.goal_type = goal_type
        self.goal_text = goal_text
        self.timeframe = timeframe
        self.hours_per_day = hours_per_day
        self.description = description
        self.tags = tags or []
        self.difficulty = difficulty
        self.prerequisites = prerequisites

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
            'prerequisites': self.prerequisites
        }


# Template Registry
TEMPLATES = []


# ============================================================================
# LEARNING & SKILLS TEMPLATES (10)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Master Prompt Engineering",
    goal_type="learning",
    goal_text="Master prompt engineering for Claude, GPT, and modern AI models",
    timeframe=30,
    hours_per_day=2.0,
    description="Learn prompt design, Claude/GPT best practices, build portfolio of prompts",
    tags=["AI", "Remote-Friendly", "Beginner-Friendly", "In-Demand"],
    difficulty="Beginner",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="Python for Data Science",
    goal_type="learning",
    goal_text="Learn Python data science stack: NumPy, Pandas, Matplotlib, and build real-world projects",
    timeframe=60,
    hours_per_day=2.0,
    description="NumPy, Pandas, Matplotlib, Seaborn, real-world data projects",
    tags=["Python", "Data Science", "Portfolio-Building"],
    difficulty="Intermediate",
    prerequisites="Basic Python knowledge recommended"
))

TEMPLATES.append(GoalTemplate(
    name="Full-Stack Web Development (MERN)",
    goal_type="learning",
    goal_text="Master full-stack web development with MongoDB, Express, React, and Node.js",
    timeframe=90,
    hours_per_day=3.0,
    description="MongoDB, Express, React, Node.js - build 3 full-stack apps",
    tags=["Web Development", "Full-Stack", "Portfolio-Building"],
    difficulty="Intermediate",
    prerequisites="HTML, CSS, JavaScript basics"
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
    prerequisites="Python basics, high school math"
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
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="FastAPI & Modern Python Backend",
    goal_type="learning",
    goal_text="Master FastAPI for building production-ready Python APIs",
    timeframe=30,
    hours_per_day=2.0,
    description="REST APIs, async Python, authentication, testing, deployment",
    tags=["Python", "Backend", "API Development"],
    difficulty="Intermediate",
    prerequisites="Python basics"
))

TEMPLATES.append(GoalTemplate(
    name="Google Cloud Professional Certification",
    goal_type="learning",
    goal_text="Prepare for and pass Google Cloud Professional certification exam",
    timeframe=60,
    hours_per_day=2.0,
    description="GCP services, architecture, certification exam prep",
    tags=["Cloud", "Certification", "Career-Boost"],
    difficulty="Intermediate",
    prerequisites="Basic cloud computing knowledge"
))

TEMPLATES.append(GoalTemplate(
    name="DevOps for Python Developers",
    goal_type="learning",
    goal_text="Learn DevOps essentials: Docker, CI/CD, and cloud deployment for Python apps",
    timeframe=45,
    hours_per_day=2.0,
    description="Docker, GitHub Actions, AWS/GCP deployment, monitoring",
    tags=["DevOps", "Python", "Cloud", "Career-Boost"],
    difficulty="Intermediate",
    prerequisites="Python development experience"
))

TEMPLATES.append(GoalTemplate(
    name="Technical Writing for Remote Work",
    goal_type="learning",
    goal_text="Master technical writing to land remote technical writer roles at international companies",
    timeframe=21,
    hours_per_day=1.5,
    description="API docs, tutorials, portfolio samples for international clients",
    tags=["Technical Writing", "Remote-Friendly", "Portfolio-Building"],
    difficulty="Beginner",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="LangChain & AI Application Development",
    goal_type="learning",
    goal_text="Build AI applications with LangChain, vector databases, and RAG systems",
    timeframe=30,
    hours_per_day=2.0,
    description="Build AI apps with LangChain, vector databases, RAG systems",
    tags=["AI", "LangChain", "In-Demand", "Portfolio-Building"],
    difficulty="Intermediate",
    prerequisites="Python basics, basic AI understanding"
))


# ============================================================================
# CAREER TRANSITION TEMPLATES (10)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Land Remote AI Engineering Role (International)",
    goal_type="career",
    goal_text="Get hired as AI engineer at international company with remote work",
    timeframe=90,
    hours_per_day=3.0,
    description="Build AI skills, portfolio projects, target global companies, ace interviews",
    tags=["AI", "Remote-Friendly", "Career Switch", "International"],
    difficulty="Advanced",
    prerequisites="Python programming experience"
))

TEMPLATES.append(GoalTemplate(
    name="Transition from Teaching to EdTech Product Role",
    goal_type="career",
    goal_text="Transition from teaching to product management role at international EdTech company",
    timeframe=75,
    hours_per_day=2.5,
    description="EdTech industry knowledge, product skills, portfolio, international EdTech applications",
    tags=["EdTech", "Remote-Friendly", "Career Switch", "Teaching Background"],
    difficulty="Intermediate",
    prerequisites="Teaching experience"
))

TEMPLATES.append(GoalTemplate(
    name="Break Into Developer Relations (Remote)",
    goal_type="career",
    goal_text="Land remote Developer Relations role at tech company",
    timeframe=60,
    hours_per_day=2.5,
    description="Technical content, community building, DevRel portfolio, global opportunities",
    tags=["DevRel", "Remote-Friendly", "Content Creation", "Community"],
    difficulty="Intermediate",
    prerequisites="Technical background and communication skills"
))

TEMPLATES.append(GoalTemplate(
    name="Get Hired as Remote Python Developer",
    goal_type="career",
    goal_text="Land remote Python developer position at international software company",
    timeframe=90,
    hours_per_day=3.0,
    description="Advanced Python, projects, GitHub portfolio, international job applications",
    tags=["Python", "Remote-Friendly", "Software Development", "International"],
    difficulty="Intermediate",
    prerequisites="Python fundamentals"
))

TEMPLATES.append(GoalTemplate(
    name="Become AI Prompt Engineer (Emerging Role)",
    goal_type="career",
    goal_text="Get hired as AI Prompt Engineer at AI company or AI-first startup",
    timeframe=60,
    hours_per_day=2.0,
    description="Master prompting, build portfolio, target AI companies globally",
    tags=["AI", "Remote-Friendly", "Emerging Role", "In-Demand"],
    difficulty="Beginner",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="Land Remote Technical Writer Role",
    goal_type="career",
    goal_text="Get hired as technical writer at international tech company (remote)",
    timeframe=45,
    hours_per_day=2.0,
    description="Technical writing samples, portfolio site, applications to global companies",
    tags=["Technical Writing", "Remote-Friendly", "Content Creation"],
    difficulty="Beginner",
    prerequisites="Good writing skills"
))

TEMPLATES.append(GoalTemplate(
    name="Transition to Remote Data Analyst",
    goal_type="career",
    goal_text="Switch career to remote data analyst role at international company",
    timeframe=60,
    hours_per_day=2.5,
    description="SQL, Excel, Python, Tableau - portfolio projects, remote job prep",
    tags=["Data Analysis", "Remote-Friendly", "Career Switch"],
    difficulty="Intermediate",
    prerequisites="Basic Excel/data skills"
))

TEMPLATES.append(GoalTemplate(
    name="Get Hired at Global SaaS Startup",
    goal_type="career",
    goal_text="Land role at high-growth international SaaS startup (remote-first)",
    timeframe=75,
    hours_per_day=2.5,
    description="Research startups, build relevant skills, network, applications",
    tags=["Startup", "Remote-Friendly", "SaaS", "International"],
    difficulty="Intermediate",
    prerequisites="Relevant skills for target role"
))

TEMPLATES.append(GoalTemplate(
    name="Become Remote Solutions Architect",
    goal_type="career",
    goal_text="Transition to Solutions Architect role at global tech company",
    timeframe=90,
    hours_per_day=3.0,
    description="Cloud architecture, system design, certifications, portfolio, job search",
    tags=["Cloud", "Architecture", "Remote-Friendly", "Senior Role"],
    difficulty="Advanced",
    prerequisites="Software development experience"
))

TEMPLATES.append(GoalTemplate(
    name="Break Into AI Safety/Alignment Research",
    goal_type="career",
    goal_text="Get research position in AI safety and alignment at global organization",
    timeframe=90,
    hours_per_day=3.0,
    description="AI safety fundamentals, research portfolio, target organizations",
    tags=["AI Safety", "Research", "Remote-Friendly", "Emerging Field"],
    difficulty="Advanced",
    prerequisites="Strong technical background, research interest"
))


# ============================================================================
# FREELANCE & BUSINESS TEMPLATES (10)
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
    prerequisites=None
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
    prerequisites="Marketable skill (writing, design, development, etc.)"
))

TEMPLATES.append(GoalTemplate(
    name="Launch AI Consulting Practice",
    goal_type="freelance",
    goal_text="Start AI consulting business and land first 3 clients",
    timeframe=45,
    hours_per_day=2.5,
    description="Positioning, pricing, first 3 clients, service packages",
    tags=["AI", "Consulting", "Income-Generating", "High-Value"],
    difficulty="Advanced",
    prerequisites="AI/ML expertise"
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
    prerequisites="Teaching/tutoring experience"
))

TEMPLATES.append(GoalTemplate(
    name="Start No-Code Development Agency",
    goal_type="freelance",
    goal_text="Launch no-code development agency and land first 3 clients",
    timeframe=60,
    hours_per_day=2.5,
    description="Services menu, portfolio, client pipeline, pricing",
    tags=["No-Code", "Agency", "Income-Generating", "Beginner-Friendly"],
    difficulty="Intermediate",
    prerequisites="No-code platform knowledge"
))

TEMPLATES.append(GoalTemplate(
    name="Launch SaaS Product MVP",
    goal_type="freelance",
    goal_text="Build and launch SaaS product MVP with first 10 paying customers",
    timeframe=90,
    hours_per_day=3.0,
    description="Idea validation, MVP development, beta launch, first customers",
    tags=["SaaS", "Product Launch", "Income-Generating", "Entrepreneurship"],
    difficulty="Advanced",
    prerequisites="Technical skills or no-code expertise"
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
    prerequisites="Expert-level skills in development/design/finance"
))

TEMPLATES.append(GoalTemplate(
    name="Earn First $500 from Digital Products",
    goal_type="freelance",
    goal_text="Create and sell digital products earning first $500 in revenue",
    timeframe=30,
    hours_per_day=2.0,
    description="Create templates/courses, market on Gumroad/Etsy, first sales",
    tags=["Digital Products", "Income-Generating", "Passive Income", "Beginner-Friendly"],
    difficulty="Beginner",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="Start Technical Content Writing Business",
    goal_type="freelance",
    goal_text="Launch technical writing freelance business and land first 3 clients",
    timeframe=30,
    hours_per_day=2.0,
    description="Samples, cold outreach, first 3 clients, recurring work",
    tags=["Technical Writing", "Income-Generating", "Remote-Friendly", "Content"],
    difficulty="Beginner",
    prerequisites="Good writing skills, technical interest"
))

TEMPLATES.append(GoalTemplate(
    name="Build Passive Income Stream ($200/Month)",
    goal_type="freelance",
    goal_text="Create passive income stream generating $200/month",
    timeframe=60,
    hours_per_day=2.0,
    description="Choose model (affiliate, digital products, API), build, monetize",
    tags=["Passive Income", "Income-Generating", "Automation"],
    difficulty="Intermediate",
    prerequisites="Marketing or technical skills"
))


# ============================================================================
# PROJECT COMPLETION TEMPLATES (10)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Build & Launch Developer Portfolio Website",
    goal_type="project",
    goal_text="Create professional developer portfolio website and launch with custom domain",
    timeframe=14,
    hours_per_day=2.0,
    description="Design, development, content, SEO, deploy to custom domain",
    tags=["Portfolio", "Web Development", "Career-Boost", "Quick-Start"],
    difficulty="Beginner",
    prerequisites="Basic HTML/CSS or no-code tools"
))

TEMPLATES.append(GoalTemplate(
    name="Create & Launch Course on Udemy",
    goal_type="project",
    goal_text="Create and publish course on Udemy with first 50 students",
    timeframe=45,
    hours_per_day=2.5,
    description="Course outline, recording, editing, marketing, first students",
    tags=["Course Creation", "Income-Generating", "Content Creation"],
    difficulty="Intermediate",
    prerequisites="Expertise in a topic"
))

TEMPLATES.append(GoalTemplate(
    name="Build & Launch AI-Powered SaaS Tool",
    goal_type="project",
    goal_text="Build and launch AI-powered SaaS tool on Product Hunt",
    timeframe=60,
    hours_per_day=3.0,
    description="Planning, development (Python/JS), testing, ProductHunt launch",
    tags=["AI", "SaaS", "Product Launch", "Portfolio-Building"],
    difficulty="Advanced",
    prerequisites="Development skills or no-code expertise"
))

TEMPLATES.append(GoalTemplate(
    name="Write & Publish Technical eBook",
    goal_type="project",
    goal_text="Write and self-publish technical eBook on Amazon/Gumroad",
    timeframe=30,
    hours_per_day=2.0,
    description="Outline, writing, editing, Gumroad/Amazon publishing",
    tags=["Writing", "Income-Generating", "Content Creation"],
    difficulty="Beginner",
    prerequisites="Technical knowledge in a topic"
))

TEMPLATES.append(GoalTemplate(
    name="Build Chrome Extension (10K Users)",
    goal_type="project",
    goal_text="Develop Chrome extension and grow to 10,000 users",
    timeframe=21,
    hours_per_day=2.0,
    description="Development, testing, Chrome Web Store, marketing",
    tags=["Chrome Extension", "Product Launch", "Portfolio-Building"],
    difficulty="Intermediate",
    prerequisites="JavaScript basics"
))

TEMPLATES.append(GoalTemplate(
    name="Launch YouTube Channel (First 1000 Subscribers)",
    goal_type="project",
    goal_text="Start YouTube channel and grow to 1000 subscribers",
    timeframe=90,
    hours_per_day=2.0,
    description="Niche selection, 20 videos, SEO, community building",
    tags=["YouTube", "Content Creation", "Community Building"],
    difficulty="Intermediate",
    prerequisites="Content creation interest"
))

TEMPLATES.append(GoalTemplate(
    name="Launch Open Source Project (100 Stars)",
    goal_type="project",
    goal_text="Create open source project and grow to 100 GitHub stars",
    timeframe=45,
    hours_per_day=2.0,
    description="Planning, development, documentation, community, promotion",
    tags=["Open Source", "Portfolio-Building", "Community"],
    difficulty="Intermediate",
    prerequisites="Development skills"
))

TEMPLATES.append(GoalTemplate(
    name="Build & Launch API Service",
    goal_type="project",
    goal_text="Build API service and acquire first 10 paying customers",
    timeframe=45,
    hours_per_day=2.5,
    description="API development, documentation, monetization, first customers",
    tags=["API", "Income-Generating", "Developer Tools"],
    difficulty="Advanced",
    prerequisites="Backend development experience"
))

TEMPLATES.append(GoalTemplate(
    name="Create Premium Notion Template Business",
    goal_type="project",
    goal_text="Create and sell premium Notion templates earning first $200",
    timeframe=21,
    hours_per_day=1.5,
    description="Templates, marketing, Gumroad setup, first sales",
    tags=["Notion", "Digital Products", "Income-Generating", "Quick-Start"],
    difficulty="Beginner",
    prerequisites="Notion knowledge"
))

TEMPLATES.append(GoalTemplate(
    name="Develop Mobile App & Launch on Stores",
    goal_type="project",
    goal_text="Build mobile app and launch on App Store and Play Store",
    timeframe=60,
    hours_per_day=3.0,
    description="Flutter/React Native, development, testing, App/Play Store",
    tags=["Mobile Development", "Product Launch", "Portfolio-Building"],
    difficulty="Advanced",
    prerequisites="Programming experience"
))


# ============================================================================
# PERSONAL ACHIEVEMENT TEMPLATES (10)
# ============================================================================

TEMPLATES.append(GoalTemplate(
    name="Run Your First 5K Race",
    goal_type="personal",
    goal_text="Train for and complete first 5K race",
    timeframe=30,
    hours_per_day=1.0,
    description="Couch to 5K training plan, nutrition basics, race registration",
    tags=["Fitness", "Running", "Health", "Beginner-Friendly"],
    difficulty="Beginner",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="Build Bulletproof Morning Routine",
    goal_type="personal",
    goal_text="Establish consistent morning routine for productivity and wellness",
    timeframe=21,
    hours_per_day=0.5,
    description="Design optimal routine, track consistency, make it stick",
    tags=["Habits", "Productivity", "Wellness", "Quick-Start"],
    difficulty="Beginner",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="Learn Guitar (Play 10 Songs)",
    goal_type="personal",
    goal_text="Learn guitar basics and master 10 songs",
    timeframe=60,
    hours_per_day=1.0,
    description="Basics, chords, strumming, 10 song mastery",
    tags=["Music", "Creative", "Skill Building"],
    difficulty="Beginner",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="Lose 10 Pounds Sustainably",
    goal_type="personal",
    goal_text="Lose 10 pounds through sustainable nutrition and exercise habits",
    timeframe=45,
    hours_per_day=1.0,
    description="Nutrition plan, exercise routine, habit formation, tracking",
    tags=["Fitness", "Health", "Weight Loss"],
    difficulty="Intermediate",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="Master Daily Meditation Practice",
    goal_type="personal",
    goal_text="Establish daily meditation practice for 30 consecutive days",
    timeframe=30,
    hours_per_day=0.33,
    description="Techniques, apps, consistency, mindfulness integration",
    tags=["Meditation", "Mental Health", "Habits", "Wellness"],
    difficulty="Beginner",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="Read 12 Books in 90 Days",
    goal_type="personal",
    goal_text="Read 12 books in 90 days with comprehension and note-taking",
    timeframe=90,
    hours_per_day=1.0,
    description="Book selection, reading schedule, comprehension, notes",
    tags=["Reading", "Learning", "Personal Growth"],
    difficulty="Beginner",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="Achieve Conversational Spanish Fluency",
    goal_type="personal",
    goal_text="Reach conversational fluency in Spanish",
    timeframe=90,
    hours_per_day=1.0,
    description="Duolingo, iTalki tutors, conversation practice, immersion",
    tags=["Language Learning", "Spanish", "Communication"],
    difficulty="Intermediate",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="Complete 30-Day Strength Training Challenge",
    goal_type="personal",
    goal_text="Complete 30-day strength training program and build muscle",
    timeframe=30,
    hours_per_day=0.75,
    description="Workout plan, progressive overload, nutrition, tracking",
    tags=["Fitness", "Strength Training", "Health"],
    difficulty="Beginner",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="Establish Daily Writing Habit (500 Words)",
    goal_type="personal",
    goal_text="Write 500 words daily for 21 consecutive days",
    timeframe=21,
    hours_per_day=0.5,
    description="Write daily, overcome resistance, build consistency",
    tags=["Writing", "Habits", "Creative", "Quick-Start"],
    difficulty="Beginner",
    prerequisites=None
))

TEMPLATES.append(GoalTemplate(
    name="Improve Public Speaking (10 Presentations)",
    goal_type="personal",
    goal_text="Deliver 10 presentations to improve public speaking skills",
    timeframe=45,
    hours_per_day=1.0,
    description="Toastmasters/practice, techniques, deliver 10 talks",
    tags=["Public Speaking", "Communication", "Confidence"],
    difficulty="Intermediate",
    prerequisites=None
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
