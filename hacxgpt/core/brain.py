
import sys
import openai
from typing import Generator
from ..config import Config
from ..ui.interface import UI 


class HacxBrain:
    """Handles the connection to the LLM"""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.model = Config.get_model()
        self.system_prompt = Config.load_system_prompt()
        self._init_client()
        
        # HacxGPT models don't need the system prompt history
        if Config.is_hacxgpt_model(self.model):
            self.history = []
        else:
            self.history = [{"role": "system", "content": self.system_prompt}]

    def _init_client(self):
        config = Config.get_provider_config()
        
        base_url = config.get("BASE_URL")
        api_key = self.api_key
        
        # Handle dynamic templates (e.g., for HacxGPT Internal)
        if "BASE_URL_TEMPLATE" in config:
            base_url = config["BASE_URL_TEMPLATE"].format(
                key=self.api_key,
                port=Config.INTERNAL_PORT
            )
            api_key = "HacxGPT" # Placeholder for internal API

        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url,
            default_headers={
                "HTTP-Referer": "https://github.com/BlackTechX011",
                "X-Title": "HacxGPT-CLI"
            }
        )

    def set_model(self, model_name: str):
        """Update the model being used"""
        self.model = model_name
        Config.ACTIVE_MODEL = model_name
        # If switching between HacxGPT and normal models, a reset might be best, 
        # but we'll try to just remove/add the system prompt if the history is fresh.
        if len(self.history) <= 1:
            self.reset()

    def set_provider(self, provider_name: str, api_key: str):
        """Update provider and re-init client"""
        Config.ACTIVE_PROVIDER = provider_name
        Config.ACTIVE_MODEL = None # Reset model to provider default
        self.api_key = api_key
        self.model = Config.get_model()
        self._init_client()
        self.reset() # Reset history on provider switch for safety

    def reset(self):
        if Config.is_hacxgpt_model(self.model):
            self.history = []
        else:
            self.history = [{"role": "system", "content": self.system_prompt}]
        
    def chat(self, user_input: str) -> Generator[str, None, None]:
        self.history.append({"role": "user", "content": user_input})
        
        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=self.history,
                stream=True,
                temperature=0.75
            )
            
            full_content = ""
            for chunk in stream:
                content = chunk.choices[0].delta.content
                if content:
                    full_content += content
                    yield content
            
            self.history.append({"role": "assistant", "content": full_content})
            
        except openai.AuthenticationError:
            yield f"Error: 401 Unauthorized for {Config.ACTIVE_PROVIDER.upper()}. Check your API Key."
        except Exception as e:
            yield f"Error: Connection Terminated. Reason: {str(e)}"
