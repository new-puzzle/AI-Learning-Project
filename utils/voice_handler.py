"""
Voice interface module for GoalPath AI
Provides voice input (speech-to-text) and voice output (text-to-speech)
Using Web Speech API (browser-native, free)
"""

import streamlit as st
from streamlit.components.v1 import html


def render_voice_input_button(key_suffix="", widget_key=None):
    """
    Render a microphone button that enables voice input
    Uses Web Speech API for speech-to-text
    """
    if widget_key is None:
        widget_key = key_suffix
    
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

            // Update status
            document.getElementById('voice-status-{key_suffix}').innerHTML = `✅ Got it: "${{transcript.substring(0, 50)}}..."`;
            
            // Helper to set value safely for React
            function setNativeValue(element, value) {{
                const valueDescriptor = Object.getOwnPropertyDescriptor(element, 'value');
                const prototype = Object.getPrototypeOf(element);
                const prototypeValueDescriptor = Object.getOwnPropertyDescriptor(prototype, 'value');
                
                let setter = null;
                if (prototypeValueDescriptor && prototypeValueDescriptor.set && valueDescriptor !== prototypeValueDescriptor) {{
                    setter = prototypeValueDescriptor.set;
                }} else if (valueDescriptor && valueDescriptor.set) {{
                    setter = valueDescriptor.set;
                }}
                
                if (setter) {{
                    setter.call(element, value);
                }} else {{
                    element.value = value;
                }}
            }}

            // Find target element
            const doc = window.parent.document;
            let target = null;
            
            // 1. Try active element
            if (doc.activeElement && (doc.activeElement.tagName === 'TEXTAREA' || (doc.activeElement.tagName === 'INPUT' && doc.activeElement.type === 'text'))) {{
                target = doc.activeElement;
            }}
            
            // 2. If no active element, find the most likely input
            if (!target) {{
                // Get all text inputs and textareas
                const inputs = Array.from(doc.querySelectorAll('textarea, input[type="text"]'));
                
                // Filter out hidden or disabled ones
                const visibleInputs = inputs.filter(el => {{
                    const style = window.parent.getComputedStyle(el);
                    return style.display !== 'none' && style.visibility !== 'hidden' && !el.disabled;
                }});
                
                if (visibleInputs.length > 0) {{
                    // Prefer empty ones, or the last one (common for chat inputs)
                    // Reverse search for empty
                    for (let i = visibleInputs.length - 1; i >= 0; i--) {{
                        if (!visibleInputs[i].value) {{
                            target = visibleInputs[i];
                            break;
                        }}
                    }}
                    // If all have text, just take the last one
                    if (!target) target = visibleInputs[visibleInputs.length - 1];
                }}
            }}

            if (target) {{
                target.focus();
                
                // 1. Set value using native setter to bypass React's shadowing
                setNativeValue(target, transcript);
                
                // 2. Dispatch events using parent window's constructors
                const InputEvent = window.parent.InputEvent || window.InputEvent;
                const Event = window.parent.Event || window.Event;
                
                target.dispatchEvent(new InputEvent('input', {{ bubbles: true, composed: true }}));
                target.dispatchEvent(new Event('change', {{ bubbles: true }}));
                
                // 3. Direct React Internal Handler Call (Robustness Fix)
                // This finds the internal React props attached to the DOM node and calls onChange directly
                try {{
                    const key = Object.keys(target).find(k => k.startsWith('__reactProps') || k.startsWith('__reactEventHandlers'));
                    if (key && target[key] && target[key].onChange) {{
                        target[key].onChange({{ target: target, currentTarget: target, bubbles: true }});
                    }}
                }} catch (e) {{
                    console.error('React internal handler error:', e);
                }}
                
                // 4. Blur to ensure state commit
                target.blur();
            }}
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
