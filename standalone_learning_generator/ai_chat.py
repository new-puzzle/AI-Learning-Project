"""
AI Chat Assistant for Learning Suggestions
Extracted from app.py render_general_ai_chat()

This provides an AI chat interface where users can ask questions about
what to learn, get career advice, and receive learning suggestions.
"""

from typing import Optional, List, Dict
import os

try:
    import streamlit as st
    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False
    print("Warning: streamlit not installed. This module requires streamlit.")

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("Warning: anthropic package not installed. Install with: pip install anthropic")


class AIChatAssistant:
    """AI Chat Assistant for learning and career advice"""
    
    def __init__(self, api_key: Optional[str] = None, model_name: str = "claude-sonnet-4-5-20250929"):
        """
        Initialize AI Chat Assistant
        
        Args:
            api_key: Anthropic API key (or set ANTHROPIC_API_KEY env var)
            model_name: Claude model to use
        """
        if not ANTHROPIC_AVAILABLE:
            raise ImportError("anthropic package is required. Install with: pip install anthropic")
        
        # Get API key
        if api_key:
            self.api_key = api_key
        else:
            try:
                import streamlit as st
                self.api_key = st.secrets.get("ANTHROPIC_API_KEY")
            except:
                self.api_key = os.getenv("ANTHROPIC_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "Anthropic API key not found. "
                "Set ANTHROPIC_API_KEY environment variable or pass api_key parameter."
            )
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = model_name
        self.system_prompt = """You are a helpful AI career and learning advisor.
Help users make informed decisions about their goals, learning paths, and career choices.
Be conversational, encouraging, and provide actionable advice.
Keep responses concise (3-5 sentences) but insightful.
When suggesting what to learn, be specific and practical."""
    
    def chat(self, message: str, conversation_history: Optional[List[Dict]] = None) -> str:
        """
        Send a message to the AI and get a response
        
        Args:
            message: User's message/question
            conversation_history: Optional list of previous messages for context
                Format: [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]
        
        Returns:
            AI response text
        """
        # Build messages list
        messages = []
        
        # Add conversation history if provided
        if conversation_history:
            for msg in conversation_history[-10:]:  # Last 10 messages for context
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
        
        # Add current message
        messages.append({
            "role": "user",
            "content": message
        })
        
        # Call API
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                system=self.system_prompt,
                messages=messages
            )
            
            return response.content[0].text
        
        except Exception as e:
            raise Exception(f"Error getting AI response: {str(e)}")
    
    def suggest_learning_path(self, goal: str, current_skills: Optional[str] = None) -> str:
        """
        Get AI suggestions for what to learn to achieve a goal
        
        Args:
            goal: The goal (e.g., "become an AI engineer", "learn prompt engineering")
            current_skills: Optional description of current skills/background
        
        Returns:
            AI-generated learning suggestions
        """
        prompt = f"I want to {goal}."
        
        if current_skills:
            prompt += f"\n\nMy current background: {current_skills}"
        
        prompt += "\n\nWhat should I learn? Please suggest a learning path with specific topics, skills, and resources."
        
        return self.chat(prompt)
    
    def compare_topics(self, topic1: str, topic2: str, context: Optional[str] = None) -> str:
        """
        Compare two learning topics and get advice on which to learn
        
        Args:
            topic1: First topic to compare
            topic2: Second topic to compare
            context: Optional context (e.g., "I want to work in data science")
        
        Returns:
            AI comparison and recommendation
        """
        prompt = f"Should I learn {topic1} or {topic2}?"
        
        if context:
            prompt += f"\n\nContext: {context}"
        
        prompt += "\n\nPlease compare them and give me a recommendation."
        
        return self.chat(prompt)


def render_ai_chat_interface(assistant: AIChatAssistant, key_prefix: str = ""):
    """
    Render Streamlit interface for AI chat
    
    Args:
        assistant: AIChatAssistant instance
        key_prefix: Prefix for widget keys
    """
    if not STREAMLIT_AVAILABLE:
        raise ImportError("streamlit is required for this function")
    
    # Initialize chat history
    history_key = f"{key_prefix}chat_history"
    if history_key not in st.session_state:
        st.session_state[history_key] = []
    
    st.markdown("### 💬 Ask AI Anything About Learning")
    
    # Welcome message (only if no chat history)
    if not st.session_state[history_key]:
        st.info("""
        **Get AI-powered advice on what to learn!**
        
        Ask questions like:
        - "What should I learn to become an AI engineer?"
        - "Is prompt engineering harder than Python?"
        - "What skills do I need for data science?"
        - "How long does it take to master n8n?"
        - "Should I learn React or Vue?"
        """)
        st.markdown("---")
    
    # Display chat history
    if st.session_state[history_key]:
        st.markdown("### 💭 Conversation")
        for msg in st.session_state[history_key]:
            if msg['role'] == 'user':
                with st.chat_message("user"):
                    st.write(msg['content'])
            else:
                with st.chat_message("assistant"):
                    st.write(msg['content'])
        st.markdown("---")
    
    # Input area
    user_message = st.text_area(
        "Type your question here...",
        placeholder="Ask me anything about learning, career, or skills...",
        key=f"{key_prefix}chat_input",
        height=100,
        label_visibility="collapsed"
    )
    
    # Buttons
    col1, col2 = st.columns([4, 1])
    
    with col1:
        send_button = st.button(
            "🚀 Send Message",
            type="primary",
            use_container_width=True,
            key=f"{key_prefix}send_chat"
        )
    
    with col2:
        clear_button = st.button(
            "🗑️ Clear",
            use_container_width=True,
            key=f"{key_prefix}clear_chat"
        )
    
    # Handle clear
    if clear_button:
        st.session_state[history_key] = []
        st.rerun()
    
    # Handle send
    if send_button:
        if user_message.strip():
            # Add user message to history
            st.session_state[history_key].append({
                'role': 'user',
                'content': user_message
            })
            
            # Get AI response
            with st.spinner("🤖 AI is thinking..."):
                try:
                    response = assistant.chat(
                        user_message,
                        conversation_history=st.session_state[history_key]
                    )
                    
                    # Add AI response to history
                    st.session_state[history_key].append({
                        'role': 'assistant',
                        'content': response
                    })
                    
                    st.rerun()
                
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a message first!")
    
    # Quick suggestion buttons
    if not st.session_state[history_key]:
        st.markdown("---")
        st.markdown("**💡 Quick Suggestions:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("What should I learn for AI?", key=f"{key_prefix}suggest1"):
                st.session_state[f"{key_prefix}chat_input"] = "What should I learn to become an AI engineer?"
                st.rerun()
            
            if st.button("Compare two topics", key=f"{key_prefix}suggest2"):
                st.session_state[f"{key_prefix}chat_input"] = "Should I learn Python or JavaScript first?"
                st.rerun()
        
        with col2:
            if st.button("Learning path suggestions", key=f"{key_prefix}suggest3"):
                st.session_state[f"{key_prefix}chat_input"] = "I want to learn prompt engineering. What should I study?"
                st.rerun()
            
            if st.button("Career advice", key=f"{key_prefix}suggest4"):
                st.session_state[f"{key_prefix}chat_input"] = "What skills are most in-demand in tech right now?"
                st.rerun()


# Standalone usage example
if __name__ == "__main__":
    if STREAMLIT_AVAILABLE:
        st.title("🎓 Learning Advisor Chat")
        
        # Initialize assistant
        try:
            assistant = AIChatAssistant()
            render_ai_chat_interface(assistant)
        except ValueError as e:
            st.error(str(e))
            st.info("Please set ANTHROPIC_API_KEY environment variable or configure in Streamlit secrets.")
    else:
        # Non-Streamlit usage
        assistant = AIChatAssistant()
        
        print("AI Learning Advisor Chat")
        print("=" * 50)
        print("Type 'quit' to exit\n")
        
        conversation_history = []
        
        while True:
            user_input = input("\nYou: ")
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            try:
                response = assistant.chat(user_input, conversation_history)
                print(f"\nAI: {response}")
                
                conversation_history.append({"role": "user", "content": user_input})
                conversation_history.append({"role": "assistant", "content": response})
            
            except Exception as e:
                print(f"Error: {e}")

