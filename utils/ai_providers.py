"""
Multi-Model AI Provider System
Supports Claude, OpenAI, Gemini, DeepSeek, Mistral, and Qwen
Implements silent failure for missing API keys
"""

import os
from typing import Dict, List, Optional, Any
from abc import ABC, abstractmethod
import json


class AIProvider(ABC):
    """Base class for all AI providers"""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.is_configured = self.check_configuration()

    @abstractmethod
    def check_configuration(self) -> bool:
        """Check if the provider is properly configured"""
        pass

    @abstractmethod
    def generate_text(self, prompt: str, system_prompt: str = "", max_tokens: int = 2000) -> str:
        """Generate text response"""
        pass

    @abstractmethod
    def analyze_image(self, image_data: bytes, prompt: str) -> str:
        """Analyze an image (if supported)"""
        pass

    def supports_vision(self) -> bool:
        """Check if provider supports image analysis"""
        return False


class ClaudeProvider(AIProvider):
    """Anthropic Claude provider"""

    MODELS = {
        "Claude Sonnet 4.5": "claude-sonnet-4-5-20250929",
        "Claude Sonnet 3.5": "claude-3-5-sonnet-20241022",
        "Claude Haiku": "claude-3-5-haiku-20241022"
    }

    def __init__(self, api_key: Optional[str] = None, model_name: str = "Claude Sonnet 4.5"):
        self.model_name = model_name
        # Try to get API key from: 1) parameter, 2) streamlit secrets, 3) environment variable
        if not api_key:
            try:
                import streamlit as st
                api_key = st.secrets.get("ANTHROPIC_API_KEY")
            except:
                api_key = os.getenv("ANTHROPIC_API_KEY")
        super().__init__(api_key)

    def check_configuration(self) -> bool:
        return bool(self.api_key and self.api_key != "your_api_key_here")

    def generate_text(self, prompt: str, system_prompt: str = "", max_tokens: int = 2000) -> str:
        if not self.is_configured:
            raise ValueError("Claude API key not configured")

        import anthropic
        client = anthropic.Anthropic(api_key=self.api_key)
        model = self.MODELS.get(self.model_name, self.MODELS["Claude Sonnet 4.5"])

        messages = [{"role": "user", "content": prompt}]

        if system_prompt:
            response = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system_prompt,
                messages=messages
            )
        else:
            response = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                messages=messages
            )

        return response.content[0].text

    def analyze_image(self, image_data: bytes, prompt: str) -> str:
        if not self.is_configured:
            raise ValueError("Claude API key not configured")

        import anthropic
        import base64

        client = anthropic.Anthropic(api_key=self.api_key)
        model = self.MODELS.get(self.model_name, self.MODELS["Claude Sonnet 4.5"])

        # Encode image to base64
        image_base64 = base64.b64encode(image_data).decode('utf-8')

        # Detect image type (assume PNG, could be enhanced)
        image_type = "image/png"
        if image_data[:4] == b'\xff\xd8\xff\xe0':
            image_type = "image/jpeg"

        response = client.messages.create(
            model=model,
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": image_type,
                            "data": image_base64
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }]
        )

        return response.content[0].text

    def supports_vision(self) -> bool:
        return True


class OpenAIProvider(AIProvider):
    """OpenAI provider"""

    MODELS = {
        "GPT-4": "gpt-4",
        "GPT-4 Turbo": "gpt-4-turbo-preview",
        "GPT-3.5 Turbo": "gpt-3.5-turbo",
        "GPT-4 Vision": "gpt-4-vision-preview"
    }

    def __init__(self, api_key: Optional[str] = None, model_name: str = "GPT-4 Turbo"):
        self.model_name = model_name
        super().__init__(api_key or os.getenv("OPENAI_API_KEY"))

    def check_configuration(self) -> bool:
        return bool(self.api_key and self.api_key != "your_api_key_here")

    def generate_text(self, prompt: str, system_prompt: str = "", max_tokens: int = 2000) -> str:
        if not self.is_configured:
            raise ValueError("OpenAI API key not configured")

        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("OpenAI package not installed. Run: pip install openai")

        client = OpenAI(api_key=self.api_key)
        model = self.MODELS.get(self.model_name, self.MODELS["GPT-4 Turbo"])

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content

    def analyze_image(self, image_data: bytes, prompt: str) -> str:
        if not self.is_configured:
            raise ValueError("OpenAI API key not configured")

        try:
            from openai import OpenAI
            import base64
        except ImportError:
            raise ImportError("OpenAI package not installed. Run: pip install openai")

        client = OpenAI(api_key=self.api_key)

        # Encode image to base64
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        image_url = f"data:image/png;base64,{image_base64}"

        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_url}}
                ]
            }],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def supports_vision(self) -> bool:
        return True


class GeminiProvider(AIProvider):
    """Google Gemini provider"""

    MODELS = {
        "Gemini 2.5 Pro": "gemini-2.5-pro",
        "Gemini 2.5 Flash": "gemini-2.5-flash",
        "Gemini 3.0 Pro (Preview)": "gemini-3-pro-preview",
        "Gemini 2.5 Flash Lite": "gemini-2.5-flash-lite"
    }

    def __init__(self, api_key: Optional[str] = None, model_name: str = "Gemini 2.5 Flash"):
        self.model_name = model_name
        super().__init__(api_key or os.getenv("GOOGLE_API_KEY"))

    def check_configuration(self) -> bool:
        return bool(self.api_key and self.api_key != "your_api_key_here")

    def generate_text(self, prompt: str, system_prompt: str = "", max_tokens: int = 2000) -> str:
        if not self.is_configured:
            raise ValueError("Google API key not configured")

        try:
            import google.generativeai as genai
        except ImportError:
            raise ImportError("Google Generative AI package not installed. Run: pip install google-generativeai")

        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(self.MODELS.get(self.model_name, self.MODELS["Gemini 2.5 Flash"]))

        full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
        response = model.generate_content(full_prompt)

        return response.text

    def analyze_image(self, image_data: bytes, prompt: str) -> str:
        if not self.is_configured:
            raise ValueError("Google API key not configured")

        try:
            import google.generativeai as genai
            from PIL import Image
            import io
        except ImportError:
            raise ImportError("Required packages not installed. Run: pip install google-generativeai pillow")

        genai.configure(api_key=self.api_key)
        # Gemini 2.5 models support vision natively
        model = genai.GenerativeModel(self.MODELS.get(self.model_name, self.MODELS["Gemini 2.5 Flash"]))

        # Convert bytes to PIL Image
        image = Image.open(io.BytesIO(image_data))

        response = model.generate_content([prompt, image])
        return response.text

    def supports_vision(self) -> bool:
        return True


class DeepSeekProvider(AIProvider):
    """DeepSeek provider with OCR support"""

    MODELS = {
        "DeepSeek Chat": "deepseek-chat",
        "DeepSeek Coder": "deepseek-coder"
    }

    def __init__(self, api_key: Optional[str] = None, model_name: str = "DeepSeek Chat"):
        self.model_name = model_name
        super().__init__(api_key or os.getenv("DEEPSEEK_API_KEY"))

    def check_configuration(self) -> bool:
        return bool(self.api_key and self.api_key != "your_api_key_here")

    def generate_text(self, prompt: str, system_prompt: str = "", max_tokens: int = 2000) -> str:
        if not self.is_configured:
            raise ValueError("DeepSeek API key not configured")

        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("OpenAI package not installed. Run: pip install openai")

        # DeepSeek uses OpenAI-compatible API
        client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.deepseek.com"
        )

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model=self.MODELS.get(self.model_name, self.MODELS["DeepSeek Chat"]),
            messages=messages,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content

    def analyze_image(self, image_data: bytes, prompt: str) -> str:
        """Use OCR capabilities for image analysis"""
        if not self.is_configured:
            raise ValueError("DeepSeek API key not configured")

        # DeepSeek doesn't have native vision, but we can use OCR
        try:
            import pytesseract
            from PIL import Image
            import io
        except ImportError:
            raise ImportError("OCR packages not installed. Run: pip install pytesseract pillow")

        # Extract text from image using OCR
        image = Image.open(io.BytesIO(image_data))
        extracted_text = pytesseract.image_to_string(image)

        # Use the extracted text with DeepSeek
        full_prompt = f"{prompt}\n\nExtracted text from image:\n{extracted_text}"
        return self.generate_text(full_prompt)

    def supports_vision(self) -> bool:
        return True  # Via OCR


class MistralProvider(AIProvider):
    """Mistral AI provider"""

    MODELS = {
        "Mistral Large": "mistral-large-latest",
        "Mistral Medium": "mistral-medium-latest",
        "Mistral Small": "mistral-small-latest"
    }

    def __init__(self, api_key: Optional[str] = None, model_name: str = "Mistral Large"):
        self.model_name = model_name
        super().__init__(api_key or os.getenv("MISTRAL_API_KEY"))

    def check_configuration(self) -> bool:
        return bool(self.api_key and self.api_key != "your_api_key_here")

    def generate_text(self, prompt: str, system_prompt: str = "", max_tokens: int = 2000) -> str:
        if not self.is_configured:
            raise ValueError("Mistral API key not configured")

        try:
            from mistralai.client import MistralClient
            from mistralai.models.chat_completion import ChatMessage
        except ImportError:
            raise ImportError("Mistral package not installed. Run: pip install mistralai")

        client = MistralClient(api_key=self.api_key)

        messages = []
        if system_prompt:
            messages.append(ChatMessage(role="system", content=system_prompt))
        messages.append(ChatMessage(role="user", content=prompt))

        response = client.chat(
            model=self.MODELS.get(self.model_name, self.MODELS["Mistral Large"]),
            messages=messages,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content

    def analyze_image(self, image_data: bytes, prompt: str) -> str:
        raise NotImplementedError("Mistral does not support image analysis")

    def supports_vision(self) -> bool:
        return False


class QwenProvider(AIProvider):
    """Qwen provider"""

    MODELS = {
        "Qwen Turbo": "qwen-turbo",
        "Qwen Plus": "qwen-plus",
        "Qwen Max": "qwen-max"
    }

    def __init__(self, api_key: Optional[str] = None, model_name: str = "Qwen Plus"):
        self.model_name = model_name
        super().__init__(api_key or os.getenv("QWEN_API_KEY"))

    def check_configuration(self) -> bool:
        return bool(self.api_key and self.api_key != "your_api_key_here")

    def generate_text(self, prompt: str, system_prompt: str = "", max_tokens: int = 2000) -> str:
        if not self.is_configured:
            raise ValueError("Qwen API key not configured")

        try:
            import dashscope
            from dashscope import Generation
        except ImportError:
            raise ImportError("DashScope package not installed. Run: pip install dashscope")

        dashscope.api_key = self.api_key

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = Generation.call(
            model=self.MODELS.get(self.model_name, self.MODELS["Qwen Plus"]),
            messages=messages,
            result_format='message'
        )

        return response.output.choices[0].message.content

    def analyze_image(self, image_data: bytes, prompt: str) -> str:
        raise NotImplementedError("Qwen does not support image analysis in this implementation")

    def supports_vision(self) -> bool:
        return False


class AIProviderManager:
    """Manager for all AI providers with silent failure support"""

    # All available providers and their models
    PROVIDERS = {
        "Claude": {
            "class": ClaudeProvider,
            "models": ["Claude Sonnet 4.5", "Claude Sonnet 3.5", "Claude Haiku"],
            "supports_vision": True
        },
        "OpenAI": {
            "class": OpenAIProvider,
            "models": ["GPT-4 Turbo", "GPT-4", "GPT-3.5 Turbo", "GPT-4 Vision"],
            "supports_vision": True
        },
        "Google Gemini": {
            "class": GeminiProvider,
            "models": ["Gemini 2.5 Flash", "Gemini 2.5 Pro", "Gemini 3.0 Pro (Preview)", "Gemini 2.5 Flash Lite"],
            "supports_vision": True
        },
        "DeepSeek": {
            "class": DeepSeekProvider,
            "models": ["DeepSeek Chat", "DeepSeek Coder"],
            "supports_vision": True  # Via OCR
        },
        "Mistral": {
            "class": MistralProvider,
            "models": ["Mistral Large", "Mistral Medium", "Mistral Small"],
            "supports_vision": False
        },
        "Qwen": {
            "class": QwenProvider,
            "models": ["Qwen Plus", "Qwen Turbo", "Qwen Max"],
            "supports_vision": False
        }
    }

    def __init__(self):
        self.providers = {}
        self._initialize_providers()

    def _initialize_providers(self):
        """Initialize all providers (silently fail if not configured)"""
        for provider_name, config in self.PROVIDERS.items():
            try:
                provider_class = config["class"]
                provider = provider_class()
                self.providers[provider_name] = {
                    "instance": provider,
                    "configured": provider.is_configured,
                    "models": config["models"],
                    "supports_vision": config["supports_vision"]
                }
            except Exception as e:
                # Silent failure - provider not available
                self.providers[provider_name] = {
                    "instance": None,
                    "configured": False,
                    "models": config["models"],
                    "supports_vision": config["supports_vision"],
                    "error": str(e)
                }

    def get_available_models(self) -> Dict[str, List[str]]:
        """Get all models grouped by provider (including unconfigured)"""
        models = {}
        for provider_name, data in self.providers.items():
            models[provider_name] = {
                "models": data["models"],
                "configured": data["configured"],
                "supports_vision": data["supports_vision"]
            }
        return models

    def get_provider(self, provider_name: str, model_name: str) -> Optional[AIProvider]:
        """Get a specific provider instance"""
        if provider_name not in self.providers:
            return None

        provider_data = self.providers[provider_name]
        if not provider_data["configured"]:
            return None

        # Create new instance with specific model
        provider_class = self.PROVIDERS[provider_name]["class"]
        return provider_class(model_name=model_name)

    def generate_text(self, provider_name: str, model_name: str, prompt: str,
                     system_prompt: str = "", max_tokens: int = 2000) -> str:
        """Generate text using specified provider and model"""
        provider = self.get_provider(provider_name, model_name)
        if not provider:
            raise ValueError(f"{provider_name} is not configured. Please add API key to .env file.")

        return provider.generate_text(prompt, system_prompt, max_tokens)

    def analyze_image(self, provider_name: str, model_name: str,
                     image_data: bytes, prompt: str) -> str:
        """Analyze image using specified provider"""
        provider = self.get_provider(provider_name, model_name)
        if not provider:
            raise ValueError(f"{provider_name} is not configured. Please add API key to .env file.")

        if not provider.supports_vision():
            raise ValueError(f"{provider_name} does not support image analysis")

        return provider.analyze_image(image_data, prompt)


def get_available_providers() -> Dict[str, Any]:
    """Get a dictionary of all available providers with their instances"""
    manager = AIProviderManager()
    providers = {}
    for provider_name, data in manager.providers.items():
        if data["configured"]:
            providers[provider_name] = data["instance"]
    return providers