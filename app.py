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

    # Status filter
    status_filter = st.selectbox(
        "Filter by status:",
        ["All", "Active", "On Hold", "Archived"],
        key="status_filter"
    )

    # Map filter to database values
    status_map = {
        "All": None,
        "Active": "active",
        "On Hold": "on_hold",
        "Archived": "archived"
    }

    paths = generator.get_paths_by_status(status_map[status_filter])

    if not paths:
        st.info("No learning paths yet. Create your first one above!")
        return

    for path in paths:
        path_id = path['id']
        goal = path['goal']
        timeframe = path['timeframe']
        created_at = path['created_at']
        status = path.get('status', 'active')

        # Get progress stats
        stats = generator.get_progress_stats(path_id)
        progress = stats['progress_percentage']

        # Status badge
        status_colors = {
            'active': '🟢',
            'on_hold': '🟡',
            'archived': '⚪',
            'deleted': '🔴'
        }
        status_icon = status_colors.get(status, '🟢')

        col1, col2, col3 = st.columns([3, 1, 1])

        with col1:
            st.markdown(f"{status_icon} **{goal}**")
            st.caption(f"Created: {created_at[:10]} | {timeframe} days | Status: {status.replace('_', ' ').title()}")

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

    # Header with back button and status controls
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.markdown(f"### 📚 {path_info['goal']}")
    with col2:
        # Status management
        current_status = path_info.get('status', 'active')
        new_status = st.selectbox(
            "Status",
            ["active", "on_hold", "archived"],
            index=["active", "on_hold", "archived"].index(current_status),
            key=f"status_select_{path_id}",
            label_visibility="collapsed"
        )
        if new_status != current_status:
            generator.update_path_status(path_id, new_status)
            st.success(f"Status updated to: {new_status.replace('_', ' ').title()}")
            st.rerun()
    with col3:
        if st.button("← Back"):
            st.session_state.show_generator = True
            st.session_state.current_path_id = None
            st.rerun()

    # Delete confirmation
    with st.expander("⚙️ Advanced Options"):
        st.warning("Danger Zone")
        if st.button("🗑️ Delete this learning path", key=f"delete_{path_id}"):
            if st.session_state.get(f"confirm_delete_{path_id}", False):
                generator.update_path_status(path_id, 'deleted')
                st.success("Learning path deleted!")
                st.session_state.show_generator = True
                st.session_state.current_path_id = None
                st.rerun()
            else:
                st.session_state[f"confirm_delete_{path_id}"] = True
                st.error("Click again to confirm deletion")

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

    # Tabs for Curriculum and AI Tutor
    tab1, tab2 = st.tabs(["📖 Curriculum", "🤖 AI Tutor"])

    with tab1:
        # Curriculum with checkboxes
        st.markdown("#### 📖 Your Learning Curriculum")

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

    with tab2:
        # AI Tutor Chat Interface
        st.markdown("#### 🤖 AI Learning Tutor")
        st.caption("Ask questions, upload images/files, and get personalized explanations from multiple AI models")

        # Initialize chat history in session state
        if f'chat_history_{path_id}' not in st.session_state:
            st.session_state[f'chat_history_{path_id}'] = []

        # Get available models
        available_models = generator.get_available_models()

        # Build model options with provider grouping
        model_options = []
        for provider_name, provider_data in available_models.items():
            configured_status = "✓" if provider_data['configured'] else "⚠️"
            vision_status = "👁️" if provider_data['supports_vision'] else ""
            for model in provider_data['models']:
                model_options.append(f"{configured_status} {vision_status} {provider_name} / {model}")

        # Model selector
        st.markdown("**Select AI Model:** (✓ = configured, ⚠️ = not configured, 👁️ = supports images)")
        model_choice = st.selectbox(
            "Model",
            model_options,
            key=f"model_selector_{path_id}",
            label_visibility="collapsed",
            help="Configure API keys in .env file to enable all models"
        )

        # File upload
        st.markdown("**Upload Image or File (optional):**")
        uploaded_file = st.file_uploader(
            "Upload file",
            type=["png", "jpg", "jpeg", "pdf", "txt", "docx"],
            key=f"file_upload_{path_id}",
            label_visibility="collapsed",
            help="Upload images, PDFs, or documents for the AI to analyze"
        )

        # Context about current learning path
        current_context = f"Learning Goal: {path_info['goal']}\nTopics covered: " + ", ".join([t['topic'] for t in curriculum[:5]])

        # Display chat history
        for i, message in enumerate(st.session_state[f'chat_history_{path_id}']):
            if message['role'] == 'user':
                st.markdown(f"**You:** {message['content']}")
            else:
                model_used = message.get('model', 'Claude Sonnet 4.5')
                st.markdown(f"**AI Tutor ({model_used}):** {message['content']}")
            st.markdown("---")

        # Chat input
        user_question = st.text_area(
            "Ask a question about your learning topics:",
            placeholder="e.g., Can you explain prompt engineering in simple terms?\nWhat's the difference between zero-shot and few-shot prompting?",
            height=100,
            key=f"chat_input_{path_id}"
        )

        col1, col2 = st.columns([1, 5])
        with col1:
            if st.button("Ask Tutor", type="primary"):
                if user_question.strip() or uploaded_file:
                    # Clean up model choice (remove status icons)
                    clean_model = model_choice
                    for icon in ["✓", "⚠️", "👁️", " "]:
                        clean_model = clean_model.replace(icon, "")
                    clean_model = clean_model.strip()

                    # Prepare user message
                    user_msg = user_question if user_question.strip() else "(Analyzing uploaded file)"
                    if uploaded_file:
                        user_msg += f"\n📎 Uploaded: {uploaded_file.name}"

                    # Add user message to history
                    st.session_state[f'chat_history_{path_id}'].append({
                        'role': 'user',
                        'content': user_msg
                    })

                    # Get AI response
                    with st.spinner(f"AI Tutor ({clean_model}) is thinking..."):
                        try:
                            if uploaded_file and uploaded_file.type.startswith('image/'):
                                # Image analysis
                                image_data = uploaded_file.read()
                                prompt = user_question if user_question.strip() else "Analyze this image and explain what you see. If it contains any problems or questions, solve them."
                                response = generator.analyze_uploaded_image(image_data, prompt, clean_model)
                            elif uploaded_file:
                                # Text file handling (PDF, TXT, DOCX)
                                file_content = ""
                                if uploaded_file.type == "application/pdf":
                                    try:
                                        import PyPDF2
                                        import io
                                        pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
                                        for page in pdf_reader.pages:
                                            file_content += page.extract_text()
                                    except:
                                        file_content = "(Could not extract PDF text)"
                                elif uploaded_file.type == "text/plain":
                                    file_content = uploaded_file.read().decode('utf-8')
                                elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                                    try:
                                        import docx
                                        import io
                                        doc = docx.Document(io.BytesIO(uploaded_file.read()))
                                        file_content = "\n".join([para.text for para in doc.paragraphs])
                                    except:
                                        file_content = "(Could not extract document text)"

                                full_question = f"Based on this document:\n\n{file_content[:2000]}...\n\n{user_question}"
                                response = generator.get_assistance(full_question, current_context, clean_model)
                            else:
                                # Regular text question
                                response = generator.get_assistance(user_question, current_context, clean_model)

                            # Add AI response to history with model info
                            st.session_state[f'chat_history_{path_id}'].append({
                                'role': 'assistant',
                                'content': response,
                                'model': clean_model
                            })

                            st.rerun()
                        except Exception as e:
                            st.error(f"Error: {str(e)}\n\nMake sure the API key for this provider is configured in your .env file.")
                else:
                    st.warning("Please enter a question or upload a file")

        with col2:
            if st.button("Clear Chat History"):
                st.session_state[f'chat_history_{path_id}'] = []
                st.rerun()

        # Quick question suggestions
        st.markdown("**💡 Quick Question Suggestions:**")
        suggestions_col1, suggestions_col2 = st.columns(2)

        with suggestions_col1:
            if st.button("Explain this topic simply", key=f"suggest1_{path_id}"):
                st.session_state[f'suggested_question_{path_id}'] = "Can you explain the current topic in simple terms with examples?"

            if st.button("Give me practice problems", key=f"suggest2_{path_id}"):
                st.session_state[f'suggested_question_{path_id}'] = "Can you give me some practice problems for this topic?"

        with suggestions_col2:
            if st.button("What are common mistakes?", key=f"suggest3_{path_id}"):
                st.session_state[f'suggested_question_{path_id}'] = "What are common mistakes beginners make with this topic?"

            if st.button("How does this apply in real-world?", key=f"suggest4_{path_id}"):
                st.session_state[f'suggested_question_{path_id}'] = "How is this used in real-world applications?"


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
