"""
GoalPath AI - Universal Goal Planning Platform
Main Streamlit Application
"""

import streamlit as st
import os
from dotenv import load_dotenv
from datetime import datetime
from utils.path_generator import LearningPathGenerator
from utils.auth import init_cookie_manager, check_password, render_login_screen, logout

# Load environment variables
load_dotenv()

# Initialize cookie manager for authentication
cookies = init_cookie_manager()

# Check authentication before showing app
if not check_password(cookies):
    render_login_screen(cookies)
    st.stop()

# Page configuration
st.set_page_config(
    page_title="GoalPath AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add viewport meta tag for mobile optimization
st.markdown("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
""", unsafe_allow_html=True)

# Custom CSS for better styling and mobile optimization
st.markdown("""
    <style>
    /* === GLOBAL MOBILE FIXES === */
    * {
        -webkit-tap-highlight-color: rgba(0,0,0,0.1);
        -webkit-overflow-scrolling: touch;
    }

    /* Prevent horizontal scroll */
    body {
        overflow-x: hidden;
    }

    .main .block-container {
        max-width: 100%;
        overflow-x: hidden;
    }

    /* === DESKTOP STYLES === */
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
        margin-bottom: 0.5rem;
    }
    .resource-link {
        color: #1E88E5;
        text-decoration: none;
    }

    /* === MOBILE OPTIMIZATION (TABLETS & PHONES) === */
    @media only screen and (max-width: 768px) {
        /* Headers */
        .main-header {
            font-size: 2rem;
            margin-bottom: 0.3rem;
            padding: 0 0.5rem;
        }
        .sub-header {
            font-size: 1rem;
            margin-bottom: 1rem;
            padding: 0 0.5rem;
        }

        /* Cards and containers */
        .topic-card {
            padding: 0.75rem;
            margin-bottom: 0.75rem;
        }
        .stat-box {
            padding: 0.75rem;
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }

        /* Buttons - Touch friendly (44px minimum) */
        .stButton > button {
            min-height: 48px !important;
            font-size: 1rem !important;
            padding: 12px 24px !important;
            width: 100%;
            margin-bottom: 0.5rem;
        }

        /* Form inputs - Prevent zoom on iOS */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select,
        .stNumberInput > div > div > input {
            font-size: 16px !important;
            min-height: 48px !important;
            padding: 12px !important;
        }

        /* Spacing */
        .block-container {
            padding: 1rem 0.75rem !important;
            max-width: 100% !important;
        }

        /* File uploader */
        .stFileUploader {
            font-size: 0.95rem;
        }
        .stFileUploader > div {
            padding: 1rem !important;
        }

        /* YouTube embeds - Responsive */
        iframe {
            max-width: 100% !important;
            height: auto;
            aspect-ratio: 16/9;
        }

        /* Expanders - Better spacing */
        .streamlit-expanderHeader {
            font-size: 1rem !important;
            padding: 0.75rem !important;
        }
        .streamlit-expanderContent {
            padding: 0.75rem !important;
        }

        /* Tabs - Mobile friendly */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.5rem;
        }
        .stTabs [data-baseweb="tab"] {
            padding: 12px 16px !important;
            font-size: 1rem !important;
        }

        /* Progress bars */
        .stProgress > div > div {
            height: 8px;
        }

        /* Columns - Stack on mobile */
        [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }

        /* Metrics - Better mobile display */
        [data-testid="stMetricValue"] {
            font-size: 1.5rem !important;
        }
        [data-testid="stMetricLabel"] {
            font-size: 0.9rem !important;
        }

        /* Chat/AI Tutor */
        .stChatMessage {
            padding: 0.75rem !important;
        }

        /* Sidebar - Better mobile */
        section[data-testid="stSidebar"] {
            min-width: 260px !important;
        }

        /* Prevent text overflow */
        p, span, div {
            word-wrap: break-word;
            overflow-wrap: break-word;
        }

        /* Better link spacing */
        a {
            padding: 4px 0;
            display: inline-block;
        }
    }

    /* === EXTRA SMALL DEVICES (PHONES) === */
    @media only screen and (max-width: 480px) {
        .main-header {
            font-size: 1.75rem;
            line-height: 1.2;
        }
        .sub-header {
            font-size: 0.95rem;
            line-height: 1.3;
        }

        /* Even more compact */
        .block-container {
            padding: 0.75rem 0.5rem !important;
        }

        /* Smaller stat boxes */
        .stat-box {
            padding: 0.5rem;
            font-size: 0.85rem;
        }

        /* Compact buttons */
        .stButton > button {
            padding: 10px 16px !important;
            font-size: 0.95rem !important;
        }

        /* Reduce expander padding */
        .streamlit-expanderHeader,
        .streamlit-expanderContent {
            padding: 0.5rem !important;
        }
    }

    /* === LANDSCAPE MODE ON MOBILE === */
    @media only screen and (max-height: 500px) and (orientation: landscape) {
        .main-header {
            font-size: 1.5rem;
            margin-bottom: 0.25rem;
        }
        .sub-header {
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }
        .stat-box {
            padding: 0.5rem;
        }
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
    st.markdown('<p class="main-header">🎯 GoalPath AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI-Powered Goal Planner for Learning, Career, Freelancing & More</p>', unsafe_allow_html=True)


def render_learning_path_generator(generator):
    """Render the goal plan generator form with template support"""
    st.markdown("### 🚀 Create Your Goal Plan")

    # Initialize session state for selected template
    if 'selected_template' not in st.session_state:
        st.session_state.selected_template = None

    # Tabs for template vs custom
    tab1, tab2 = st.tabs(["📋 Choose Template", "✍️ Start from Scratch"])

    with tab1:
        # TEMPLATE SELECTION TAB
        render_template_selector(generator)

    with tab2:
        # CUSTOM GOAL TAB (original form)
        render_custom_goal_form(generator, template=None)


def render_template_selector(generator):
    """Render template selection interface"""
    from utils.templates import get_all_templates, get_templates_by_type, search_templates, get_all_tags

    st.markdown("#### 🎯 Browse Goal Templates")
    st.caption("Quick-start with proven goal structures. All fields are customizable!")

    # Search and filters
    col_search, col_filter = st.columns([2, 1])

    with col_search:
        search_query = st.text_input(
            "🔍 Search templates",
            placeholder="e.g., remote jobs, AI, freelance income, fitness",
            label_visibility="collapsed"
        )

    with col_filter:
        goal_type_filter = st.selectbox(
            "Filter by type",
            ["All Types", "📚 Learning & Skills", "💼 Career Transition",
             "💰 Freelance & Business", "🚀 Project Completion", "🎯 Personal Achievement"],
            label_visibility="collapsed"
        )

    # Get templates based on filters
    all_templates = get_all_templates()

    if search_query:
        templates = search_templates(search_query)
    else:
        templates = all_templates

    # Filter by type if selected
    if goal_type_filter != "All Types":
        goal_type_map = {
            "📚 Learning & Skills": "learning",
            "💼 Career Transition": "career",
            "💰 Freelance & Business": "freelance",
            "🚀 Project Completion": "project",
            "🎯 Personal Achievement": "personal"
        }
        filter_type = goal_type_map[goal_type_filter]
        templates = [t for t in templates if t.goal_type == filter_type]

    # Display template count
    st.caption(f"Showing {len(templates)} template(s)")

    # Display templates as cards
    if not templates:
        st.info("No templates found. Try different search terms or filters.")
    else:
        # Group templates by category for better organization
        templates_by_type = {}
        for template in templates:
            if template.goal_type not in templates_by_type:
                templates_by_type[template.goal_type] = []
            templates_by_type[template.goal_type].append(template)

        # Category icons
        category_icons = {
            "learning": "📚",
            "career": "💼",
            "freelance": "💰",
            "project": "🚀",
            "personal": "🎯"
        }

        category_names = {
            "learning": "Learning & Skills",
            "career": "Career Transition",
            "freelance": "Freelance & Business",
            "project": "Project Completion",
            "personal": "Personal Achievement"
        }

        for goal_type, templates_list in templates_by_type.items():
            st.markdown(f"#### {category_icons[goal_type]} {category_names[goal_type]}")

            # Display templates in rows of 2
            for i in range(0, len(templates_list), 2):
                cols = st.columns(2)

                for j, col in enumerate(cols):
                    if i + j < len(templates_list):
                        template = templates_list[i + j]

                        with col:
                            with st.container():
                                st.markdown(f"""
                                <div style='padding: 15px; border: 1px solid #ddd; border-radius: 8px; margin-bottom: 10px;'>
                                    <h4 style='margin-top: 0;'>{template.name}</h4>
                                    <p style='color: #666; font-size: 0.9em;'>{template.description}</p>
                                    <p style='margin: 5px 0;'>
                                        ⏱️ {template.timeframe} days |
                                        ⏰ {template.hours_per_day} hrs/day |
                                        📊 {template.difficulty}
                                    </p>
                                </div>
                                """, unsafe_allow_html=True)

                                # Tags
                                if template.tags:
                                    tag_html = " ".join([f"<span style='background: #e8f4f8; padding: 2px 8px; border-radius: 3px; font-size: 0.8em; margin-right: 5px;'>{tag}</span>" for tag in template.tags[:4]])
                                    st.markdown(tag_html, unsafe_allow_html=True)

                                if st.button(f"Use This Template", key=f"template_{template.name}", use_container_width=True):
                                    st.session_state.selected_template = template
                                    st.rerun()

    # If template selected, show the custom form with pre-filled values
    if st.session_state.selected_template:
        st.markdown("---")
        st.markdown("#### ✏️ Customize Your Template")
        st.info(f"**Template:** {st.session_state.selected_template.name} - All fields below are editable!")

        render_custom_goal_form(generator, template=st.session_state.selected_template)


def render_custom_goal_form(generator, template=None):
    """Render the custom goal form (optionally pre-filled with template)"""
    from datetime import date as dt_date

    # Goal type selector
    goal_type_options = {
        "📚 Learning & Skills": "learning",
        "💼 Career Transition": "career",
        "💰 Freelance & Business": "freelance",
        "🚀 Project Completion": "project",
        "🎯 Personal Achievement": "personal"
    }

    # Pre-select goal type if template provided
    default_goal_type_index = 0
    if template:
        goal_type_to_label = {v: k for k, v in goal_type_options.items()}
        default_label = goal_type_to_label.get(template.goal_type, list(goal_type_options.keys())[0])
        default_goal_type_index = list(goal_type_options.keys()).index(default_label)

    selected_type = st.selectbox(
        "Goal Type",
        list(goal_type_options.keys()),
        index=default_goal_type_index,
        help="Select the type of goal you want to achieve"
    )
    goal_type = goal_type_options[selected_type]

    # Update placeholder based on goal type
    placeholders = {
        "learning": "e.g., Learn prompt engineering, Master Python, Understand blockchain",
        "career": "e.g., Get hired as AI engineer, Transition to product management, Land remote job",
        "freelance": "e.g., Get 5 Fiverr clients, Earn $1000/month freelancing, Launch consulting business",
        "project": "e.g., Build portfolio website, Launch mobile app, Write a book",
        "personal": "e.g., Run a 10K race, Learn guitar, Lose 20 pounds"
    }

    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        goal = st.text_input(
            "What do you want to achieve?",
            value=template.goal_text if template else "",
            placeholder=placeholders.get(goal_type, "Enter your goal"),
            help="Enter your goal in a clear, specific way"
        )

    with col2:
        timeframe = st.number_input(
            "Timeframe (days)",
            min_value=1,
            max_value=365,
            value=template.timeframe if template else 30,
            help="How many days do you want to dedicate to this goal?"
        )

    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        from utils.voice_handler import render_voice_input_button
        render_voice_input_button(key_suffix="goal_input")

    # Date and time planning inputs
    st.markdown("#### 📅 Schedule Your Goal")

    col_date, col_hours = st.columns(2)

    with col_date:
        start_date = st.date_input(
            "Start Date",
            value=dt_date.today(),
            help="When do you want to start working on this goal?"
        )

    with col_hours:
        hours_per_day = st.number_input(
            "Hours per day",
            min_value=0.5,
            max_value=24.0,
            value=template.hours_per_day if template else 2.0,
            step=0.5,
            help="How many hours per day can you dedicate?"
        )

    # Optional advanced scheduling
    with st.expander("⚙️ Advanced Schedule (Optional)"):
        st.caption("Customize your availability for more realistic planning")

        # Unavailable dates
        unavailable_dates_input = st.text_input(
            "Unavailable Dates (Optional)",
            placeholder="e.g., Nov 20-22, Dec 1, Dec 25",
            help="Enter specific dates you're unavailable (supports ranges)"
        )

        # Quick skip options
        st.markdown("**Skip recurring days:**")
        col_skip1, col_skip2 = st.columns(2)

        with col_skip1:
            skip_weekends = st.checkbox("Skip weekends", value=False)
            skip_wednesday = st.checkbox("Skip Wednesdays", value=False)

        with col_skip2:
            skip_thursday = st.checkbox("Skip Thursdays", value=False)
            skip_friday = st.checkbox("Skip Fridays", value=False)

        # Build skip_weekdays list
        skip_weekdays = []
        if skip_wednesday:
            skip_weekdays.append(2)  # Wednesday
        if skip_thursday:
            skip_weekdays.append(3)  # Thursday
        if skip_friday:
            skip_weekdays.append(4)  # Friday

    # Generate button
    button_cols = st.columns([3, 1])
    with button_cols[0]:
        generate_button = st.button("Generate Goal Plan", type="primary", use_container_width=True)

    with button_cols[1]:
        if template and st.button("Clear Template", use_container_width=True):
            st.session_state.selected_template = None
            st.rerun()

    if generate_button:
        if not goal:
            st.error("Please enter a goal!")
            return

        with st.spinner(f"🤖 AI is creating your personalized {selected_type.split()[0].lower()} plan..."):
            try:
                # Generate goal plan with scheduling parameters
                learning_path = generator.create_learning_path(
                    goal,
                    timeframe,
                    goal_type,
                    start_date=start_date.strftime('%Y-%m-%d'),
                    hours_per_day=hours_per_day,
                    unavailable_dates_input=unavailable_dates_input if unavailable_dates_input.strip() else None,
                    skip_weekends=skip_weekends,
                    skip_weekdays=skip_weekdays if skip_weekdays else None
                )

                # Store in session state
                st.session_state.generated_path = learning_path
                st.session_state.current_path_id = learning_path['path_id']
                st.session_state.show_generator = False
                st.session_state.selected_template = None  # Clear template after generation

                st.success(f"✅ {selected_type} plan generated successfully!")
                st.rerun()

            except Exception as e:
                st.error(f"Error generating goal plan: {str(e)}")


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
        due_date_str = topic.get('due_date', None)

        # Format title with calendar date if available
        from utils.date_scheduler import format_date_display
        if due_date_str:
            date_display = format_date_display(due_date_str)
            title = f"{date_display}: {topic_name}"
        else:
            title = f"📅 Day {day_num}: {topic_name}"

        with st.expander(title, expanded=(day_num == 1)):
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
        goal_type = path.get('goal_type', 'learning')

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

        # Goal type icons
        goal_type_icons = {
            'learning': '📚',
            'career': '💼',
            'freelance': '💰',
            'project': '🚀',
            'personal': '🎯'
        }
        goal_type_icon = goal_type_icons.get(goal_type, '📚')

        col1, col2, col3 = st.columns([3, 1, 1])

        with col1:
            st.markdown(f"{status_icon} {goal_type_icon} **{goal}**")
            st.caption(f"Created: {created_at[:10]} | {timeframe} days | Type: {goal_type.title()} | Status: {status.replace('_', ' ').title()}")

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

    # Export and advanced options
    with st.expander("⚙️ Advanced Options"):
        # PDF Export
        st.markdown("**📄 Export**")
        if st.button("📥 Download as PDF", key=f"export_pdf_{path_id}"):
            try:
                from io import BytesIO
                from reportlab.lib.pagesizes import letter
                from reportlab.lib.styles import getSampleStyleSheet
                from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
                from reportlab.lib.units import inch

                buffer = BytesIO()
                doc = SimpleDocTemplate(buffer, pagesize=letter)
                styles = getSampleStyleSheet()
                story = []

                # Title
                goal_type = path_info.get('goal_type', 'learning').title()
                title = Paragraph(f"<b>{path_info['goal']}</b>", styles['Title'])
                story.append(title)
                story.append(Spacer(1, 0.2*inch))

                # Metadata
                meta = Paragraph(f"Type: {goal_type} | Timeframe: {path_info['timeframe']} days | Progress: {stats['progress_percentage']:.0f}%", styles['Normal'])
                story.append(meta)
                story.append(Spacer(1, 0.3*inch))

                # Curriculum
                from utils.date_scheduler import format_date_display
                for topic in curriculum:
                    # Use calendar date if available
                    due_date_str = topic.get('due_date', None)
                    if due_date_str:
                        date_display = format_date_display(due_date_str)
                        day_header = f"{date_display}: {topic['topic']}"
                    else:
                        day_header = f"Day {topic['day']}: {topic['topic']}"

                    day_text = Paragraph(f"<b>{day_header}</b>", styles['Heading2'])
                    story.append(day_text)
                    story.append(Spacer(1, 0.1*inch))

                    # Priority and hours
                    priority = topic.get('priority', 'medium').upper()
                    info = Paragraph(f"Priority: {priority} | Estimated: {topic['estimated_hours']} hours", styles['Normal'])
                    story.append(info)
                    story.append(Spacer(1, 0.1*inch))

                    # Subtopics
                    if topic['subtopics']:
                        for subtopic in topic['subtopics']:
                            bullet = Paragraph(f"• {subtopic}", styles['Normal'])
                            story.append(bullet)
                    story.append(Spacer(1, 0.2*inch))

                doc.build(story)
                buffer.seek(0)

                st.download_button(
                    label="💾 Save PDF",
                    data=buffer,
                    file_name=f"goalpath_{path_info['goal'][:30].replace(' ', '_')}.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"PDF generation failed: {str(e)}")

        # Calendar Export
        st.markdown("---")
        st.markdown("**📅 Calendar Export**")

        # Check if plan has due dates
        has_due_dates = any(topic.get('due_date') for topic in curriculum)

        if not has_due_dates:
            st.info("💡 Generate your plan with calendar dates first to use this feature.")
        else:
            if st.button("📅 Export to Calendar (.ics)", key=f"export_calendar_{path_id}"):
                try:
                    # Generate .ics file
                    ics_content = generator.db.generate_ics_calendar(path_id, default_start_time_hour=9)

                    if ics_content:
                        filename = generator.db.get_calendar_filename(path_id)

                        st.download_button(
                            label="💾 Download Calendar File",
                            data=ics_content,
                            file_name=filename,
                            mime="text/calendar"
                        )

                        # Show import instructions
                        st.success("✅ Calendar file ready!")
                        st.markdown("""
**Import into your calendar:**
- **Google Calendar:** Settings → Import & Export → Import
- **Outlook:** File → Open & Export → Import/Export
- **Apple Calendar:** File → Import → Select file
- **Other apps:** Look for Import or Add Calendar option

Your goal plan tasks will appear as scheduled events with all details!
                        """)
                    else:
                        st.error("Failed to generate calendar file. Please ensure icalendar library is installed.")
                except Exception as e:
                    st.error(f"Calendar generation failed: {str(e)}")

        st.markdown("---")
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

    # On-track indicator
    from datetime import datetime
    created_at = path_info.get('created_at', '')
    timeframe = path_info.get('timeframe', 30)

    if created_at:
        try:
            # Parse created_at date (format: YYYY-MM-DD HH:MM:SS)
            created_date = datetime.strptime(created_at.split(' ')[0], '%Y-%m-%d')
            current_date = datetime.now()
            days_elapsed = (current_date - created_date).days

            # Calculate expected progress
            expected_progress = min((days_elapsed / timeframe) * 100, 100)
            actual_progress = stats['progress_percentage']

            # Determine status
            if actual_progress >= expected_progress:
                status_text = "✅ On Track"
                status_color = "green"
            else:
                behind_by = expected_progress - actual_progress
                status_text = f"⚠️ Behind by {behind_by:.0f}%"
                status_color = "orange"

            # Display on-track status
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"**Status:**")
            with col2:
                st.markdown(f"<span style='color: {status_color}; font-weight: bold;'>{status_text}</span> (Expected: {expected_progress:.0f}% by day {days_elapsed})", unsafe_allow_html=True)
        except:
            pass  # Skip if date parsing fails

    # Reschedule button (only show if plan has calendar dates)
    start_date = path_info.get('start_date')
    if start_date:
        st.markdown("---")

        with st.expander("📅 Reschedule Plan"):
            st.caption("Adjust your schedule for incomplete topics while keeping completed ones unchanged")

            from datetime import date as dt_date

            col_new_start, col_new_hours = st.columns(2)

            with col_new_start:
                new_start_date = st.date_input(
                    "New Start Date for Remaining Topics",
                    value=dt_date.today(),
                    help="When do you want to reschedule remaining topics to?"
                )

            with col_new_hours:
                current_hours = path_info.get('hours_per_day', 2.0)
                new_hours_per_day = st.number_input(
                    "New Hours per Day",
                    min_value=0.5,
                    max_value=24.0,
                    value=current_hours,
                    step=0.5,
                    help="Update your daily time commitment"
                )

            # Optional: Update unavailable dates
            new_unavailable_dates = st.text_input(
                "Update Unavailable Dates (Optional)",
                placeholder="e.g., Nov 20-22, Dec 1",
                help="Enter any new dates you're unavailable"
            )

            if st.button("Reschedule Incomplete Topics", type="primary"):
                from utils.date_scheduler import parse_unavailable_dates, reschedule_incomplete_topics
                import json

                # Parse new unavailable dates
                unavailable_dates_list = []
                if new_unavailable_dates and new_unavailable_dates.strip():
                    unavailable_dates_list = parse_unavailable_dates(new_unavailable_dates)

                # Reschedule incomplete topics
                rescheduled_topics = reschedule_incomplete_topics(
                    curriculum,
                    new_start_date,
                    new_hours_per_day,
                    unavailable_dates_list,
                    weekly_pattern=None,
                    skip_weekends=False,
                    skip_weekdays=None
                )

                # Update database
                for topic in rescheduled_topics:
                    if not topic.get('is_completed', False):
                        generator.db.update_topic_due_date(topic['id'], topic['due_date'])

                # Update path schedule in database
                unavailable_json = None
                if unavailable_dates_list:
                    unavailable_json = json.dumps([d.strftime('%Y-%m-%d') for d in unavailable_dates_list])

                generator.db.update_path_schedule(
                    path_id,
                    start_date=new_start_date.strftime('%Y-%m-%d'),
                    hours_per_day=new_hours_per_day,
                    unavailable_dates=unavailable_json
                )

                st.success("✅ Plan rescheduled successfully!")
                st.rerun()

    st.markdown("---")

    # AI Progress Review & Coaching Section
    st.markdown("### 🤖 AI Coaching")

    col_coach1, col_coach2 = st.columns(2)

    with col_coach1:
        if st.button("📊 Get Progress Review & Coaching", use_container_width=True, type="primary"):
            with st.spinner("🤖 AI is analyzing your progress..."):
                # Get comprehensive data for coaching
                time_stats = generator.db.get_path_time_stats(path_id)
                from datetime import datetime
                created_at = path_info.get('created_at', '')
                days_elapsed = 0
                if created_at:
                    try:
                        created_date = datetime.strptime(created_at.split(' ')[0], '%Y-%m-%d')
                        days_elapsed = (datetime.now() - created_date).days
                    except:
                        pass

                # Create coaching prompt
                coaching_prompt = f"""You are an encouraging but honest AI coach reviewing someone's goal progress.

**Goal:** {path_info['goal']}
**Goal Type:** {path_info.get('goal_type', 'learning')}
**Timeframe:** {timeframe} days
**Days Elapsed:** {days_elapsed} days

**Progress Data:**
- Tasks Completed: {stats['completed_topics']}/{stats['total_topics']} ({stats['progress_percentage']:.0f}%)
- Estimated Total Time: {time_stats['total_estimated_hours']:.1f} hours
- Actual Time Spent: {time_stats['total_actual_hours']:.1f} hours
- Time Variance: {time_stats['variance_hours']:.1f} hours ({time_stats['variance_percentage']:.0f}%)

**Analysis Required:**
1. PERFORMANCE SUMMARY (2-3 sentences) - How are they doing overall?
2. KEY INSIGHTS (2-3 bullet points) - What patterns do you see?
3. ACTIONABLE RECOMMENDATIONS (3-4 specific suggestions) - What should they do next?

Write in a conversational, encouraging but honest tone. Be specific with numbers. Give practical advice they can act on TODAY.

Format your response in 3 clear sections with those headers."""

                try:
                    # Get AI review using Claude
                    review_text = generator.ai.generate_text(coaching_prompt)

                    # Save review to database
                    generator.db.save_coaching_review(
                        path_id=path_id,
                        review_text=review_text
                    )

                    # Display review
                    st.session_state[f'show_review_{path_id}'] = True
                    st.rerun()

                except Exception as e:
                    st.error(f"Coaching analysis failed: {str(e)}")

    with col_coach2:
        # Show last review date if available
        latest_review = generator.db.get_latest_coaching_review(path_id)
        if latest_review:
            st.caption(f"Last reviewed: {latest_review['created_at'][:16]}")

    # Display latest review if available
    if st.session_state.get(f'show_review_{path_id}', False):
        latest_review = generator.db.get_latest_coaching_review(path_id)
        if latest_review:
            st.markdown("---")
            st.markdown("#### 🎯 Your Progress Review")

            # Display time stats
            time_stats = generator.db.get_path_time_stats(path_id)
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Tasks", f"{stats['completed_topics']}/{stats['total_topics']}")
            with col2:
                st.metric("Progress", f"{stats['progress_percentage']:.0f}%")
            with col3:
                st.metric("Est. Hours", f"{time_stats['total_estimated_hours']:.1f}")
            with col4:
                variance_color = "inverse" if time_stats['variance_hours'] > 0 else "normal"
                st.metric("Actual Hours", f"{time_stats['total_actual_hours']:.1f}",
                         delta=f"{time_stats['variance_hours']:+.1f}",
                         delta_color=variance_color)

            # Display AI coaching text
            st.markdown(latest_review['review_text'])

            # View past reviews
            with st.expander("📜 View Past Reviews"):
                all_reviews = generator.db.get_coaching_reviews(path_id)
                for idx, review in enumerate(all_reviews):
                    st.markdown(f"**Review #{len(all_reviews) - idx}** - {review['created_at'][:16]}")
                    st.markdown(review['review_text'])
                    st.markdown("---")

    st.markdown("---")

    # Tabs for Curriculum and AI Tutor
    tab1, tab2, tab3 = st.tabs(["📖 Curriculum", "🤖 AI Tutor", "💬 AI Coach Chat"])

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
            priority = topic.get('priority', 'medium')

            # Priority indicators
            priority_emoji = {
                'high': '🔴',
                'medium': '🟡',
                'low': '🟢'
            }.get(priority, '🟡')

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
                    # Display with calendar date and color coding
                    from utils.date_scheduler import format_date_display, get_date_status

                    due_date_str = topic.get('due_date', None)
                    date_status = get_date_status(due_date_str, is_completed)

                    # Format display title
                    if due_date_str:
                        date_display = format_date_display(due_date_str)
                        title = f"{date_status['emoji']} {priority_emoji} {date_display}: {topic_name}"
                    else:
                        title = f"{priority_emoji} {'✅' if is_completed else '⭐'} Day {day_num}: {topic_name}"

                    with st.expander(title, expanded=not is_completed and date_status.get('status') != 'upcoming'):
                        # Show date status if available
                        if due_date_str:
                            from utils.date_scheduler import get_days_until
                            days_until = get_days_until(due_date_str)

                            if not is_completed:
                                if days_until is not None:
                                    if days_until < 0:
                                        st.warning(f"⚠️ Overdue by {abs(days_until)} day(s)")
                                    elif days_until == 0:
                                        st.info(f"📌 Due today!")
                                    else:
                                        st.caption(f"📅 Due in {days_until} day(s)")

                        # Time tracking section
                        actual_hours = topic.get('actual_hours', 0) or 0

                        col_time1, col_time2 = st.columns(2)
                        with col_time1:
                            st.markdown(f"**⏱️ Estimated:** {estimated_hours} hrs")
                        with col_time2:
                            time_diff = actual_hours - estimated_hours
                            diff_color = "red" if time_diff > 0 else "green" if time_diff < 0 else "gray"
                            st.markdown(f"**⏲️ Actual:** {actual_hours:.1f} hrs <span style='color: {diff_color};'>({time_diff:+.1f})</span>", unsafe_allow_html=True)

                        # Timer and manual input
                        if not is_completed:
                            st.markdown("---")

                            # Initialize timer state
                            timer_key = f"timer_{topic_id}"
                            if timer_key not in st.session_state:
                                st.session_state[timer_key] = {'running': False, 'start_time': None, 'elapsed': 0}

                            timer_col1, timer_col2 = st.columns(2)

                            with timer_col1:
                                st.markdown("**⏱️ Track Time**")

                                if not st.session_state[timer_key]['running']:
                                    if st.button(f"▶️ Start Timer", key=f"start_{topic_id}", use_container_width=True):
                                        from datetime import datetime
                                        st.session_state[timer_key]['running'] = True
                                        st.session_state[timer_key]['start_time'] = datetime.now().isoformat()
                                        st.rerun()
                                else:
                                    # Show elapsed time
                                    from datetime import datetime
                                    start = datetime.fromisoformat(st.session_state[timer_key]['start_time'])
                                    elapsed_seconds = int((datetime.now() - start).total_seconds())
                                    hours = elapsed_seconds // 3600
                                    minutes = (elapsed_seconds % 3600) // 60
                                    seconds = elapsed_seconds % 60

                                    st.markdown(f"⏱️ **{hours:02d}:{minutes:02d}:{seconds:02d}**")

                                    if st.button(f"⏸️ Stop & Save", key=f"stop_{topic_id}", use_container_width=True):
                                        duration_minutes = elapsed_seconds // 60
                                        if duration_minutes > 0:
                                            generator.db.add_time_session(
                                                topic_id=topic_id,
                                                path_id=path_id,
                                                duration_minutes=duration_minutes,
                                                start_time=st.session_state[timer_key]['start_time'],
                                                end_time=datetime.now().isoformat()
                                            )
                                        st.session_state[timer_key]['running'] = False
                                        st.session_state[timer_key]['start_time'] = None
                                        st.success(f"✅ Saved {duration_minutes} minutes!")
                                        st.rerun()

                            with timer_col2:
                                st.markdown("**✏️ Add Time Manually**")
                                manual_hours = st.number_input(
                                    "Hours",
                                    min_value=0.0,
                                    max_value=24.0,
                                    step=0.5,
                                    key=f"manual_{topic_id}",
                                    label_visibility="collapsed"
                                )
                                if st.button("Add Time", key=f"add_manual_{topic_id}", use_container_width=True):
                                    if manual_hours > 0:
                                        generator.db.add_time_session(
                                            topic_id=topic_id,
                                            path_id=path_id,
                                            duration_minutes=int(manual_hours * 60),
                                            notes="Manually added"
                                        )
                                        st.success(f"✅ Added {manual_hours} hours!")
                                        st.rerun()

                            st.markdown("---")

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

                                # YouTube auto-embed
                                if 'youtube.com' in resource_url or 'youtu.be' in resource_url:
                                    import re
                                    # Extract video ID
                                    video_id = None
                                    if 'youtube.com/watch?v=' in resource_url:
                                        video_id = resource_url.split('v=')[1].split('&')[0]
                                    elif 'youtu.be/' in resource_url:
                                        video_id = resource_url.split('youtu.be/')[1].split('?')[0]

                                    if video_id:
                                        st.markdown(f"""
                                        <iframe width="100%" height="315"
                                        src="https://www.youtube.com/embed/{video_id}"
                                        frameborder="0"
                                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                        allowfullscreen>
                                        </iframe>
                                        """, unsafe_allow_html=True)

                        # Resource Links Section
                        st.markdown("---")
                        st.markdown("**📎 My Resource Links**")
                        st.caption("Add links to your own study materials (Google Drive, Notion, saved files, etc.)")

                        current_links = topic.get('resource_links', '') or ''
                        resource_links = st.text_area(
                            "Add your resource links (one per line)",
                            value=current_links,
                            height=100,
                            key=f"resource_links_{topic_id}",
                            placeholder="Example:\nhttps://drive.google.com/folder/my-python-notes\nhttps://notion.so/my-study-guide\n~/Documents/python-tutorial.pdf",
                            label_visibility="collapsed"
                        )

                        # Auto-save on change
                        if resource_links != current_links:
                            conn = generator.db.get_connection()
                            cursor = conn.cursor()
                            cursor.execute("""
                                UPDATE topics
                                SET resource_links = ?
                                WHERE id = ?
                            """, (resource_links, topic_id))
                            conn.commit()
                            conn.close()

                        # Display links as clickable
                        if resource_links and resource_links.strip():
                            st.markdown("**Your saved links:**")
                            for link in resource_links.strip().split('\n'):
                                link = link.strip()
                                if link:
                                    if link.startswith('http://') or link.startswith('https://'):
                                        st.markdown(f"🔗 [{link}]({link})")
                                    else:
                                        st.markdown(f"📁 `{link}`")

            st.markdown("<br>", unsafe_allow_html=True)

    with tab2:
        # AI Tutor Chat Interface
        st.markdown("#### 🤖 AI Learning Tutor")
        st.caption("Ask questions, upload images/files, and get personalized explanations from multiple AI models")

        # Voice settings
        with st.expander("🎙️ Voice Settings", expanded=False):
            from utils.voice_handler import render_voice_settings
            render_voice_settings(key_prefix="tutor_")

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

                # Voice output button for AI responses
                if st.session_state.get('auto_read_responses', False) or True:  # Always show button
                    col_voice1, col_voice2 = st.columns([1, 4])
                    with col_voice1:
                        from utils.voice_handler import render_voice_output_button
                        render_voice_output_button(
                            text_to_speak=message['content'][:500],  # Limit to 500 chars for performance
                            button_text="🔊 Read",
                            key_suffix=f"response_{path_id}_{i}"
                        )
            st.markdown("---")

        # Chat input with voice
        col_input, col_voice = st.columns([4, 1])

        with col_input:
            user_question = st.text_area(
                "Ask a question about your learning topics:",
                placeholder="e.g., Can you explain prompt engineering in simple terms?\nWhat's the difference between zero-shot and few-shot prompting?",
                height=100,
                key=f"chat_input_{path_id}"
            )

        with col_voice:
            if st.session_state.get('voice_input_enabled', True):
                st.markdown("<br>", unsafe_allow_html=True)
                from utils.voice_handler import render_voice_input_button
                render_voice_input_button(key_suffix=f"tutor_{path_id}")

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

    with tab3:
        # Conversational AI Coach Chat
        st.markdown("#### 💬 Let's Discuss Your Progress")
        st.caption("Have a natural conversation with your AI coach about your goals, challenges, and progress")

        # Voice settings for coach chat
        with st.expander("🎙️ Voice Settings", expanded=False):
            from utils.voice_handler import render_voice_settings
            render_voice_settings(key_prefix="coach_")

        # Initialize coaching chat history
        if f'coach_chat_{path_id}' not in st.session_state:
            st.session_state[f'coach_chat_{path_id}'] = []
            # Add welcome message
            st.session_state[f'coach_chat_{path_id}'].append({
                'role': 'assistant',
                'content': f"Hey! I'm your AI coach for **{path_info['goal']}**. I've been following your progress - you've completed {stats['completed_topics']}/{stats['total_topics']} tasks so far. How's it going? What would you like to discuss?"
            })

        # Get time stats for context
        time_stats = generator.db.get_path_time_stats(path_id)

        # Build context for conversational AI
        from datetime import datetime
        created_at = path_info.get('created_at', '')
        days_elapsed = 0
        if created_at:
            try:
                created_date = datetime.strptime(created_at.split(' ')[0], '%Y-%m-%d')
                days_elapsed = (datetime.now() - created_date).days
            except:
                pass

        coach_context = f"""You are a friendly, conversational AI coach. You're having a natural discussion with someone working on their goal.

THEIR GOAL: {path_info['goal']}
GOAL TYPE: {path_info.get('goal_type', 'learning')}
TIMEFRAME: {timeframe} days
DAYS ELAPSED: {days_elapsed}

CURRENT PROGRESS:
- Tasks: {stats['completed_topics']}/{stats['total_topics']} ({stats['progress_percentage']:.0f}%)
- Time: {time_stats['total_actual_hours']:.1f} hrs actual vs {time_stats['total_estimated_hours']:.1f} hrs estimated
- Variance: {time_stats['variance_hours']:+.1f} hrs

CONVERSATION STYLE:
- Be warm, encouraging, and conversational (like chatting with a friend who's a coach)
- Ask follow-up questions to understand their situation better
- Give specific, actionable advice based on their actual data
- Be honest but supportive - if they're behind, acknowledge it but focus on solutions
- Use their actual numbers when relevant
- Keep responses concise (3-4 sentences max unless they ask for detail)

Examples of GOOD responses:
- "40% complete is solid! How are you feeling about the pace? Is 2 hours a day still working for you?"
- "I'm noticing you're spending a bit more time than estimated. That's totally normal - it means you're being thorough! Should we talk about adjusting the timeline?"
- "Let's tackle that overwhelmed feeling. What if we focus on just the next 3 tasks this week? Sometimes breaking it down helps."

Examples of BAD responses:
- "Your completion rate is 40%." (too clinical)
- "You should increase daily hours by 0.5." (too robotic)
- Long analysis without asking what they need (not conversational)

Remember: You're having a CONVERSATION, not delivering a report."""

        # Display coaching chat history
        for i, message in enumerate(st.session_state[f'coach_chat_{path_id}']):
            if message['role'] == 'user':
                st.markdown(f"**You:** {message['content']}")
            else:
                st.markdown(f"**Coach:** {message['content']}")

                # Voice output for coach responses
                col_voice1, col_voice2 = st.columns([1, 4])
                with col_voice1:
                    from utils.voice_handler import render_voice_output_button
                    render_voice_output_button(
                        text_to_speak=message['content'][:500],
                        button_text="🔊 Hear",
                        key_suffix=f"coach_{path_id}_{i}"
                    )
            st.markdown("---")

        # Chat input with voice
        col_input, col_voice = st.columns([4, 1])

        with col_input:
            coach_question = st.text_area(
                "What's on your mind?",
                placeholder="e.g., I'm feeling overwhelmed...\nI have less time this week, what should I do?\nHow am I doing overall?\nShould I adjust my timeline?",
                height=100,
                key=f"coach_input_{path_id}"
            )

        with col_voice:
            if st.session_state.get('voice_input_enabled', True):
                st.markdown("<br>", unsafe_allow_html=True)
                from utils.voice_handler import render_voice_input_button
                render_voice_input_button(key_suffix=f"coach_{path_id}")

        col1, col2 = st.columns([1, 5])
        with col1:
            if st.button("💬 Send", type="primary", key=f"send_coach_{path_id}"):
                if coach_question.strip():
                    # Add user message to history
                    st.session_state[f'coach_chat_{path_id}'].append({
                        'role': 'user',
                        'content': coach_question
                    })

                    # Save to database
                    generator.db.save_chat_message(path_id, coach_question, 'user')

                    # Build conversation history for context
                    conversation_history = ""
                    for msg in st.session_state[f'coach_chat_{path_id}'][-6:]:  # Last 3 exchanges
                        role_label = "User" if msg['role'] == 'user' else "Coach"
                        conversation_history += f"{role_label}: {msg['content']}\n\n"

                    # Get AI coaching response
                    full_prompt = f"""{coach_context}

RECENT CONVERSATION:
{conversation_history}

User just said: {coach_question}

Respond naturally and conversationally. Keep it to 3-4 sentences unless they explicitly ask for more detail."""

                    with st.spinner("Coach is thinking..."):
                        try:
                            coach_response = generator.ai.generate_text(full_prompt)

                            # Add coach response to history
                            st.session_state[f'coach_chat_{path_id}'].append({
                                'role': 'assistant',
                                'content': coach_response
                            })

                            # Save to database
                            generator.db.save_chat_message(path_id, coach_response, 'assistant')

                            st.rerun()
                        except Exception as e:
                            st.error(f"Coaching chat failed: {str(e)}")
                else:
                    st.warning("Please enter a message")

        with col2:
            if st.button("Clear Conversation", key=f"clear_coach_{path_id}"):
                st.session_state[f'coach_chat_{path_id}'] = []
                generator.db.clear_chat_history(path_id)
                st.rerun()

        # Quick prompts
        st.markdown("**💡 Quick Prompts:**")
        prompt_col1, prompt_col2 = st.columns(2)

        with prompt_col1:
            if st.button("How am I doing overall?", key=f"prompt1_{path_id}"):
                st.session_state[f'coach_preset_{path_id}'] = "How am I doing overall?"
                st.rerun()

            if st.button("I'm feeling overwhelmed", key=f"prompt2_{path_id}"):
                st.session_state[f'coach_preset_{path_id}'] = "I'm feeling a bit overwhelmed with all these tasks. What should I focus on?"
                st.rerun()

        with prompt_col2:
            if st.button("Should I adjust my timeline?", key=f"prompt3_{path_id}"):
                st.session_state[f'coach_preset_{path_id}'] = "Should I adjust my timeline? Am I on track?"
                st.rerun()

            if st.button("I have less time this week", key=f"prompt4_{path_id}"):
                st.session_state[f'coach_preset_{path_id}'] = "I have less time available this week. How should I adapt my plan?"
                st.rerun()


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
            st.caption("GoalPath AI helps you create structured goal plans with AI-powered planning and progress tracking.")

            # Logout button
            st.markdown("---")
            if st.button("🚪 Logout", use_container_width=True, type="secondary"):
                logout(cookies)

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
