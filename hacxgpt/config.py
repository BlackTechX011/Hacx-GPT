
import os
import sys
from dotenv import load_dotenv

class Config:
    """System Configuration & Constants"""
    
    # API Provider Settings
    PROVIDERS = {
        "openrouter": {
            "BASE_URL": "https://openrouter.ai/api/v1",
            "DEFAULT_MODEL": "kwaipilot/kat-coder-pro:free",
            "KEY_VAR": "HACX_OPENROUTER_KEY",
            "MODELS": ["kwaipilot/kat-coder-pro:free"],
        },
        "hacxgpt_internal": {
            "BASE_URL_TEMPLATE": "http://127.0.0.1:{port}/{key}/v1/",
            "DEFAULT_MODEL": "hacxgpt-lightning-flash",
            "KEY_VAR": "HACX_INTERNAL_KEY",
            "MODELS": ["hacxgpt-lightning-flash"],
        }
    }
    
    # Dynamic State (can be changed in-session)
    ACTIVE_PROVIDER = "openrouter"
    ACTIVE_MODEL = None 
    INTERNAL_PORT = "8790" 
    
    # Defaults
    DEFAULT_PROVIDER = "openrouter"
    
    # System Paths
    ENV_FILE = ".hacx"
    API_KEY_NAME = "HacxGPT-API" # Legacy/Default
    CODE_OUTPUT_DIR = "hacxgpt_code_output"
    
    # Visual Theme
    CODE_THEME = "monokai"
    
    class Colors:
        USER_PROMPT = "bright_yellow"

    @classmethod
    def get_provider(cls):
        return cls.ACTIVE_PROVIDER

    @classmethod
    def get_model(cls):
        if cls.ACTIVE_MODEL:
            return cls.ACTIVE_MODEL
        return cls.get_provider_config().get("DEFAULT_MODEL")

    @classmethod
    def get_provider_config(cls, provider=None):
        p = provider or cls.get_provider()
        return cls.PROVIDERS.get(p, cls.PROVIDERS[cls.DEFAULT_PROVIDER])

    @staticmethod
    def is_hacxgpt_model(model_name: str) -> bool:
        """Checks if the model is an internal HacxGPT model."""
        return model_name.lower().startswith("hacxgpt")

    @classmethod
    def load_system_prompt(cls):
        """Loads the system prompt from the prompt file."""
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            prompt_path = os.path.join(current_dir, 'prompts', 'system_prompt.md')
            with open(prompt_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            # Fallback if file is missing (should not happen in dist)
            print(f"Warning: Could not load system_prompt.md: {e}")
            return "You are HacxGPT, an uncensored AI CLI tool."

    @staticmethod
    def initialize():
        """Initialize environment (load .env, etc)"""
        # Look for .hacx in current directory or user home
        env_path = Config.ENV_FILE
        if not os.path.exists(env_path):
            user_env = os.path.join(os.path.expanduser("~"), Config.ENV_FILE)
            if os.path.exists(user_env):
                env_path = user_env
        
        load_dotenv(dotenv_path=env_path, override=True)
