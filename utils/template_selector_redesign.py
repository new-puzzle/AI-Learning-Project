"""
New Card-Based Template Selector for GoalPath AI
Multi-level navigation: Categories → Subdivisions → Templates → Customization
"""

import streamlit as st
import re
from typing import Dict, List


# ============================================================================
# CARD STYLING & CSS
# ============================================================================

def inject_card_styles():
    """Inject custom CSS for card-based UI"""
    st.markdown("""
    <style>
    /* ===== LEVEL 1: MAIN CATEGORY CARDS ===== */
    .category-card-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin: 20px 0;
    }
    
    .category-card {
        background: linear-gradient(135deg, var(--card-color-1) 0%, var(--card-color-2) 100%);
        border-radius: 16px;
        padding: 30px 20px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 2px solid transparent;
        position: relative;
        overflow: hidden;
    }
    
    .category-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
        border-color: rgba(255,255,255,0.3);
    }
    
    .category-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .category-card:hover::before {
        opacity: 1;
    }
    
    .category-icon {
        font-size: 60px;
        margin-bottom: 15px;
        display: block;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
    }
    
    .category-name {
        font-size: 24px;
        font-weight: 700;
        color: white;
        margin-bottom: 8px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .category-count {
        font-size: 16px;
        color: rgba(255,255,255,0.9);
        font-weight: 500;
    }
    
    .category-description {
        font-size: 14px;
        color: rgba(255,255,255,0.8);
        margin-top: 10px;
        line-height: 1.4;
    }
    
    /* Category-specific gradients */
    .category-learning {
        --card-color-1: #667eea;
        --card-color-2: #764ba2;
    }
    
    .category-career {
        --card-color-1: #f093fb;
        --card-color-2: #f5576c;
    }
    
    .category-freelance {
        --card-color-1: #4facfe;
        --card-color-2: #00f2fe;
    }
    
    .category-project {
        --card-color-1: #43e97b;
        --card-color-2: #38f9d7;
    }
    
    .category-personal {
        --card-color-1: #fa709a;
        --card-color-2: #fee140;
    }
    
    /* ===== LEVEL 2: SUBDIVISION CARDS ===== */
    .subdivision-card-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 18px;
        margin: 25px 0;
    }
    
    .subdivision-card {
        background: #2d3748;
        border-radius: 12px;
        padding: 24px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        border: 2px solid #4a5568;
        position: relative;
    }
    
    .subdivision-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.4);
        border-color: var(--accent-color);
        background: #374151;
    }
    
    .subdivision-card::after {
        content: '→';
        position: absolute;
        right: 20px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 24px;
        color: var(--accent-color);
        opacity: 0;
        transition: all 0.3s ease;
    }
    
    .subdivision-card:hover::after {
        opacity: 1;
        right: 16px;
    }
    
    .subdivision-icon {
        font-size: 40px;
        margin-bottom: 12px;
        display: block;
    }
    
    .subdivision-name {
        font-size: 18px;
        font-weight: 600;
        color: #e2e8f0;
        margin-bottom: 8px;
    }
    
    .subdivision-count {
        font-size: 14px;
        color: #cbd5e0;
        margin-bottom: 8px;
    }
    
    .subdivision-description {
        font-size: 13px;
        color: #a0aec0;
        line-height: 1.5;
    }
    
    /* ===== LEVEL 3: TEMPLATE CARDS ===== */
    .template-card-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
        gap: 20px;
        margin: 25px 0;
    }
    
    .template-card {
        background: #2d3748;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        border: 2px solid #4a5568;
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    
    .template-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.4);
        border-color: var(--accent-color);
        background: #374151;
    }
    
    .template-header {
        margin-bottom: 12px;
    }
    
    .template-name {
        font-size: 18px;
        font-weight: 600;
        color: #e2e8f0;
        margin-bottom: 8px;
        line-height: 1.3;
    }
    
    .template-description {
        font-size: 14px;
        color: #cbd5e0;
        line-height: 1.5;
        margin-bottom: 16px;
        flex-grow: 1;
    }
    
    .template-metadata {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-bottom: 16px;
        padding-bottom: 16px;
        border-bottom: 1px solid #4a5568;
    }
    
    .template-meta-item {
        display: flex;
        align-items: center;
        gap: 4px;
        font-size: 13px;
        color: #cbd5e0;
    }
    
    .difficulty-badge {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
    }
    
    .difficulty-beginner {
        background-color: #c6f6d5;
        color: #22543d;
    }
    
    .difficulty-intermediate {
        background-color: #fef3c7;
        color: #78350f;
    }
    
    .difficulty-advanced {
        background-color: #fecaca;
        color: #7f1d1d;
    }
    
    .template-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-bottom: 16px;
    }
    
    .tag-pill {
        padding: 4px 10px;
        background-color: #4a5568;
        color: #e2e8f0;
        border-radius: 12px;
        font-size: 11px;
        font-weight: 500;
    }
    
    /* ===== NAVIGATION ===== */
    .breadcrumb {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 20px;
        padding: 12px 0;
        font-size: 14px;
        color: #cbd5e0;
    }
    
    .breadcrumb-item {
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .breadcrumb-link {
        color: #4299e1;
        text-decoration: none;
        cursor: pointer;
    }
    
    .breadcrumb-link:hover {
        text-decoration: underline;
    }
    
    .breadcrumb-separator {
        color: #cbd5e0;
    }
    
    .breadcrumb-current {
        color: #e2e8f0;
        font-weight: 600;
    }
    
    /* ===== SEARCH & FILTERS ===== */
    .search-filter-bar {
        background: #2d3748;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        margin-bottom: 25px;
        border: 2px solid #4a5568;
    }
    
    /* ===== RESPONSIVE DESIGN ===== */
    @media (max-width: 768px) {
        .category-card-container {
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 12px;
        }
        
        .category-card {
            padding: 20px 15px;
        }
        
        .category-icon {
            font-size: 40px;
        }
        
        .category-name {
            font-size: 18px;
        }
        
        .subdivision-card-container,
        .template-card-container {
            grid-template-columns: 1fr;
            gap: 15px;
        }
    }
    
    /* ===== ANIMATIONS ===== */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.5s ease-out;
    }
    </style>
    """, unsafe_allow_html=True)


# ============================================================================
# SUBDIVISION DEFINITIONS (72 intelligent subdivisions)
# ============================================================================

SUBDIVISION_DEFINITIONS = {
    "learning": {
        # TECH (5 subdivisions)
        "Python & Backend Development": {
            "icon": "🐍",
            "description": "Python, FastAPI, Backend Development, Scientific Computing",
            "keywords": ["python", "backend", "fastapi", "devops", "scientific computing"]
        },
        "Web Development & Design": {
            "icon": "🌐",
            "description": "React, MERN, TypeScript, GraphQL, Full-Stack",
            "keywords": ["web development", "react", "mern", "typescript", "graphql", "full-stack", "frontend"]
        },
        "AI & Machine Learning": {
            "icon": "🤖",
            "description": "Prompt Engineering, ML, LangChain, Data Visualization",
            "keywords": ["ai", "machine learning", "prompt engineering", "langchain", "data visualization", "neural"]
        },
        "Cloud, DevOps & Developer Tools": {
            "icon": "☁️",
            "description": "AWS, Kubernetes, Git, Cybersecurity, Rust, Blockchain",
            "keywords": ["aws", "cloud", "kubernetes", "git", "github", "cybersecurity", "rust", "blockchain", "devops"]
        },
        "Mobile Development & No-Code": {
            "icon": "📱",
            "description": "React Native, No-Code, SQL, Databases",
            "keywords": ["mobile", "react native", "no-code", "sql", "database"]
        },
        
        # STEM (3 subdivisions)
        "Mathematics": {
            "icon": "➕",
            "description": "Calculus, Linear Algebra, Statistics, Differential Equations",
            "keywords": ["calculus", "linear algebra", "statistics", "probability", "differential equations", "discrete math"]
        },
        "Physics & Chemistry": {
            "icon": "⚛️",
            "description": "Mechanics, Organic Chemistry, Thermodynamics, Quantum, Astronomy",
            "keywords": ["physics", "chemistry", "organic chemistry", "thermodynamics", "quantum", "astronomy", "materials science"]
        },
        "Life Sciences": {
            "icon": "🧬",
            "description": "Biology, Neuroscience, Molecular Biology, Electronics",
            "keywords": ["biology", "molecular biology", "neuroscience", "electronics", "circuit"]
        },
        
        # BUSINESS & MONEY (5 subdivisions)
        "Personal Finance & Investing": {
            "icon": "💰",
            "description": "Stock Market, Wealth Building, Financial Analysis, Accounting",
            "keywords": ["finance", "investing", "stock market", "personal finance", "wealth building", "financial analysis", "accounting"]
        },
        "Marketing & Sales Skills": {
            "icon": "📣",
            "description": "Digital Marketing, Sales Techniques, Revenue Generation",
            "keywords": ["marketing", "digital marketing", "sales"]
        },
        "Business Strategy & Entrepreneurship": {
            "icon": "💼",
            "description": "Strategy, Frameworks, Entrepreneurship, Product Management",
            "keywords": ["business strategy", "entrepreneurship", "startup", "product management", "frameworks"]
        },
        "Accounting & Financial Analysis": {
            "icon": "📊",
            "description": "Accounting Fundamentals, Financial Modeling",
            "keywords": ["accounting", "financial modeling"]
        },
        "Operations & Analytics": {
            "icon": "📈",
            "description": "Business Analytics, Supply Chain, Project Management",
            "keywords": ["business analytics", "supply chain", "project management", "pmp", "operations"]
        },
        
        # LANGUAGES (2 subdivisions)
        "European Languages": {
            "icon": "🇪🇺",
            "description": "Spanish, German, Italian, Portuguese, French",
            "keywords": ["spanish", "german", "italian", "portuguese", "french", "b2", "b1", "a2"]
        },
        "Asian & Other Languages": {
            "icon": "🌏",
            "description": "Japanese, Mandarin, Korean, Arabic",
            "keywords": ["japanese", "chinese", "mandarin", "korean", "arabic", "jlpt", "hsk", "topik"]
        },
        
        # CREATIVE ARTS (3 subdivisions)
        "Visual Arts & Design": {
            "icon": "🎨",
            "description": "Drawing, Color Theory, Art History, Typography, UI/UX",
            "keywords": ["drawing", "color theory", "art history", "typography", "ui/ux", "design"]
        },
        "Music & Performance": {
            "icon": "🎭",
            "description": "Music Theory, Acting, Performance Techniques",
            "keywords": ["music theory", "acting", "performance", "theater"]
        },
        "Writing & Storytelling": {
            "icon": "✍️",
            "description": "Creative Writing, Poetry, Film Analysis, Literature",
            "keywords": ["creative writing", "poetry", "film", "storytelling", "literature"]
        },
        
        # PERSONAL DEVELOPMENT (4 subdivisions)
        "Leadership & Professional Skills": {
            "icon": "👔",
            "description": "Leadership, Strategic Thinking, Influence, Cultural Intelligence",
            "keywords": ["leadership", "strategic thinking", "influence", "persuasion", "cultural intelligence", "executive"]
        },
        "Personal Effectiveness": {
            "icon": "⚡",
            "description": "Time Management, Discipline, Critical Thinking, Problem-Solving",
            "keywords": ["time management", "productivity", "discipline", "critical thinking", "problem-solving", "decision making"]
        },
        "Meditation & Philosophy": {
            "icon": "🧘",
            "description": "Vipassana, Stoicism, Transcendental Meditation",
            "keywords": ["meditation", "vipassana", "stoic", "transcendental", "philosophy"]
        },
        "Cognitive Skills": {
            "icon": "🧠",
            "description": "Memory Palace, Speed Reading, Mind Mapping, CBT",
            "keywords": ["lucid dreaming", "memory", "speed reading", "mind mapping", "cbt", "cognitive"]
        },
        
        # NEW - EVERYDAY SKILLS (3 subdivisions)
        "Cooking & Nutrition": {
            "icon": "🍳",
            "description": "Meal Planning, Healthy Cooking, Baking, Nutrition Basics",
            "keywords": ["cooking", "nutrition", "meal planning", "baking", "healthy eating"]
        },
        "Home & Life Management": {
            "icon": "🏠",
            "description": "Organization, Decluttering, Basic Repairs, Budgeting",
            "keywords": ["organization", "declutter", "home repair", "budgeting", "life management"]
        },
        "Parenting & Family Skills": {
            "icon": "👨‍👩‍👧",
            "description": "Child Development, Parenting Strategies, Family Time",
            "keywords": ["parenting", "child development", "family", "caregiving"]
        }
    },
    "career": {
        "Tech Career Paths": {
            "icon": "👨‍💻",
            "description": "AI Engineer, Developer, Data Analyst, DevRel",
            "keywords": ["ai engineering", "python developer", "data analyst", "developer relations", "edtech", "remote ai"]
        },
        "Business & Consulting Roles": {
            "icon": "📊",
            "description": "Product Manager, Management Consulting, Financial Analyst",
            "keywords": ["product manager", "consulting", "financial analyst", "business"]
        },
        "Creative & Content Careers": {
            "icon": "🎨",
            "description": "UX/UI Designer, Technical Writer, Content Creator",
            "keywords": ["ux", "ui", "designer", "technical writer", "content"]
        },
        "Healthcare & Education Careers": {
            "icon": "🏥",
            "description": "Teaching, Healthcare Admin, Counseling, Education",
            "keywords": ["teaching", "healthcare", "education", "counseling", "admin"]
        },
        "Trades & Service Careers": {
            "icon": "🛠️",
            "description": "Real Estate, Sales, Skilled Trades, Service Industry",
            "keywords": ["real estate", "sales", "trades", "service", "skilled"]
        }
    },
    "freelance": {
        "Design & Creative Freelancing": {
            "icon": "🎨",
            "description": "Design, Art, Creative Work, 99designs",
            "keywords": ["design", "99designs", "creative", "art", "freelance design"]
        },
        "Writing & Content Freelancing": {
            "icon": "✍️",
            "description": "Writing, Copywriting, Content, Medium, Technical Writing",
            "keywords": ["writing", "medium", "content", "copywriting", "technical writing", "social media management"]
        },
        "Professional Services": {
            "icon": "💼",
            "description": "Virtual Assistant, Transcription, Bookkeeping, Translation",
            "keywords": ["virtual assistant", "transcription", "bookkeeping", "translation", "admin"]
        },
        "Tech Freelancing": {
            "icon": "💻",
            "description": "Web Dev, App Dev, Tech Services",
            "keywords": ["web development", "app development", "tech freelancing"]
        },
        "Business & Strategy Consulting": {
            "icon": "🎓",
            "description": "AI Consulting, Business Strategy, Marketing, HR",
            "keywords": ["ai consulting", "business strategy", "marketing consulting", "hr consulting", "strategy"]
        },
        "Tech & Development Consulting": {
            "icon": "👨‍💻",
            "description": "Web Dev Consulting, Data Analytics Consulting",
            "keywords": ["web development consulting", "data analytics consulting", "tech consulting"]
        },
        "Finance & Planning Consulting": {
            "icon": "💰",
            "description": "Financial Planning, SEO Consulting",
            "keywords": ["financial planning", "seo consulting", "finance consulting"]
        },
        "Digital Products & Templates": {
            "icon": "📦",
            "description": "Notion, Canva, Ebooks, Stock Photos, Digital Art, Fonts",
            "keywords": ["digital product", "notion template", "canva template", "stock photo", "digital art", "font", "typeface"]
        },
        "SaaS & Software Products": {
            "icon": "⚙️",
            "description": "SaaS MVP, API, Chrome Extension, WordPress Plugin, Mobile App",
            "keywords": ["saas", "api service", "chrome extension", "wordpress plugin", "mobile app", "freemium"]
        },
        "Passive Income Streams": {
            "icon": "💸",
            "description": "Affiliate Marketing, Print-on-Demand, YouTube, Blog",
            "keywords": ["passive income", "affiliate", "print-on-demand", "youtube", "blog", "monetize"]
        },
        "Crafts & Handmade Business": {
            "icon": "🧵",
            "description": "Etsy, Handmade Goods, Crafts, Artisan Products",
            "keywords": ["etsy", "handmade", "craft", "artisan"]
        },
        "E-Commerce & Physical Products": {
            "icon": "📦",
            "description": "Dropshipping, Local Business, Physical Products",
            "keywords": ["dropshipping", "e-commerce", "physical product", "local business", "store"]
        }
    },
    "project": {
        "Tech & Software Projects": {
            "icon": "🖥️",
            "description": "SaaS MVP, AI Web App, Chrome Extension, Mobile App",
            "keywords": ["saas mvp", "ai-powered", "chrome extension", "mobile app", "web app", "software", "api"]
        },
        "Content & Media Projects": {
            "icon": "🎥",
            "description": "YouTube Channel, Newsletter, Podcast",
            "keywords": ["youtube", "newsletter", "podcast", "content creation", "channel"]
        },
        "Online Education": {
            "icon": "👨‍🏫",
            "description": "Create Online Course, Start Tutoring Business",
            "keywords": ["online course", "tutoring business", "teaching", "education"]
        },
        "E-Commerce & Digital Sales": {
            "icon": "🛒",
            "description": "E-Commerce Store, Notion Templates Business",
            "keywords": ["e-commerce", "notion templates business", "digital sales", "store"]
        },
        "Freelance Business Launch": {
            "icon": "💼",
            "description": "Freelance Writing Business",
            "keywords": ["freelance writing", "freelance business", "writing business"]
        },
        "Creative Projects": {
            "icon": "🎨",
            "description": "Art Portfolio, Music Album, Photography Book",
            "keywords": ["art portfolio", "music album", "photography book", "creative project"]
        },
        "Home & Life Projects": {
            "icon": "🏡",
            "description": "Home Renovation, Garden Makeover, Family Events",
            "keywords": ["home renovation", "garden", "family event", "life project"]
        }
    },
    "personal": {
        # FITNESS & HEALTH (5)
        "Running & Endurance": {
            "icon": "🏃",
            "description": "5K, Half Marathon, Marathon, Triathlon, OCR",
            "keywords": ["5k", "half marathon", "marathon", "triathlon", "ironman", "ocr", "obstacle course", "sub-20", "running"]
        },
        "Strength & Muscle Building": {
            "icon": "💪",
            "description": "Gym, Calisthenics, Muscle-Up, 100 Push-ups, Strength Training",
            "keywords": ["muscle", "strength training", "calisthenics", "muscle-up", "push-ups", "bodyweight", "gym"]
        },
        "Weight Management": {
            "icon": "⚖️",
            "description": "Lose Weight, Gain Muscle, Body Composition",
            "keywords": ["lose", "weight loss", "gain", "pounds"]
        },
        "Flexibility, Mobility & Recovery": {
            "icon": "🧘",
            "description": "Yoga, Swimming, Posture, Sleep Optimization",
            "keywords": ["yoga", "flexibility", "swimming", "posture", "back pain", "sleep", "mobility"]
        },
        "Nutrition & Healthy Eating": {
            "icon": "🥗",
            "description": "Meal Prep, Healthy Habits, Nutrition Tracking",
            "keywords": ["nutrition", "meal prep", "healthy eating", "hydration", "water"]
        },
        
        # HABITS & WELLNESS (4)
        "Morning & Daily Routines": {
            "icon": "☀️",
            "description": "Morning Routine, Wake at 5 AM, Time Blocking",
            "keywords": ["morning routine", "wake up", "5 am", "time blocking"]
        },
        "Digital Wellness & Detox": {
            "icon": "📵",
            "description": "Quit Social Media, Screen Time, Phone-Free Meals, Inbox Zero",
            "keywords": ["social media", "digital detox", "screen time", "phone", "inbox zero"]
        },
        "Health Habits": {
            "icon": "💚",
            "description": "Daily Meditation, No Alcohol, Water, Cold Shower, Breathwork",
            "keywords": ["daily meditation", "alcohol", "water daily", "cold shower", "breathwork"]
        },
        "Mindfulness & Reflection": {
            "icon": "📔",
            "description": "Journaling, Gratitude, Weekly Review",
            "keywords": ["journaling", "gratitude", "weekly review", "reflection"]
        },
        
        # CREATIVE HOBBIES (4)
        "Music": {
            "icon": "🎸",
            "description": "Guitar, Piano, Singing, DJ, Music Production",
            "keywords": ["guitar", "piano", "singing", "voice training", "dj", "music production"]
        },
        "Visual Arts": {
            "icon": "🎨",
            "description": "Drawing, Photography, Pottery, Portrait, Calligraphy",
            "keywords": ["drawing", "photography", "pottery", "portrait", "calligraphy", "ceramics", "painting"]
        },
        "Digital Creative": {
            "icon": "🎬",
            "description": "Video Editing, 3D Modeling, Animation",
            "keywords": ["video editing", "3d modeling", "blender", "animation", "motion graphics"]
        },
        "Writing": {
            "icon": "✍️",
            "description": "Daily Writing Habit, Novel Draft, Creative Writing",
            "keywords": ["daily writing", "novel", "500 words", "50,000 words", "draft"]
        },
        
        # EVERYDAY HOBBIES (3)
        "Gardening & Plants": {
            "icon": "🌱",
            "description": "Indoor Gardening, Urban Farming, Houseplants",
            "keywords": ["gardening", "plants", "indoor gardening", "urban farm", "houseplants"]
        },
        "Puzzles & Games": {
            "icon": "🧩",
            "description": "Chess, Board Games, Puzzles, Collecting",
            "keywords": ["chess", "puzzle", "board game", "collecting", "games"]
        },
        "Cooking & Baking": {
            "icon": "🍳",
            "description": "Advanced Cooking, Baking, Fermentation",
            "keywords": ["cooking hobby", "baking hobby", "fermentation", "advanced cooking"]
        },
        
        # COMMUNICATION (3)
        "Public Speaking & Presentation": {
            "icon": "🎤",
            "description": "Public Speaking, Storytelling, Business Email",
            "keywords": ["public speaking", "presentation", "storytelling", "business email"]
        },
        "Foreign Language Practice": {
            "icon": "🗣️",
            "description": "Conversational Fluency, Language Practice",
            "keywords": ["conversational", "fluency practice", "achieve", "improve"]
        },
        "Interpersonal Skills": {
            "icon": "💬",
            "description": "Active Listening, Negotiation, Assertiveness, LinkedIn",
            "keywords": ["active listening", "negotiation", "assertiveness", "linkedin networking", "sign language"]
        },
        
        # MENTAL HEALTH (3)
        "Anxiety & Stress Management": {
            "icon": "🌊",
            "description": "Overcome Anxiety, CBT, Mindfulness, Stress Management",
            "keywords": ["anxiety", "cbt", "mindfulness", "stress", "self-compassion"]
        },
        "Confidence & Self-Worth": {
            "icon": "✨",
            "description": "Emotional Intelligence, Self-Confidence, Perfectionism, Growth Mindset",
            "keywords": ["emotional intelligence", "confidence", "perfectionism", "growth mindset"]
        },
        "Discipline & Mental Toughness": {
            "icon": "🔥",
            "description": "Overcome Procrastination, Resilience, Mental Toughness",
            "keywords": ["procrastination", "resilience", "mental toughness"]
        },
        
        # RELATIONSHIPS (2)
        "Romantic & Family Relationships": {
            "icon": "❤️",
            "description": "Strengthen Marriage, Parenting, Improve Family",
            "keywords": ["romantic", "relationship", "family", "parent", "caregiver"]
        },
        "Friendships & Social Life": {
            "icon": "🤝",
            "description": "Build Friendships, Conflict Resolution, Boundaries, Social Circle",
            "keywords": ["friendship", "conflict resolution", "boundaries", "social circle", "reconnect"]
        },
        
        # COMMUNITY (1)
        "Community & Volunteering": {
            "icon": "🤝",
            "description": "Local Volunteering, Community Projects, Activism",
            "keywords": ["volunteer", "community", "activism", "local"]
        }
    }
}


# Category metadata
CATEGORY_METADATA = {
    "learning": {
        "name": "Learning & Skills",
        "icon": "📚",
        "description": "Master new skills and knowledge domains",
        "color_class": "category-learning"
    },
    "career": {
        "name": "Career Transition",
        "icon": "💼",
        "description": "Land your dream job or pivot careers",
        "color_class": "category-career"
    },
    "freelance": {
        "name": "Freelance & Business",
        "icon": "💰",
        "description": "Build income streams and businesses",
        "color_class": "category-freelance"
    },
    "project": {
        "name": "Project Completion",
        "icon": "🚀",
        "description": "Launch projects and creative ventures",
        "color_class": "category-project"
    },
    "personal": {
        "name": "Personal Achievement",
        "icon": "🎯",
        "description": "Improve health, habits, and lifestyle",
        "color_class": "category-personal"
    }
}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def count_templates_by_category(all_templates: List) -> Dict[str, int]:
    """Count templates in each main category"""
    counts = {"learning": 0, "career": 0, "freelance": 0, "project": 0, "personal": 0}
    for template in all_templates:
        if template.goal_type in counts:
            counts[template.goal_type] += 1
    return counts


def _keyword_matches(text: str, keyword: str) -> bool:
    """Check if keyword matches in text using word boundaries to avoid substring false positives"""
    # Use word boundary regex to match whole words or phrases
    # Escape special regex characters in keyword
    escaped_keyword = re.escape(keyword.lower())
    # Match word boundaries or start/end of string
    pattern = r'\b' + escaped_keyword + r'\b'
    return bool(re.search(pattern, text.lower()))


def count_templates_by_subdivision(all_templates: List, category: str) -> Dict[str, int]:
    """Count templates in each subdivision for a given category"""
    counts = {}
    category_templates = [t for t in all_templates if t.goal_type == category]
    
    # Get subdivision definitions for this category
    subdivisions = SUBDIVISION_DEFINITIONS.get(category, {})
    
    # Initialize counts
    for subdivision_name in subdivisions.keys():
        counts[subdivision_name] = 0
    
    # Count templates by matching keywords or subdivision_category
    for template in category_templates:
        matched = False
        template_subdivision = getattr(template, 'subdivision_category', None)
        template_name = template.name.lower()
        template_desc = template.description.lower()
        
        # Try to match by subdivision
        for subdivision_name, subdivision_data in subdivisions.items():
            keywords = subdivision_data.get("keywords", [])
            
            # Check if template's subdivision_category matches any keyword
            if template_subdivision:
                if any(_keyword_matches(template_subdivision, keyword) for keyword in keywords):
                    counts[subdivision_name] += 1
                    matched = True
                    break
            
            # Check if template name or description contains keywords (using word boundaries)
            if not matched:
                if any(_keyword_matches(template_name, keyword) or _keyword_matches(template_desc, keyword) for keyword in keywords):
                    counts[subdivision_name] += 1
                    matched = True
                    break
        
        # If no match, add to first subdivision (fallback)
        if not matched and subdivisions:
            first_subdivision = list(subdivisions.keys())[0]
            counts[first_subdivision] += 1
    
    return counts


def get_templates_for_subdivision(all_templates: List, category: str, subdivision: str) -> List:
    """Get all templates that belong to a specific subdivision"""
    category_templates = [t for t in all_templates if t.goal_type == category]
    
    # Get keywords for this subdivision
    subdivisions = SUBDIVISION_DEFINITIONS.get(category, {})
    subdivision_data = subdivisions.get(subdivision, {})
    keywords = subdivision_data.get("keywords", [])
    
    matched_templates = []
    for template in category_templates:
        template_subdivision = getattr(template, 'subdivision_category', None)
        template_name = template.name.lower()
        template_desc = template.description.lower()
        
        # Match by subdivision_category or keywords (using word boundaries)
        if template_subdivision:
            if any(_keyword_matches(template_subdivision, keyword) for keyword in keywords):
                matched_templates.append(template)
                continue
        
        # Match by name or description (using word boundaries)
        if any(_keyword_matches(template_name, keyword) or _keyword_matches(template_desc, keyword) for keyword in keywords):
            matched_templates.append(template)
    
    return matched_templates


# ============================================================================
# UI RENDERING FUNCTIONS
# ============================================================================

def render_breadcrumb(level: str, category: str = None, subdivision: str = None):
    """Render breadcrumb navigation using Streamlit buttons"""
    # Use columns for breadcrumb buttons
    breadcrumb_parts = ["🏠 Templates"]
    
    if category:
        cat_meta = CATEGORY_METADATA.get(category, {})
        breadcrumb_parts.append(cat_meta.get("name", category))
    
    if subdivision:
        breadcrumb_parts.append(subdivision)
    
    # Create columns for breadcrumb
    cols = st.columns(len(breadcrumb_parts) * 2 - 1)  # Space for separators
    
    for i, part in enumerate(breadcrumb_parts):
        col_idx = i * 2
        with cols[col_idx]:
            is_current = (i == len(breadcrumb_parts) - 1)
            
            if is_current:
                # Current location - just text
                st.markdown(f"**{part}**")
            else:
                # Clickable breadcrumb
                button_key = f"breadcrumb_{i}_{part}"
                if st.button(part, key=button_key, type="secondary"):
                    if i == 0:
                        # Go to categories
                        st.session_state.template_nav_level = "categories"
                        st.session_state.template_nav_category = None
                        st.session_state.template_nav_subdivision = None
                        st.rerun()
                    elif i == 1:
                        # Go to subdivisions
                        st.session_state.template_nav_level = "subdivisions"
                        st.session_state.template_nav_subdivision = None
                        st.rerun()
        
        # Add separator
        if i < len(breadcrumb_parts) - 1:
            with cols[col_idx + 1]:
                st.markdown("›")


def render_level1_categories(all_templates: List):
    """Render Level 1: Main category cards"""
    st.markdown("#### 🎯 Choose Your Goal Category")
    st.caption("Select a category to explore specific goal templates")
    
    # Count templates
    counts = count_templates_by_category(all_templates)
    
    # Render cards using columns for better control
    cols = st.columns(5)
    
    for idx, (category_key, category_data) in enumerate(CATEGORY_METADATA.items()):
        with cols[idx]:
            card_html = f"""
            <div class="category-card {category_data['color_class']}">
                <span class="category-icon">{category_data['icon']}</span>
                <div class="category-name">{category_data['name']}</div>
                <div class="category-count">{counts.get(category_key, 0)} templates</div>
                <div class="category-description">{category_data['description']}</div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
            # Button to navigate
            if st.button("Explore", key=f"cat_{category_key}", use_container_width=True):
                st.session_state.template_nav_level = "subdivisions"
                st.session_state.template_nav_category = category_key
                st.rerun()


def render_level2_subdivisions(all_templates: List, category: str):
    """Render Level 2: Subdivision cards for selected category"""
    cat_meta = CATEGORY_METADATA.get(category, {})
    
    # Back button
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("← Back", key="back_to_categories"):
            st.session_state.template_nav_level = "categories"
            st.session_state.template_nav_category = None
            st.rerun()
    
    # Header
    st.markdown(f"#### {cat_meta.get('icon', '')} {cat_meta.get('name', category)}")
    st.caption(f"{cat_meta.get('description', '')} - Select a focus area")
    
    # Breadcrumb
    render_breadcrumb("subdivisions", category)
    
    # Count templates per subdivision
    subdivision_counts = count_templates_by_subdivision(all_templates, category)
    
    # Get subdivisions for this category
    subdivisions = SUBDIVISION_DEFINITIONS.get(category, {})
    
    # Render subdivision cards
    if subdivisions:
        # Use columns for grid layout
        cols_per_row = 3
        subdivision_items = list(subdivisions.items())
        
        for i in range(0, len(subdivision_items), cols_per_row):
            cols = st.columns(cols_per_row)
            for j in range(cols_per_row):
                if i + j < len(subdivision_items):
                    subdivision_name, subdivision_data = subdivision_items[i + j]
                    count = subdivision_counts.get(subdivision_name, 0)
                    
                    with cols[j]:
                        card_html = f"""
                        <div class="subdivision-card" style="--accent-color: var(--card-color-1);">
                            <span class="subdivision-icon">{subdivision_data['icon']}</span>
                            <div class="subdivision-name">{subdivision_name}</div>
                            <div class="subdivision-count">{count} template{'s' if count != 1 else ''}</div>
                            <div class="subdivision-description">{subdivision_data['description']}</div>
                        </div>
                        """
                        st.markdown(card_html, unsafe_allow_html=True)
                        
                        # Button to navigate
                        if st.button("View Templates", key=f"sub_{category}_{subdivision_name}", use_container_width=True):
                            st.session_state.template_nav_level = "templates"
                            st.session_state.template_nav_subdivision = subdivision_name
                            st.rerun()
    else:
        st.info("No subdivisions defined for this category yet.")


def render_level3_templates(all_templates: List, category: str, subdivision: str):
    """Render Level 3: Template cards for selected subdivision"""
    cat_meta = CATEGORY_METADATA.get(category, {})
    
    # Back button
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("← Back", key="back_to_subdivisions"):
            st.session_state.template_nav_level = "subdivisions"
            st.session_state.template_nav_subdivision = None
            st.rerun()
    
    # Header
    subdivision_data = SUBDIVISION_DEFINITIONS.get(category, {}).get(subdivision, {})
    st.markdown(f"#### {subdivision_data.get('icon', '📁')} {subdivision}")
    st.caption(f"{subdivision_data.get('description', '')} - Select a template to customize")
    
    # Breadcrumb
    render_breadcrumb("templates", category, subdivision)
    
    # Get templates
    templates = get_templates_for_subdivision(all_templates, category, subdivision)
    
    if not templates:
        st.info(f"No templates found in {subdivision}. Try another subdivision or use the search feature.")
        return
    
    st.caption(f"Showing {len(templates)} template{'s' if len(templates) != 1 else ''}")
    
    # Render template cards
    cols_per_row = 3
    for i in range(0, len(templates), cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            if i + j < len(templates):
                template = templates[i + j]
                
                with cols[j]:
                    # Difficulty badge
                    difficulty_class = {
                        "Beginner": "difficulty-beginner",
                        "Intermediate": "difficulty-intermediate",
                        "Advanced": "difficulty-advanced"
                    }.get(template.difficulty, "difficulty-intermediate")
                    
                    difficulty_emoji = {
                        "Beginner": "🟢",
                        "Intermediate": "🟡",
                        "Advanced": "🔴"
                    }.get(template.difficulty, "⚪")
                    
                    # Build card HTML
                    card_html = f"""
                    <div class="template-card">
                        <div class="template-header">
                            <div class="template-name">{template.name}</div>
                        </div>
                        <div class="template-description">{template.description}</div>
                        <div class="template-metadata">
                            <div class="template-meta-item">⏱️ {template.timeframe} days</div>
                            <div class="template-meta-item">⏰ {template.hours_per_day}h/day</div>
                            <div class="difficulty-badge {difficulty_class}">{difficulty_emoji} {template.difficulty}</div>
                        </div>
                    """
                    
                    # Add tags (max 3)
                    if template.tags:
                        card_html += '<div class="template-tags">'
                        for tag in template.tags[:3]:
                            card_html += f'<span class="tag-pill">{tag}</span>'
                        if len(template.tags) > 3:
                            card_html += f'<span class="tag-pill">+{len(template.tags) - 3} more</span>'
                        card_html += '</div>'
                    
                    card_html += """
                    </div>
                    """
                    
                    st.markdown(card_html, unsafe_allow_html=True)
                    
                    # Select button
                    if st.button("Select Template", key=f"select_template_{template.name}_{i}_{j}", use_container_width=True):
                        st.session_state.selected_template = template
                        st.session_state.template_conversation_step = 1
                        st.rerun()


# ============================================================================
# MAIN TEMPLATE SELECTOR FUNCTION
# ============================================================================

def render_template_selector_redesign(generator):
    """Main function to render the new card-based template selector"""
    from utils.templates import get_all_templates
    
    # Inject CSS
    inject_card_styles()
    
    # Initialize navigation state
    if 'template_nav_level' not in st.session_state:
        st.session_state.template_nav_level = "categories"
    if 'template_nav_category' not in st.session_state:
        st.session_state.template_nav_category = None
    if 'template_nav_subdivision' not in st.session_state:
        st.session_state.template_nav_subdivision = None
    
    # Get all templates
    all_templates = get_all_templates()
    
    # Render appropriate level based on navigation state
    level = st.session_state.template_nav_level
    category = st.session_state.template_nav_category
    subdivision = st.session_state.template_nav_subdivision
    
    if level == "categories":
        render_level1_categories(all_templates)
    elif level == "subdivisions" and category:
        render_level2_subdivisions(all_templates, category)
    elif level == "templates" and category and subdivision:
        render_level3_templates(all_templates, category, subdivision)
    else:
        # Fallback to categories
        st.session_state.template_nav_level = "categories"
        render_level1_categories(all_templates)
