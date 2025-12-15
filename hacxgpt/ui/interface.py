
import os
import time
import pyperclip
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.live import Live
from rich.table import Table
from rich.spinner import Spinner
from rich.align import Align
from ..config import Config
from ..core.extractor import CodeExtractor
from .banner import Banner

class UI:
    """Advanced Terminal User Interface using Rich"""
    
    def __init__(self):
        self.console = Console()
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def banner(self):
        self.clear()
        Banner.print_banner(self.console)

    def main_menu(self):
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Icon", style="bold yellow", justify="right")
        table.add_column("Option", style="bold white")
        
        table.add_row("[1]", "Initialize Uplink (Start Chat)")
        table.add_row("[2]", "Configure Security Keys (API Setup)")
        table.add_row("[3]", "System Manifesto (About)")
        table.add_row("[4]", "Terminate Session (Exit)")
        
        panel = Panel(
            Align.center(table),
            title="[bold cyan]MAIN MENU[/bold cyan]",
            border_style="bright_blue",
            padding=(1, 5)
        )
        self.console.print(panel)

    def show_msg(self, title: str, content: str, color: str = "white"):
        self.console.print(Panel(content, title=f"[bold]{title}[/]", border_style=color))

    def get_input(self, label: str = "COMMAND") -> str:
        prompt_style = Config.Colors.USER_PROMPT
        self.console.print(f"[{prompt_style}]┌──({label})-[~][/]")
        return self.console.input(f"[{prompt_style}]└─> [/]")

    def stream_markdown(self, title: str, content_generator):
        """
        Renders Markdown content in real-time as it streams.
        """
        full_response = ""
        
        with Live(
            Panel(Spinner("dots", text="Decryption in progress..."), title=title, border_style="cyan"),
            console=self.console,
            refresh_per_second=12,
            transient=False 
        ) as live:
            
            for chunk in content_generator:
                full_response += chunk
                
                # Clean format for display
                display_text = full_response.replace("[HacxGPT]:", "").replace("[CODE]:", "").strip()
                if not display_text: display_text = "..." 

                md = Markdown(display_text, code_theme=Config.CODE_THEME)
                
                live.update(
                    Panel(
                        md, 
                        title=f"[bold cyan]{title}[/bold cyan] [dim](Stream Active)[/dim]", 
                        border_style="cyan"
                    )
                )
            
            display_text = full_response.replace("[HacxGPT]:", "").replace("[CODE]:", "").strip()
            live.update(
                Panel(
                    Markdown(display_text, code_theme=Config.CODE_THEME), 
                    title=f"[bold green]{title}[/bold green] [bold]✓[/]", 
                    border_style="green"
                )
            )
        
        return full_response

    def handle_code_blocks(self, response_text: str):
        """Handle code block extraction and user actions with Pro UI"""
        code_blocks = CodeExtractor.extract_code_blocks(response_text)
        
        if not code_blocks:
            return
        
        self.console.print(Panel(f"[bold yellow]🔍 Detected {len(code_blocks)} code block(s)[/]", border_style="yellow"))
        
        # Display code blocks info
        table = Table(show_header=True, header_style="bold magenta", border_style="dim white", expand=True)
        table.add_column("#", style="cyan", justify="center", width=4)
        table.add_column("Language", style="green")
        table.add_column("Preview", style="dim white")
        table.add_column("Lines", style="yellow", justify="right")
        
        for idx, (lang, code) in enumerate(code_blocks, 1):
            lines = code.split('\n')
            preview = lines[0].strip()[:50] + "..." if len(lines[0]) > 50 else lines[0].strip()
            table.add_row(str(idx), lang.upper(), preview, str(len(lines)))
        
        self.console.print(table)
        
        # Pro Menu
        menu_text = """
[bold cyan]Options:[/bold cyan]
[bold green][1][/] Save All    [bold green][2][/] Copy All    [bold green][3][/] Save One    [bold green][4][/] Copy One    [bold red][SEMICOLON/Space][/] Skip
"""
        self.console.print(Panel(menu_text.strip(), border_style="blue", title="[bold]Action Menu[/]"))
        self.console.print("[dim]Press the corresponding key...[/]")

        while True:
            import msvcrt
            key = msvcrt.getch()
            try:
                char = key.decode("utf-8").lower()
            except:
                continue

            if char == '1':
                self._save_all_blocks(code_blocks)
                break
            elif char == '2':
                self._copy_all_blocks(code_blocks)
                break
            elif char == '3':
                self._save_specific_block_interactive(code_blocks)
                break
            elif char == '4':
                self._copy_specific_block_interactive(code_blocks)
                break
            elif char == ' ' or char == ';':
                self.console.print("[yellow]Skipped.[/]")
                break

    def _save_specific_block_interactive(self, code_blocks):
        self.console.print("[bold cyan]Press the number of the block to save (1-9)...[/]")
        while True:
            import msvcrt
            key = msvcrt.getch()
            try:
                char = key.decode("utf-8")
                if char.isdigit() and 1 <= int(char) <= len(code_blocks):
                    idx = int(char) - 1
                    lang, code = code_blocks[idx]
                    filepath = CodeExtractor.save_code_block(code, lang, idx)
                    self.console.print(f"[bold green]✓ Saved Block {char} to: {filepath}[/]")
                    break
            except:
                pass

    def _copy_specific_block_interactive(self, code_blocks):
        self.console.print("[bold cyan]Press the number of the block to copy (1-9)...[/]")
        while True:
            import msvcrt
            key = msvcrt.getch()
            try:
                char = key.decode("utf-8")
                if char.isdigit() and 1 <= int(char) <= len(code_blocks):
                    idx = int(char) - 1
                    lang, code = code_blocks[idx]
                    pyperclip.copy(code)
                    self.console.print(f"[bold green]✓ Block {char} copied to clipboard![/]")
                    break
            except:
                pass
