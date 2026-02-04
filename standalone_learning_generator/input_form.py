"""
Streamlit Input Form for Learning Path Generator
Extracted and adapted from app.py

This provides a ready-to-use Streamlit form for collecting user input
for generating learning paths with flexible scheduling options.
"""

from typing import Optional

try:
    import streamlit as st
    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False
    print("Warning: streamlit not installed. This module requires streamlit.")


def render_learning_input_form(key_prefix: str = "") -> Optional[dict]:
    """
    Render a Streamlit form for learning path input
    
    Args:
        key_prefix: Prefix for widget keys (useful if multiple forms on same page)
        
    Returns:
        Dictionary with form data if submitted, None otherwise
        Keys: topic, timeframe, hours_per_day, start_date, skip_weekends,
              skip_weekdays, unavailable_dates_input, proficiency, focus_areas,
              additional_requests
    """
    if not STREAMLIT_AVAILABLE:
        raise ImportError("streamlit is required for this module")
    
    from datetime import date as dt_date
    
    st.markdown("### 🎓 Create Your Learning Path")
    
    # Topic input
    topic = st.text_input(
        "What do you want to learn?",
        placeholder="e.g., prompt engineering, n8n automation, Python for data science",
        key=f"{key_prefix}topic",
        help="Enter the topic or skill you want to master"
    )
    
    # Basic settings in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        timeframe = st.number_input(
            "Timeframe (days)",
            min_value=1,
            max_value=365,
            value=30,
            key=f"{key_prefix}timeframe",
            help="How many days do you want to dedicate to this?"
        )
    
    with col2:
        hours_per_day = st.number_input(
            "Hours per day",
            min_value=0.5,
            max_value=24.0,
            value=2.0,
            step=0.5,
            key=f"{key_prefix}hours_per_day",
            help="How many hours per day can you dedicate?"
        )
    
    with col3:
        proficiency = st.selectbox(
            "Proficiency Level",
            ["Beginner", "Intermediate", "Advanced"],
            index=1,
            key=f"{key_prefix}proficiency",
            help="Your current skill level in this area"
        )
    
    # Start date
    start_date = st.date_input(
        "Start Date",
        value=dt_date.today(),
        key=f"{key_prefix}start_date",
        help="When do you want to start?"
    )
    
    st.markdown("---")
    
    # Advanced Scheduling
    st.markdown("#### ⚙️ Schedule Options")
    
    with st.expander("Customize your availability", expanded=False):
        st.caption("Configure which days you're available for learning")
        
        # Skip weekends
        skip_weekends = st.checkbox(
            "Skip weekends",
            value=False,
            key=f"{key_prefix}skip_weekends",
            help="Only schedule learning on weekdays"
        )
        
        # Skip specific weekdays
        st.markdown("**Skip specific weekdays:**")
        col_skip1, col_skip2 = st.columns(2)
        
        skip_weekdays = []
        weekday_options = {
            "Monday": 0,
            "Tuesday": 1,
            "Wednesday": 2,
            "Thursday": 3,
            "Friday": 4,
            "Saturday": 5,
            "Sunday": 6
        }
        
        with col_skip1:
            skip_monday = st.checkbox("Skip Monday", key=f"{key_prefix}skip_monday")
            skip_tuesday = st.checkbox("Skip Tuesday", key=f"{key_prefix}skip_tuesday")
            skip_wednesday = st.checkbox("Skip Wednesday", key=f"{key_prefix}skip_wednesday")
            skip_thursday = st.checkbox("Skip Thursday", key=f"{key_prefix}skip_thursday")
        
        with col_skip2:
            skip_friday = st.checkbox("Skip Friday", key=f"{key_prefix}skip_friday")
            skip_saturday = st.checkbox("Skip Saturday", key=f"{key_prefix}skip_saturday")
            skip_sunday = st.checkbox("Skip Sunday", key=f"{key_prefix}skip_sunday")
        
        if skip_monday:
            skip_weekdays.append(0)
        if skip_tuesday:
            skip_weekdays.append(1)
        if skip_wednesday:
            skip_weekdays.append(2)
        if skip_thursday:
            skip_weekdays.append(3)
        if skip_friday:
            skip_weekdays.append(4)
        if skip_saturday:
            skip_weekdays.append(5)
        if skip_sunday:
            skip_weekdays.append(6)
        
        # Unavailable dates
        unavailable_dates_input = st.text_input(
            "Unavailable Dates (Optional)",
            placeholder="e.g., Nov 20-22, Dec 1, Dec 25",
            key=f"{key_prefix}unavailable_dates",
            help="Enter specific dates you're unavailable (supports ranges)"
        )
    
    st.markdown("---")
    
    # Optional: Focus areas
    with st.expander("🎯 Focus Areas (Optional)", expanded=False):
        st.caption("Specify particular areas you want to focus on")
        focus_areas_text = st.text_area(
            "Enter focus areas (one per line)",
            placeholder="e.g.,\nAdvanced prompt techniques\nAPI integration\nWorkflow automation",
            key=f"{key_prefix}focus_areas",
            help="List specific topics or areas you want to prioritize"
        )
        focus_areas = [area.strip() for area in focus_areas_text.split('\n') if area.strip()] if focus_areas_text else None
    else:
        focus_areas = None
    
    # Optional: Additional requests
    with st.expander("📝 Additional Preferences (Optional)", expanded=False):
        additional_requests = st.text_area(
            "Any specific requests or preferences?",
            placeholder="e.g., I prefer video tutorials, I want hands-on projects, Include certification prep...",
            key=f"{key_prefix}additional_requests",
            help="Add any specific requirements for your learning path"
        )
    else:
        additional_requests = None
    
    st.markdown("---")
    
    # Generate button
    generate_button = st.button(
        "🚀 Generate Learning Path",
        type="primary",
        use_container_width=True,
        key=f"{key_prefix}generate"
    )
    
    # Return form data if submitted
    if generate_button:
        if not topic:
            st.error("⚠️ Please enter a topic to learn!")
            return None
        
        return {
            'topic': topic,
            'timeframe': timeframe,
            'hours_per_day': hours_per_day,
            'start_date': start_date.strftime('%Y-%m-%d'),
            'skip_weekends': skip_weekends,
            'skip_weekdays': skip_weekdays if skip_weekdays else None,
            'unavailable_dates_input': unavailable_dates_input if unavailable_dates_input.strip() else None,
            'proficiency': proficiency,
            'focus_areas': focus_areas,
            'additional_requests': additional_requests if additional_requests and additional_requests.strip() else None
        }
    
    return None


def render_quick_schedule_presets(key_prefix: str = "") -> dict:
    """
    Render quick schedule preset buttons
    
    Returns:
        Dictionary with schedule settings based on selected preset
    """
    if not STREAMLIT_AVAILABLE:
        raise ImportError("streamlit is required for this module")
    
    st.markdown("**Quick Schedule Presets:**")
    
    col1, col2, col3, col4 = st.columns(4)
    
    presets = {
        'weekdays_only': {'skip_weekends': True, 'skip_weekdays': None},
        'weekends_only': {'skip_weekends': False, 'skip_weekdays': [0, 1, 2, 3, 4]},
        'mon_wed_fri': {'skip_weekends': False, 'skip_weekdays': [1, 3, 5, 6]},
        'everyday': {'skip_weekends': False, 'skip_weekdays': None}
    }
    
    selected_preset = None
    
    with col1:
        if st.button("Weekdays Only", key=f"{key_prefix}preset_weekdays", use_container_width=True):
            selected_preset = presets['weekdays_only']
    
    with col2:
        if st.button("Weekends Only", key=f"{key_prefix}preset_weekends", use_container_width=True):
            selected_preset = presets['weekends_only']
    
    with col3:
        if st.button("Mon/Wed/Fri", key=f"{key_prefix}preset_mwf", use_container_width=True):
            selected_preset = presets['mon_wed_fri']
    
    with col4:
        if st.button("Everyday", key=f"{key_prefix}preset_everyday", use_container_width=True):
            selected_preset = presets['everyday']
    
    return selected_preset if selected_preset else {}

