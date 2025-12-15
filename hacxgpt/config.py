
import os
import sys
from dotenv import load_dotenv

class Config:
    """System Configuration & Constants"""
    
    # API Provider Settings
    PROVIDERS = {
        "openrouter": {
            "BASE_URL": "https://openrouter.ai/api/v1",
            "MODEL_NAME": "kwaipilot/kat-coder-pro:free", # good model
        },
        "deepseek": {
            "BASE_URL": "https://api.deepseek.com",
            "MODEL_NAME": "deepseek-chat",
        },
    }
    
    # Defaults
    DEFAULT_PROVIDER = "openrouter"
    
    # System Paths
    ENV_FILE = ".hacx"
    API_KEY_NAME = "HacxGPT-API"
    CODE_OUTPUT_DIR = "hacxgpt_code_output"
    
    # Visual Theme
    CODE_THEME = "monokai"
    
    class Colors:
        USER_PROMPT = "bright_yellow"

    @classmethod
    def get_provider(cls):
        return os.getenv("HACX_PROVIDER", cls.DEFAULT_PROVIDER)

    @classmethod
    def get_provider_config(cls):
        provider = cls.get_provider()
        if provider not in cls.PROVIDERS:
            return cls.PROVIDERS[cls.DEFAULT_PROVIDER]
        return cls.PROVIDERS[provider]

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
        
        load_dotenv(dotenv_path=env_path)
