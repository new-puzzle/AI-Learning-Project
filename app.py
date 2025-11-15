"""
LearnPath AI - AI-Powered Learning Path Planner
Main Streamlit Application
"""

import streamlit as st
import os
from dotenv import load_dotenv
from datetime import datetime
from utils.path_generator import LearningPathGenerator

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="LearnPath AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .topic-card {
        background-color: #f5f5f5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1E88E5;
        margin-bottom: 1rem;
    }
    .completed-topic {
        background-color: #e8f5e9;
        border-left: 4px solid #4CAF50;
    }
    .stat-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    .resource-link {
        color: #1E88E5;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)


def init_session_state():
    """Initialize session state variables"""
    if 'current_path_id' not in st.session_state:
        st.session_state.current_path_id = None
    if 'show_generator' not in st.session_state:
        st.session_state.show_generator = True
    if 'generated_path' not in st.session_state:
        st.session_state.generated_path = None


def check_api_key():
    """Check if API key is configured"""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        st.error("⚠️ Anthropic API Key not configured!")
        st.info("""
        **To use LearnPath AI:**
        1. Copy `.env.example` to `.env`
        2. Add your Anthropic API key to the `.env` file
        3. Get your API key from: https://console.anthropic.com/
        4. Restart the application
        """)
        return False
    return True


def render_header():
    """Render the application header"""
    st.markdown('<p class="main-header">🎓 LearnPath AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI-Powered Learning Path Planner & Progress Tracker</p>', unsafe_allow_html=True)


def render_learning_path_generator(generator):
    """Render the learning path generator form"""
    st.markdown("### 🚀 Create Your Learning Path")

    col1, col2 = st.columns([2, 1])

    with col1:
        goal = st.text_input(
            "What do you want to learn?",
            placeholder="e.g., Learn Python programming, Master Machine Learning, Become a Web Developer",
            help="Enter your learning goal in a clear, specific way"
        )

    with col2:
        timeframe = st.number_input(
            "Timeframe (days)",
            min_value=1,
            max_value=365,
            value=30,
            help="How many days do you want to dedicate to this goal?"
        )

    if st.button("Generate Learning Path", type="primary", use_container_width=True):
        if not goal:
            st.error("Please enter a learning goal!")
            return

        with st.spinner("🤖 AI is creating your personalized learning path..."):
            try:
                # Generate learning path
                learning_path = generator.create_learning_path(goal, timeframe)

                # Store in session state
                st.session_state.generated_path = learning_path
                st.session_state.current_path_id = learning_path['path_id']
                st.session_state.show_generator = False

                st.success("✅ Learning path generated successfully!")
                st.rerun()

            except Exception as e:
                st.error(f"Error generating learning path: {str(e)}")


def render_learning_path(path_data):
    """Render the complete learning path"""
    st.markdown("### 📚 Your Learning Path")

    # Overview section
    if 'overview' in path_data:
        st.info(f"**Overview:** {path_data['overview']}")

    # Milestones
    if 'milestones' in path_data and path_data['milestones']:
        st.markdown("#### 🎯 Key Milestones")
        cols = st.columns(len(path_data['milestones']))
        for idx, milestone in enumerate(path_data['milestones']):
            with cols[idx]:
                st.markdown(f"**{idx + 1}.** {milestone}")

    # Curriculum
    st.markdown("#### 📖 Daily Curriculum")

    curriculum = path_data.get('curriculum', [])

    for topic in curriculum:
        day_num = topic.get('day', 0)
        topic_name = topic.get('topic', '')
        subtopics = topic.get('subtopics', [])
        estimated_hours = topic.get('estimated_hours', 0)
        resources = topic.get('resources', [])

        with st.expander(f"📅 Day {day_num}: {topic_name}", expanded=(day_num == 1)):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"**Topic:** {topic_name}")

                if subtopics:
                    st.markdown("**Subtopics:**")
                    for subtopic in subtopics:
                        st.markdown(f"- {subtopic}")

            with col2:
                st.metric("Estimated Time", f"{estimated_hours} hours")

            # Resources
            if resources:
                st.markdown("**📚 Recommended Resources:**")
                for resource in resources:
                    resource_type = resource.get('type', 'resource')
                    resource_name = resource.get('name', 'Resource')
                    resource_url = resource.get('url', '#')

                    icon = {
                        'course': '🎓',
                        'article': '📄',
                        'video': '🎥',
                        'book': '📖'
                    }.get(resource_type, '🔗')

                    st.markdown(f"{icon} [{resource_name}]({resource_url})")


def render_saved_paths(generator):
    """Render list of saved learning paths"""
    st.markdown("### 📋 My Learning Paths")

    paths = generator.get_all_paths()

    if not paths:
        st.info("No learning paths yet. Create your first one above!")
        return

    for path in paths:
        path_id = path['id']
        goal = path['goal']
        timeframe = path['timeframe']
        created_at = path['created_at']

        # Get progress stats
        stats = generator.get_progress_stats(path_id)
        progress = stats['progress_percentage']

        col1, col2, col3 = st.columns([3, 1, 1])

        with col1:
            st.markdown(f"**{goal}**")
            st.caption(f"Created: {created_at[:10]} | {timeframe} days")

        with col2:
            st.progress(progress / 100)
            st.caption(f"{progress:.0f}% complete")

        with col3:
            if st.button("View", key=f"view_{path_id}"):
                st.session_state.current_path_id = path_id
                st.session_state.show_generator = False
                st.rerun()


def render_progress_tracker(generator, path_id):
    """Render progress tracking interface"""
    path_data = generator.get_learning_path(path_id)

    if not path_data:
        st.error("Learning path not found!")
        return

    path_info = path_data['path_info']
    curriculum = path_data['curriculum']
    stats = path_data['stats']

    # Header with back button
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"### 📚 {path_info['goal']}")
    with col2:
        if st.button("← Back"):
            st.session_state.show_generator = True
            st.session_state.current_path_id = None
            st.rerun()

    # Progress stats
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="stat-box">', unsafe_allow_html=True)
        st.metric("Progress", f"{stats['progress_percentage']:.0f}%")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="stat-box">', unsafe_allow_html=True)
        st.metric("Completed", f"{stats['completed_topics']}/{stats['total_topics']}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="stat-box">', unsafe_allow_html=True)
        st.metric("Time Spent", f"{stats['total_time_spent_hours']} hrs")
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        streak = generator.get_learning_streak(path_id)
        st.markdown('<div class="stat-box">', unsafe_allow_html=True)
        st.metric("Learning Days", streak)
        st.markdown('</div>', unsafe_allow_html=True)

    # Progress bar
    st.progress(stats['progress_percentage'] / 100)

    st.markdown("---")

    # Curriculum with checkboxes
    st.markdown("#### 📖 Your Curriculum")

    for topic in curriculum:
        topic_id = topic['id']
        day_num = topic['day']
        topic_name = topic['topic']
        subtopics = topic['subtopics']
        estimated_hours = topic['estimated_hours']
        resources = topic['resources']
        is_completed = topic['is_completed']

        # Topic card
        card_class = "completed-topic" if is_completed else ""

        with st.container():
            col1, col2 = st.columns([1, 20])

            with col1:
                # Checkbox for completion
                completed = st.checkbox(
                    f"Mark {topic_name} as complete",
                    value=is_completed,
                    key=f"topic_{topic_id}",
                    label_visibility="collapsed"
                )

                # Update if changed
                if completed != is_completed:
                    generator.update_progress(topic_id, completed, 0)
                    st.rerun()

            with col2:
                with st.expander(f"{'✅' if is_completed else '⭐'} Day {day_num}: {topic_name}", expanded=not is_completed):
                    st.markdown(f"**Estimated Time:** {estimated_hours} hours")

                    if subtopics:
                        st.markdown("**What you'll learn:**")
                        for subtopic in subtopics:
                            st.markdown(f"- {subtopic}")

                    if resources:
                        st.markdown("**📚 Resources:**")
                        for resource in resources:
                            resource_type = resource.get('type', 'resource')
                            resource_name = resource.get('name', 'Resource')
                            resource_url = resource.get('url', '#')

                            icon = {
                                'course': '🎓',
                                'article': '📄',
                                'video': '🎥',
                                'book': '📖'
                            }.get(resource_type, '🔗')

                            st.markdown(f"{icon} [{resource_name}]({resource_url})")

        st.markdown("<br>", unsafe_allow_html=True)


def main():
    """Main application"""
    init_session_state()
    render_header()

    # Check API key
    if not check_api_key():
        return

    try:
        # Initialize generator
        generator = LearningPathGenerator()

        # Sidebar
        with st.sidebar:
            st.markdown("### 🎯 Navigation")

            if st.button("➕ New Learning Path", use_container_width=True):
                st.session_state.show_generator = True
                st.session_state.current_path_id = None
                st.rerun()

            st.markdown("---")
            render_saved_paths(generator)

            st.markdown("---")
            st.markdown("### ℹ️ About")
            st.caption("LearnPath AI helps you create structured learning paths with AI-powered curriculum generation and progress tracking.")

        # Main content
        if st.session_state.current_path_id:
            # Show progress tracker
            render_progress_tracker(generator, st.session_state.current_path_id)
        elif st.session_state.show_generator:
            # Show generator form
            render_learning_path_generator(generator)

            # Show recently generated path
            if st.session_state.generated_path:
                st.markdown("---")
                render_learning_path(st.session_state.generated_path)
        else:
            st.info("Select a learning path from the sidebar or create a new one!")

    except Exception as e:
        st.error(f"Application error: {str(e)}")
        st.info("Please check your configuration and try again.")


if __name__ == "__main__":
    main()
