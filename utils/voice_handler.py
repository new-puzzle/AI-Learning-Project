"""
Voice interface module for GoalPath AI
Provides voice input (speech-to-text) and voice output (text-to-speech)
Using Web Speech API (browser-native, free)
"""

import streamlit as st
from streamlit.components.v1 import html


def render_voice_input_button(key_suffix=""):
    """
    Render a microphone button that enables voice input
    Uses Web Speech API for speech-to-text
    """
    html_code = f"""
    <div id="voice-container-{key_suffix}" style="margin: 10px 0;">
        <button id="voice-btn-{key_suffix}" style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            width: 100%;
        " onclick="startVoiceRecognition_{key_suffix}()">
            🎤 Tap to Speak
        </button>
        <div id="voice-status-{key_suffix}" style="
            margin-top: 8px;
            font-size: 0.9rem;
            color: #666;
            text-align: center;
            min-height: 20px;
        "></div>
    </div>

    <script>
    (function() {{
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

        if (!SpeechRecognition) {{
            document.getElementById('voice-status-{key_suffix}').innerHTML = '❌ Voice not supported in this browser';
            document.getElementById('voice-btn-{key_suffix}').disabled = true;
            return;
        }}

        const recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        let isListening = false;

        window.startVoiceRecognition_{key_suffix} = function() {{
            if (isListening) {{
                recognition.stop();
                return;
            }}

            try {{
                recognition.start();
                isListening = true;
                document.getElementById('voice-btn-{key_suffix}').innerHTML = '🎤 Listening...';
                document.getElementById('voice-btn-{key_suffix}').style.background = 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)';
                document.getElementById('voice-status-{key_suffix}').innerHTML = '🎙️ Speak now...';
            }} catch(e) {{
                console.error('Recognition error:', e);
            }}
        }};

        recognition.onresult = function(event) {{
            const transcript = event.results[0][0].transcript;
            const confidence = event.results[0][0].confidence;

            // Find the textarea or input field and populate it
            const textAreas = window.parent.document.querySelectorAll('textarea');
            if (textAreas.length > 0) {{
                // Find the most recently focused or empty textarea
                for (let i = textAreas.length - 1; i >= 0; i--) {{
                    if (!textAreas[i].value || textAreas[i] === document.activeElement) {{
                        textAreas[i].value = transcript;
                        textAreas[i].dispatchEvent(new Event('input', {{ bubbles: true }}));
                        break;
                    }}
                }}
            }}

            document.getElementById('voice-status-{key_suffix}').innerHTML = `✅ Got it: "${{transcript.substring(0, 50)}}..."`;
        }};

        recognition.onerror = function(event) {{
            let errorMsg = '❌ ';
            switch(event.error) {{
                case 'no-speech':
                    errorMsg += 'No speech detected. Try again.';
                    break;
                case 'audio-capture':
                    errorMsg += 'Microphone not found';
                    break;
                case 'not-allowed':
                    errorMsg += 'Microphone permission denied';
                    break;
                default:
                    errorMsg += 'Error: ' + event.error;
            }}
            document.getElementById('voice-status-{key_suffix}').innerHTML = errorMsg;
            isListening = false;
            document.getElementById('voice-btn-{key_suffix}').innerHTML = '🎤 Tap to Speak';
            document.getElementById('voice-btn-{key_suffix}').style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
        }};

        recognition.onend = function() {{
            isListening = false;
            document.getElementById('voice-btn-{key_suffix}').innerHTML = '🎤 Tap to Speak';
            document.getElementById('voice-btn-{key_suffix}').style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
        }};
    }})();
    </script>
    """

    html(html_code, height=100)


def render_voice_output_button(text_to_speak, button_text="🔊 Read Aloud", key_suffix=""):
    """
    Render a speaker button that reads text aloud
    Uses Web Speech API for text-to-speech
    """
    # Clean text for JavaScript (escape quotes and newlines)
    clean_text = text_to_speak.replace("'", "\\'").replace('"', '\\"').replace('\n', ' ')

    html_code = f"""
    <div id="tts-container-{key_suffix}" style="margin: 10px 0;">
        <button id="tts-btn-{key_suffix}" style="
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            width: 100%;
        " onclick="toggleSpeech_{key_suffix}()">
            {button_text}
        </button>
        <div id="tts-status-{key_suffix}" style="
            margin-top: 8px;
            font-size: 0.9rem;
            color: #666;
            text-align: center;
            min-height: 20px;
        "></div>
    </div>

    <script>
    (function() {{
        if (!window.speechSynthesis) {{
            document.getElementById('tts-status-{key_suffix}').innerHTML = '❌ Speech not supported';
            document.getElementById('tts-btn-{key_suffix}').disabled = true;
            return;
        }}

        let isSpeaking = false;
        const textToSpeak = `{clean_text}`;

        window.toggleSpeech_{key_suffix} = function() {{
            if (isSpeaking) {{
                window.speechSynthesis.cancel();
                isSpeaking = false;
                document.getElementById('tts-btn-{key_suffix}').innerHTML = '🔊 Read Aloud';
                document.getElementById('tts-btn-{key_suffix}').style.background = 'linear-gradient(135deg, #11998e 0%, #38ef7d 100%)';
                document.getElementById('tts-status-{key_suffix}').innerHTML = '';
                return;
            }}

            const utterance = new SpeechSynthesisUtterance(textToSpeak);
            utterance.rate = 1.0;
            utterance.pitch = 1.0;
            utterance.volume = 1.0;
            utterance.lang = 'en-US';

            utterance.onstart = function() {{
                isSpeaking = true;
                document.getElementById('tts-btn-{key_suffix}').innerHTML = '⏸️ Stop';
                document.getElementById('tts-btn-{key_suffix}').style.background = 'linear-gradient(135deg, #eb3349 0%, #f45c43 100%)';
                document.getElementById('tts-status-{key_suffix}').innerHTML = '🔊 Speaking...';
            }};

            utterance.onend = function() {{
                isSpeaking = false;
                document.getElementById('tts-btn-{key_suffix}').innerHTML = '🔊 Read Aloud';
                document.getElementById('tts-btn-{key_suffix}').style.background = 'linear-gradient(135deg, #11998e 0%, #38ef7d 100%)';
                document.getElementById('tts-status-{key_suffix}').innerHTML = '✅ Finished';
                setTimeout(() => {{
                    document.getElementById('tts-status-{key_suffix}').innerHTML = '';
                }}, 2000);
            }};

            utterance.onerror = function(event) {{
                isSpeaking = false;
                document.getElementById('tts-btn-{key_suffix}').innerHTML = '🔊 Read Aloud';
                document.getElementById('tts-btn-{key_suffix}').style.background = 'linear-gradient(135deg, #11998e 0%, #38ef7d 100%)';
                document.getElementById('tts-status-{key_suffix}').innerHTML = '❌ Error: ' + event.error;
            }};

            window.speechSynthesis.speak(utterance);
        }};
    }})();
    </script>
    """

    html(html_code, height=100)


def render_voice_settings(key_prefix=""):
    """
    Render voice settings controls

    Args:
        key_prefix: Optional prefix for widget keys to avoid duplicates
    """
    st.markdown("### 🎙️ Voice Settings")

    col1, col2 = st.columns(2)

    with col1:
        st.checkbox(
            "Auto-read AI responses",
            value=st.session_state.get('auto_read_responses', False),
            key=f'{key_prefix}auto_read_responses',
            help="Automatically read AI responses aloud"
        )

    with col2:
        st.checkbox(
            "Enable voice input",
            value=st.session_state.get('voice_input_enabled', True),
            key=f'{key_prefix}voice_input_enabled',
            help="Show voice input buttons"
        )

    st.caption("💡 Voice features use your browser's built-in speech engine (free, works offline)")
    st.caption("🌐 Supported: Chrome, Safari, Edge | Best on: Chrome Desktop & Mobile")
