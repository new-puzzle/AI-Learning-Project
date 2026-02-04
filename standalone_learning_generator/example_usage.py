"""
Example Usage of Learning Path Generator

This file demonstrates how to use the standalone learning path generator
in different scenarios.
"""

from generator import LearningPathGenerator
from ai_chat import AIChatAssistant
from datetime import date

# Initialize generator
# Option 1: Pass API key directly
generator = LearningPathGenerator(api_key="your-anthropic-api-key")

# Option 2: Use environment variable
# export ANTHROPIC_API_KEY="your-key"
# generator = LearningPathGenerator()

# Option 3: Use Streamlit secrets (if using Streamlit)
# generator = LearningPathGenerator()  # Will auto-detect from st.secrets


# ============================================================================
# Example 1: Basic Learning Path
# ============================================================================
def example_basic():
    """Generate a basic learning path"""
    print("Example 1: Basic Learning Path")
    print("-" * 50)
    
    path = generator.generate_learning_path(
        topic="prompt engineering",
        timeframe=30,
        hours_per_day=2.0
    )
    
    print(f"Overview: {path['overview']}")
    print(f"Total days: {len(path['curriculum'])}")
    print(f"First day topic: {path['curriculum'][0]['topic']}")
    print()


# ============================================================================
# Example 2: Weekend Learner
# ============================================================================
def example_weekend_learner():
    """Generate path for someone who only learns on weekends"""
    print("Example 2: Weekend Learner")
    print("-" * 50)
    
    path = generator.generate_learning_path(
        topic="n8n automation",
        timeframe=60,  # 2 months
        hours_per_day=4.0,  # 4 hours on weekends
        start_date="2025-01-04",  # Start on Saturday
        skip_weekdays=[0, 1, 2, 3, 4],  # Skip Mon-Fri (only weekends)
        proficiency="Intermediate"
    )
    
    print(f"Overview: {path['overview']}")
    print(f"Total curriculum days: {len(path['curriculum'])}")
    print()


# ============================================================================
# Example 3: Weekday Evening Learner
# ============================================================================
def example_weekday_evening():
    """Generate path for weekday evening learning"""
    print("Example 3: Weekday Evening Learner")
    print("-" * 50)
    
    path = generator.generate_learning_path(
        topic="Python for data science",
        timeframe=45,
        hours_per_day=1.5,  # 1.5 hours after work
        start_date="2025-01-06",  # Start on Monday
        skip_weekends=True,  # Only weekdays
        unavailable_dates_input="Dec 24-26, Jan 1",  # Skip holidays
        proficiency="Beginner"
    )
    
    print(f"Overview: {path['overview']}")
    print(f"First milestone: {path['milestones'][0]}")
    print()


# ============================================================================
# Example 4: With Focus Areas
# ============================================================================
def example_with_focus_areas():
    """Generate path with specific focus areas"""
    print("Example 4: With Focus Areas")
    print("-" * 50)
    
    path = generator.generate_learning_path(
        topic="prompt engineering",
        timeframe=30,
        hours_per_day=2.0,
        proficiency="Advanced",
        focus_areas=[
            "Advanced prompt techniques",
            "API integration",
            "Workflow automation",
            "Error handling"
        ],
        additional_requests="Focus on practical projects and real-world applications"
    )
    
    print(f"Overview: {path['overview']}")
    print(f"Focus areas: {path['metadata']['focus_areas']}")
    print()


# ============================================================================
# Example 5: Flexible Schedule
# ============================================================================
def example_flexible_schedule():
    """Generate path with flexible scheduling"""
    print("Example 5: Flexible Schedule")
    print("-" * 50)
    
    path = generator.generate_learning_path(
        topic="React development",
        timeframe=60,
        hours_per_day=3.0,
        start_date="2025-01-01",
        skip_weekdays=[2, 4],  # Skip Wednesdays and Fridays
        unavailable_dates_input="Nov 20-22, Dec 25",  # Skip specific dates
        proficiency="Intermediate"
    )
    
    print(f"Overview: {path['overview']}")
    # Show first few days with dates
    for day in path['curriculum'][:3]:
        if 'due_date' in day:
            print(f"Day {day['day']}: {day['topic']} (Due: {day['due_date']})")
    print()


# ============================================================================
# Example 6: AI Chat Assistant - Get Learning Suggestions
# ============================================================================
def example_ai_chat():
    """Use AI chat to get suggestions on what to learn"""
    print("Example 6: AI Chat Assistant")
    print("-" * 50)
    
    # Initialize chat assistant
    assistant = AIChatAssistant()
    
    # Ask for learning suggestions
    print("\n1. Getting learning path suggestions:")
    response = assistant.suggest_learning_path(
        goal="become proficient in prompt engineering",
        current_skills="I know Python and basic AI concepts"
    )
    print(f"AI: {response}\n")
    
    # Compare topics
    print("2. Comparing two topics:")
    response = assistant.compare_topics(
        topic1="prompt engineering",
        topic2="n8n automation",
        context="I want to work in AI automation"
    )
    print(f"AI: {response}\n")
    
    # Regular chat
    print("3. Regular chat:")
    response = assistant.chat("What skills are most important for a data scientist?")
    print(f"AI: {response}\n")


# ============================================================================
# Example 7: Using with Streamlit
# ============================================================================
def example_streamlit():
    """Example of using with Streamlit"""
    print("Example 6: Streamlit Integration")
    print("-" * 50)
    print("""
    import streamlit as st
    from generator import LearningPathGenerator
    from input_form import render_learning_input_form
    
    st.title("Learning Path Generator")
    
    # Initialize generator
    generator = LearningPathGenerator()
    
    # Render input form
    form_data = render_learning_input_form()
    
    if form_data:
        with st.spinner("Generating your learning path..."):
            path = generator.generate_learning_path(**form_data)
        
        st.success("Learning path generated!")
        st.json(path)
    """)


# ============================================================================
# Main
# ============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("Learning Path Generator - Examples")
    print("=" * 70)
    print()
    
    # Uncomment the example you want to run:
    # example_basic()
    # example_weekend_learner()
    # example_weekday_evening()
    # example_with_focus_areas()
    # example_flexible_schedule()
    # example_ai_chat()
    # example_streamlit()
    
    print("\nNote: Uncomment examples in the code to run them.")
    print("Make sure to set your ANTHROPIC_API_KEY before running!")

