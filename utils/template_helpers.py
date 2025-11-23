"""
Helper functions for generating intelligent subdivisions/focus areas for templates
"""

from typing import List, Dict


def generate_intelligent_subdivisions(template: Dict, proficiency: str = None) -> List[str]:
    """
    Generate intelligent subdivisions/focus areas based on goal type, name, and description.
    Returns 3-4 meaningful options that are level-appropriate but flexible.
    
    Args:
        template: Template dictionary with name, goal_type, description, difficulty, etc.
        proficiency: User's proficiency level (Beginner, Intermediate, Expert)
    
    Returns:
        List of 3-4 subdivision strings
    """
    goal_type = template.get('goal_type', 'learning')
    name = template.get('name', '')
    description = template.get('description', '')
    difficulty = template.get('difficulty', 'Intermediate')
    subdivision_category = template.get('subdivision_category', '')
    
    # Use provided proficiency or fall back to template difficulty
    level = proficiency or difficulty
    
    subdivisions = []
    
    # LEARNING GOALS - Topic-based focus areas
    if goal_type == 'learning':
        subdivisions = _generate_learning_subdivisions(name, description, subdivision_category, level)
    
    # PERSONAL GOALS - Aspect/component-based focus areas
    elif goal_type == 'personal':
        subdivisions = _generate_personal_subdivisions(name, description, subdivision_category, level)
    
    # CAREER GOALS - Skill/action-based focus areas
    elif goal_type == 'career':
        subdivisions = _generate_career_subdivisions(name, description, subdivision_category, level)
    
    # PROJECT GOALS - Phase/component-based focus areas
    elif goal_type == 'project':
        subdivisions = _generate_project_subdivisions(name, description, subdivision_category, level)
    
    # FREELANCE GOALS - Strategy/component-based focus areas
    elif goal_type == 'freelance':
        subdivisions = _generate_freelance_subdivisions(name, description, subdivision_category, level)
    
    # Fallback: parse description intelligently
    if not subdivisions or len(subdivisions) < 3:
        subdivisions = _parse_description_intelligently(description, name)
    
    # Ensure we have 3-4 items
    if len(subdivisions) > 4:
        subdivisions = subdivisions[:4]
    elif len(subdivisions) < 3:
        # Add generic fallbacks based on goal type
        fallbacks = {
            'learning': ['Core Concepts', 'Practical Applications', 'Advanced Topics'],
            'personal': ['Foundation', 'Practice', 'Mastery'],
            'career': ['Skills Development', 'Portfolio Building', 'Job Search'],
            'project': ['Planning', 'Development', 'Launch'],
            'freelance': ['Setup', 'Marketing', 'Client Acquisition']
        }
        while len(subdivisions) < 3:
            for fb in fallbacks.get(goal_type, ['Phase 1', 'Phase 2', 'Phase 3']):
                if fb not in subdivisions:
                    subdivisions.append(fb)
                    break
    
    return subdivisions[:4]


def _generate_learning_subdivisions(name: str, description: str, category: str, level: str) -> List[str]:
    """Generate subdivisions for learning goals - topic-based"""
    subdivisions = []
    name_lower = name.lower()
    desc_lower = description.lower()
    
    # STEM subjects
    if 'chemistry' in name_lower or 'chemistry' in desc_lower:
        if 'organic' in name_lower:
            if level == 'Beginner':
                subdivisions = ['Molecular Structure & Bonding', 'Nomenclature & Functional Groups', 
                              'Basic Reactions', 'Stereochemistry Basics']
            elif level == 'Intermediate':
                subdivisions = ['Reaction Mechanisms', 'Stereochemistry & Chirality', 
                              'Synthesis Strategies', 'Spectroscopy Analysis']
            else:  # Advanced
                subdivisions = ['Advanced Synthesis', 'Retrosynthetic Analysis', 
                              'Complex Mechanisms', 'Multi-step Synthesis']
        else:
            subdivisions = ['Atomic Structure', 'Chemical Bonding', 'Reactions & Equations', 'Lab Techniques']
    
    # Programming/Tech
    elif any(term in name_lower for term in ['python', 'javascript', 'java', 'programming', 'coding']):
        if level == 'Beginner':
            subdivisions = ['Syntax & Basics', 'Control Structures', 'Functions & Modules', 'Basic Projects']
        elif level == 'Intermediate':
            subdivisions = ['Data Structures', 'Object-Oriented Programming', 'APIs & Libraries', 'Real Projects']
        else:
            subdivisions = ['Advanced Patterns', 'Architecture & Design', 'Performance Optimization', 'Complex Systems']
    
    # AI/ML
    elif any(term in name_lower for term in ['ai', 'machine learning', 'deep learning', 'neural', 'prompt']):
        if level == 'Beginner':
            subdivisions = ['Fundamentals & Concepts', 'Basic Models', 'Practical Applications', 'Tools & Frameworks']
        elif level == 'Intermediate':
            subdivisions = ['Model Architecture', 'Training & Optimization', 'Real-world Projects', 'Advanced Techniques']
        else:
            subdivisions = ['Research & Innovation', 'Advanced Architectures', 'Production Systems', 'Cutting-edge Methods']
    
    # Data Science
    elif 'data science' in name_lower or 'data analysis' in name_lower:
        if level == 'Beginner':
            subdivisions = ['Data Basics & Cleaning', 'Basic Statistics', 'Simple Visualizations', 'Introduction to Tools']
        elif level == 'Intermediate':
            subdivisions = ['Data Wrangling & Transformation', 'Statistical Analysis', 'Advanced Visualization', 'Machine Learning Basics']
        else:
            subdivisions = ['Advanced Data Engineering', 'Statistical Modeling', 'Complex Visualizations', 'Advanced ML & Deep Learning']
    
    # Languages
    elif any(term in name_lower for term in ['language', 'spanish', 'french', 'german', 'japanese', 'chinese']):
        if level == 'Beginner':
            subdivisions = ['Basic Vocabulary & Phrases', 'Pronunciation Basics', 'Simple Conversations', 'Grammar Foundations']
        elif level == 'Intermediate':
            subdivisions = ['Grammar & Vocabulary Expansion', 'Speaking & Pronunciation', 'Reading & Writing', 'Cultural Context']
        else:
            subdivisions = ['Advanced Grammar & Idioms', 'Fluency & Nuance', 'Literature & Media', 'Cultural Mastery']
    
    # Business/Finance
    elif any(term in name_lower for term in ['business', 'finance', 'marketing', 'management']):
        if level == 'Beginner':
            subdivisions = ['Core Concepts & Fundamentals', 'Basic Principles', 'Introduction to Tools', 'Simple Case Studies']
        elif level == 'Intermediate':
            subdivisions = ['Core Concepts', 'Practical Strategies', 'Case Studies', 'Real-world Application']
        else:
            subdivisions = ['Advanced Strategies', 'Complex Case Analysis', 'Strategic Planning', 'Leadership & Innovation']
    
    # Arts/Creative
    elif any(term in name_lower for term in ['art', 'design', 'music', 'guitar', 'piano', 'drawing', 'photography']):
        if level == 'Beginner':
            subdivisions = ['Fundamentals & Basics', 'Basic Techniques', 'Simple Exercises', 'Getting Started']
        elif level == 'Intermediate':
            subdivisions = ['Fundamentals & Technique', 'Practice & Exercises', 'Creative Projects', 'Style Development']
        else:
            subdivisions = ['Advanced Techniques', 'Mastery & Refinement', 'Complex Projects', 'Personal Style & Innovation']
    
    return subdivisions


def _generate_personal_subdivisions(name: str, description: str, category: str, level: str) -> List[str]:
    """Generate subdivisions for personal goals - aspect-based"""
    subdivisions = []
    name_lower = name.lower()
    
    # Fitness/Health
    if 'fitness' in category.lower() or 'health' in category.lower() or any(term in name_lower for term in ['run', 'fitness', 'weight', 'muscle', 'yoga', 'gym']):
        if 'run' in name_lower or 'marathon' in name_lower or 'race' in name_lower:
            if level == 'Beginner':
                subdivisions = ['Basic Running Form', 'Starting Distance', 'Basic Nutrition', 'Injury Prevention Basics']
            elif level == 'Intermediate':
                subdivisions = ['Running Training', 'Nutrition & Hydration', 'Injury Prevention', 'Mental Preparation']
            else:
                subdivisions = ['Advanced Training Plans', 'Performance Nutrition', 'Advanced Injury Prevention', 'Mental Toughness']
        elif 'weight' in name_lower or 'lose' in name_lower or 'gain' in name_lower:
            if level == 'Beginner':
                subdivisions = ['Basic Nutrition', 'Simple Exercise Routine', 'Habit Formation', 'Basic Tracking']
            elif level == 'Intermediate':
                subdivisions = ['Nutrition Plan', 'Exercise Routine', 'Habit Formation', 'Progress Tracking']
            else:
                subdivisions = ['Advanced Nutrition Strategies', 'Optimized Training', 'Habit Mastery', 'Advanced Tracking & Analysis']
        elif 'yoga' in name_lower:
            if level == 'Beginner':
                subdivisions = ['Basic Poses', 'Breathing Basics', 'Introduction to Meditation', 'Getting Started']
            elif level == 'Intermediate':
                subdivisions = ['Asana Practice', 'Breathwork', 'Meditation', 'Lifestyle Integration']
            else:
                subdivisions = ['Advanced Asanas', 'Advanced Breathwork', 'Deep Meditation', 'Philosophy & Lifestyle']
        else:
            if level == 'Beginner':
                subdivisions = ['Basic Training Plan', 'Nutrition Basics', 'Recovery Basics', 'Building Consistency']
            elif level == 'Intermediate':
                subdivisions = ['Training Plan', 'Nutrition', 'Recovery', 'Consistency']
            else:
                subdivisions = ['Advanced Training', 'Optimized Nutrition', 'Advanced Recovery', 'Consistency Mastery']
    
    # Habits/Wellness
    elif 'habit' in category.lower() or 'wellness' in category.lower() or any(term in name_lower for term in ['habit', 'meditation', 'gratitude', 'sleep']):
        if level == 'Beginner':
            subdivisions = ['Habit Basics', 'Simple Tracking', 'Environment Basics', 'Getting Started']
        elif level == 'Intermediate':
            subdivisions = ['Habit Formation', 'Tracking & Accountability', 'Environment Setup', 'Consistency Strategies']
        else:
            subdivisions = ['Advanced Habit Systems', 'Advanced Tracking', 'Optimized Environment', 'Mastery & Refinement']
    
    # Creative Skills
    elif 'creative' in category.lower() or any(term in name_lower for term in ['guitar', 'piano', 'draw', 'paint', 'cook']):
        if level == 'Beginner':
            subdivisions = ['Fundamentals & Basics', 'Basic Practice', 'Simple Projects', 'Getting Started']
        elif level == 'Intermediate':
            subdivisions = ['Fundamentals & Technique', 'Regular Practice', 'Project Work', 'Skill Progression']
        else:
            subdivisions = ['Advanced Techniques', 'Mastery Practice', 'Complex Projects', 'Personal Style']
    
    # Relationships
    elif 'relationship' in category.lower() or any(term in name_lower for term in ['friend', 'parent', 'relationship', 'communication']):
        if level == 'Beginner':
            subdivisions = ['Basic Communication', 'Quality Time Basics', 'Understanding Basics', 'Getting Started']
        elif level == 'Intermediate':
            subdivisions = ['Communication Skills', 'Quality Time', 'Understanding & Empathy', 'Consistent Effort']
        else:
            subdivisions = ['Advanced Communication', 'Deep Connection', 'Empathy Mastery', 'Relationship Mastery']
    
    return subdivisions


def _generate_career_subdivisions(name: str, description: str, category: str, level: str) -> List[str]:
    """Generate subdivisions for career goals - skill/action-based"""
    subdivisions = []
    name_lower = name.lower()
    
    # Tech roles
    if 'tech' in category.lower() or any(term in name_lower for term in ['developer', 'engineer', 'programmer', 'data']):
        if level == 'Beginner':
            subdivisions = ['Basic Technical Skills', 'Simple Portfolio Projects', 'Interview Basics', 'Networking Basics']
        elif level == 'Intermediate':
            subdivisions = ['Technical Skills', 'Portfolio Projects', 'Interview Prep', 'Networking']
        else:
            subdivisions = ['Advanced Technical Skills', 'Complex Portfolio Projects', 'Advanced Interview Prep', 'Strategic Networking']
    
    # Business roles
    elif 'business' in category.lower() or any(term in name_lower for term in ['manager', 'consulting', 'analyst', 'product']):
        if level == 'Beginner':
            subdivisions = ['Core Skills Basics', 'Basic Case Studies', 'Networking Basics', 'Interview Preparation Basics']
        elif level == 'Intermediate':
            subdivisions = ['Core Skills', 'Case Studies', 'Networking', 'Interview Preparation']
        else:
            subdivisions = ['Advanced Skills', 'Complex Case Studies', 'Strategic Networking', 'Advanced Interview Prep']
    
    # Creative roles
    elif 'creative' in category.lower() or any(term in name_lower for term in ['designer', 'writer', 'artist']):
        if level == 'Beginner':
            subdivisions = ['Portfolio Basics', 'Skill Development Basics', 'Simple Client Work', 'Networking Basics']
        elif level == 'Intermediate':
            subdivisions = ['Portfolio Building', 'Skill Development', 'Client Work', 'Industry Networking']
        else:
            subdivisions = ['Advanced Portfolio', 'Skill Mastery', 'Complex Client Work', 'Strategic Networking']
    
    # General
    else:
        if level == 'Beginner':
            subdivisions = ['Skill Development Basics', 'Portfolio/Resume Basics', 'Networking Basics', 'Job Search Basics']
        elif level == 'Intermediate':
            subdivisions = ['Skill Development', 'Portfolio/Resume', 'Networking', 'Job Search Strategy']
        else:
            subdivisions = ['Advanced Skill Development', 'Advanced Portfolio/Resume', 'Strategic Networking', 'Advanced Job Search']
    
    return subdivisions


def _generate_project_subdivisions(name: str, description: str, category: str, level: str) -> List[str]:
    """Generate subdivisions for project goals - phase/component-based"""
    subdivisions = []
    name_lower = name.lower()
    
    # Tech projects
    if 'tech' in category.lower() or any(term in name_lower for term in ['app', 'website', 'saas', 'software', 'extension']):
        if level == 'Beginner':
            subdivisions = ['Basic Planning', 'Simple Development', 'Basic Testing', 'Simple Launch']
        elif level == 'Intermediate':
            subdivisions = ['Planning & Design', 'Development', 'Testing & Refinement', 'Launch & Marketing']
        else:
            subdivisions = ['Advanced Planning & Architecture', 'Advanced Development', 'Comprehensive Testing', 'Strategic Launch & Marketing']
    
    # Content projects
    elif any(term in name_lower for term in ['youtube', 'podcast', 'blog', 'newsletter', 'course']):
        if level == 'Beginner':
            subdivisions = ['Content Basics', 'Platform Setup Basics', 'Basic Marketing', 'Getting Started']
        elif level == 'Intermediate':
            subdivisions = ['Content Creation', 'Platform Setup', 'Marketing & Growth', 'Monetization']
        else:
            subdivisions = ['Advanced Content Strategy', 'Optimized Platform Setup', 'Advanced Marketing', 'Advanced Monetization']
    
    # Business projects
    elif any(term in name_lower for term in ['business', 'store', 'e-commerce', 'product']):
        if level == 'Beginner':
            subdivisions = ['Basic Planning', 'Simple Setup', 'Basic Marketing', 'Simple Launch']
        elif level == 'Intermediate':
            subdivisions = ['Planning & Research', 'Setup & Development', 'Marketing', 'Launch & Sales']
        else:
            subdivisions = ['Advanced Planning & Strategy', 'Advanced Setup', 'Strategic Marketing', 'Advanced Launch & Sales']
    
    # General
    else:
        if level == 'Beginner':
            subdivisions = ['Basic Planning', 'Simple Development', 'Basic Testing', 'Simple Launch']
        elif level == 'Intermediate':
            subdivisions = ['Planning', 'Development', 'Testing', 'Launch']
        else:
            subdivisions = ['Advanced Planning', 'Advanced Development', 'Comprehensive Testing', 'Strategic Launch']
    
    return subdivisions


def _generate_freelance_subdivisions(name: str, description: str, category: str, level: str) -> List[str]:
    """Generate subdivisions for freelance goals - strategy/component-based"""
    subdivisions = []
    name_lower = name.lower()
    
    # Platform-based
    if 'platform' in category.lower() or any(term in name_lower for term in ['fiverr', 'upwork', 'toptal', 'medium']):
        subdivisions = ['Profile Optimization', 'Portfolio Building', 'Client Acquisition', 'Service Delivery']
    
    # Consulting
    elif 'consulting' in category.lower() or 'consulting' in name_lower:
        subdivisions = ['Service Packages', 'Client Acquisition', 'Project Delivery', 'Business Growth']
    
    # Digital products
    elif 'digital' in category.lower() or any(term in name_lower for term in ['template', 'digital product', 'course']):
        subdivisions = ['Product Creation', 'Platform Setup', 'Marketing', 'Sales & Growth']
    
    # SaaS/Products
    elif 'saas' in category.lower() or 'saas' in name_lower:
        subdivisions = ['Product Development', 'Beta Testing', 'Marketing', 'Customer Acquisition']
    
    # General
    else:
        subdivisions = ['Business Setup', 'Marketing', 'Client Acquisition', 'Service Delivery']
    
    return subdivisions


def _parse_description_intelligently(description: str, name: str) -> List[str]:
    """Intelligently parse description to extract meaningful subdivisions"""
    if not description:
        return []
    
    # Split by common separators
    parts = []
    for separator in [', ', ' and ', ' & ', '; ']:
        if separator in description:
            parts = [p.strip() for p in description.split(separator)]
            break
    
    # Clean up parts
    cleaned = []
    for part in parts[:4]:  # Max 4
        part = part.strip()
        # Remove common prefixes/suffixes
        part = part.replace('Learn ', '').replace('Master ', '').replace('Build ', '')
        part = part.replace(' basics', '').replace(' fundamentals', '')
        if part and len(part) > 3:
            cleaned.append(part.title())
    
    return cleaned if cleaned else []

