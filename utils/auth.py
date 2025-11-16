"""
Authentication module for GoalPath AI
Handles password protection with cookie-based session management
"""

import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
import os
import hashlib
from datetime import datetime, timedelta


def init_cookie_manager():
    """Initialize encrypted cookie manager for persistent login"""
    # Use a secret key for encryption (from env or generate one)
    secret_key = os.getenv("COOKIE_SECRET_KEY", "goalpath-ai-default-secret-key-change-me")

    cookies = EncryptedCookieManager(
        prefix="goalpath_ai_",
        password=secret_key
    )

    if not cookies.ready():
        st.stop()

    return cookies


def hash_password(password: str) -> str:
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(cookies) -> bool:
    """
    Check if user is authenticated via cookie or password entry
    Returns True if authenticated, False otherwise
    """
    # Get password from environment (supports both .env and Streamlit Secrets)
    app_password = os.getenv("APP_PASSWORD") or st.secrets.get("APP_PASSWORD", None)

    # If no password is set, allow access (for backwards compatibility)
    if not app_password:
        return True

    # Check if user has valid cookie (24-hour session)
    if cookies.get("authenticated") == "true":
        auth_time_str = cookies.get("auth_time")
        if auth_time_str:
            try:
                auth_time = datetime.fromisoformat(auth_time_str)
                # Check if session is still valid (24 hours)
                if datetime.now() - auth_time < timedelta(hours=24):
                    return True
            except:
                pass

    # Show login form
    return False


def render_login_screen(cookies):
    """Render the login screen with GoalPath AI branding"""
    st.markdown("""
        <style>
        .login-container {
            max-width: 400px;
            margin: 100px auto;
            padding: 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .login-header {
            font-size: 2.5rem;
            font-weight: bold;
            color: white;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .login-subheader {
            font-size: 1.1rem;
            color: rgba(255,255,255,0.9);
            text-align: center;
            margin-bottom: 2rem;
        }
        .stTextInput > div > div > input {
            background-color: rgba(255,255,255,0.9);
            border-radius: 8px;
            padding: 12px;
            font-size: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Center the login form
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown('<div class="login-header">🎯 GoalPath AI</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subheader">Universal Goal Planning Platform</div>', unsafe_allow_html=True)

        # Login form
        with st.form("login_form"):
            password = st.text_input("Enter Password", type="password", placeholder="Enter your password")
            submit = st.form_submit_button("🔐 Login", use_container_width=True)

            if submit:
                app_password = os.getenv("APP_PASSWORD") or st.secrets.get("APP_PASSWORD", None)

                if password == app_password:
                    # Set cookie for 24-hour session
                    cookies["authenticated"] = "true"
                    cookies["auth_time"] = datetime.now().isoformat()
                    cookies.save()
                    st.success("✅ Login successful! Redirecting...")
                    st.rerun()
                else:
                    st.error("❌ Incorrect password. Please try again.")

        st.markdown('</div>', unsafe_allow_html=True)

        # Info message
        st.info("💡 For deployment on Streamlit Cloud, set APP_PASSWORD in the Secrets section.")


def logout(cookies):
    """Clear authentication cookies and logout"""
    cookies["authenticated"] = "false"
    cookies["auth_time"] = ""
    cookies.save()
    st.success("Logged out successfully!")
    st.rerun()
