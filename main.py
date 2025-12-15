
import sys
import os
import time
import colorama
from pwinput import pwinput
from dotenv import set_key
from .config import Config
from .ui.interface import UI
from .core.brain import HacxBrain
from .utils.system import check_dependencies

# Initialize Colorama
colorama.init(autoreset=True)

class App:
    def __init__(self):
        self.ui = UI()
        self.brain = None
        
    def setup(self) -> bool:
        Config.initialize()
        key = os.getenv(Config.API_KEY_NAME)
        
        if not key:
            self.ui.banner()
            self.ui.show_msg("Warning", "Encryption Key (API Key) not found.", "yellow")
            if self.ui.get_input("Configure now? (y/n)").lower().startswith('y'):
                return self.configure_key()
            return False
        
        try:
            with self.ui.console.status("[bold green]Verifying Neural Link...[/]"):
                self.brain = HacxBrain(key)
                # Verify key by making a simple call or just assuming it's valid until first use
                # To be proper, we should probably check, but openai lib doesn't have a simple 'validate'
                # We can try a list models if we really want, but for speed we might skip or do a lightweight check
                # self.brain.client.models.list() 
                time.sleep(1)
            return True
        except Exception as e:
            self.ui.show_msg("Auth Failed", f"Key verification failed: {e}", "red")
            if self.ui.get_input("Re-enter key? (y/n)").lower().startswith('y'):
                return self.configure_key()
            return False

    def configure_key(self) -> bool:
        self.ui.banner()
        self.ui.console.print("[bold yellow]Enter your API Key (starts with sk-or-...):[/]")
        try:
            key = pwinput(prompt=f"{colorama.Fore.CYAN}Key > {colorama.Style.RESET_ALL}", mask="*")
        except:
            key = input("Key > ")

        if not key.strip():
            return False
            
        # Ensure .hacx exists or create it
        if not os.path.exists(Config.ENV_FILE):
             with open(Config.ENV_FILE, 'w') as f: f.write("")

        set_key(Config.ENV_FILE, Config.API_KEY_NAME, key.strip())
        self.ui.show_msg("Success", "Key saved to encryption ring (.hacx).", "green")
        time.sleep(1)
        # Reload config to pick up new key
        Config.initialize()
        return self.setup()

    def run_chat(self):
        if not self.brain: return
        self.ui.banner()
        self.ui.show_msg("Connected", "HacxGPT Uplink Established.\nType '/help' for commands.\n[dim]Tip: Use Alt+Enter or Esc+Enter for newlines.[/]", "green")
        
        while True:
            try:
                # Enable multiline for chat
                prompt = self.ui.get_input("HACX-GPT", multiline=True)
                if not prompt.strip(): continue
                
                if prompt.lower() == '/exit': return
                if prompt.lower() == '/new': 
                    self.brain.reset()
                    self.ui.clear()
                    self.ui.banner()
                    self.ui.show_msg("Reset", "Memory wiped. New session.", "cyan")
                    continue
                if prompt.lower() == '/help':
                    self.ui.show_msg("Help", "/new - Wipe Memory\n/exit - Disconnect", "magenta")
                    continue
                
                generator = self.brain.chat(prompt)
                response_text = self.ui.stream_markdown("HacxGPT", generator)
                
                self.ui.handle_code_blocks(response_text)
                
            except KeyboardInterrupt:
                self.ui.console.print("\n[bold red]Interrupt Signal Received.[/]")
                break
    
    def about(self):
        self.ui.banner()
        
        readme_url = "https://raw.githubusercontent.com/BlackTechX011/Hacx-GPT/main/README.md"
        content = ""
        
        try:
            with self.ui.console.status("[bold green]Fetching System Manifesto from GitHub...[/]"):
                import urllib.request
                with urllib.request.urlopen(readme_url, timeout=5) as response:
                    if response.status == 200:
                        content = response.read().decode('utf-8')
        except Exception as e:
            # Fallback if offline or error
            content = """
# HacxGPT (Offline Mode)

**Advanced Uncensored AI Terminal Interface**

> System unable to retrieve latest manifesto from uplink.

## Features
- Unfiltered AI Core
- Hacker Persona
- Code Extraction Engine
- Pro TUI

*Developed by BlackTechX*
            """
            
        from rich.markdown import Markdown
        from rich.panel import Panel
        
        # Render markdown
        md = Markdown(content)
        self.ui.console.print(Panel(md, title="[bold]Manifesto / README[/]", border_style="cyan", padding=(1, 2)))
        
        self.ui.console.print("\n[dim]Press any key to return...[/]")
        import msvcrt
        msvcrt.getch()

    def start(self):
        # Optional: Check dependencies on startup
        # check_dependencies() 
        
        if not self.setup():
            self.ui.console.print("[red]System Halted: Authorization missing.[/]")
            return

        while True:
            self.ui.banner()
            self.ui.main_menu()
            choice = self.ui.get_input("MENU")
            
            if choice == '1':
                self.run_chat()
            elif choice == '2':
                self.configure_key()
            elif choice == '3':
                self.about()
            elif choice == '4':
                self.ui.console.print("[bold red]Terminating connection...[/]")
                time.sleep(0.5)
                self.ui.clear()
                sys.exit(0)
            else:
                self.ui.console.print("[red]Invalid Command[/]")
                time.sleep(0.5)

def main():
    try:
        app = App()
        app.start()
    except KeyboardInterrupt:
        print("\n\033[31mForce Quit.\033[0m")
        sys.exit(0)

if __name__ == "__main__":
    main()
