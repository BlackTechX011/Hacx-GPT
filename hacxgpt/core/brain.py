
import sys
import openai
from typing import Generator
from ..config import Config
from ..ui.interface import UI # Circular dependency potential, careful. 
# Actually Brain shouldn't depend on UI directly if possible, or pass it in.
# The original passed UI to Brain.

class HacxBrain:
    """Handles the connection to the LLM"""

    def __init__(self, api_key: str):
        config = Config.get_provider_config()
        self.model = config["MODEL_NAME"]
        
        # Load System Prompt
        self.system_prompt = Config.load_system_prompt()
        
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=config["BASE_URL"],
            default_headers={
                "HTTP-Referer": "https://github.com/BlackTechX011",
                "X-Title": "HacxGPT-CLI"
            }
        )
        self.history = [{"role": "system", "content": self.system_prompt}]

    def reset(self):
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
            yield "Error: 401 Unauthorized. Check your API Key."
        except Exception as e:
            yield f"Error: Connection Terminated. Reason: {str(e)}"
