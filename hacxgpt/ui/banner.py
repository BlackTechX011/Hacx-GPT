
from rich.text import Text
from rich.align import Align
from rich.panel import Panel

class Banner:
    @staticmethod
    def get_ascii_art():
        return """
[bold cyan]██╗  ██╗[/] [bold green] █████╗ [/] [bold cyan]███████╗██╗  ██╗     ██████╗ ██████╗ ████████╗[/]
[bold cyan]██║  ██║[/] [bold green]██╔══██╗[/] [bold cyan]██╔════╝╚██╗██╔╝    ██╔════╝ ██═══██╗╚══██╔══╝[/]
[bold cyan]███████║[/] [bold green]███████║[/] [bold cyan]██║      ╚███╔╝     ██║  ███╗██████╔╝   ██║[/]   
[bold cyan]██╔══██║[/] [bold green]██╔══██║[/] [bold cyan]██║      ██╔██╗     ██║   ██║██╔═       ██║[/]   
[bold cyan]██║  ██║[/] [bold green]██║  ██║[/] [bold cyan]╚██████╗██╔╝ ██╗    ╚██████╔╝██║        ██║[/]   
[bold cyan]╚═╝  ╚═╝[/] [bold green]╚═╝  ╚═╝[/] [bold cyan] ╚═════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝        ╚═╝[/]
        """

    @staticmethod
    def print_banner(console):
        tagline = Text("SYSTEM: UNRESTRICTED | PROTOCOL: ACTIVE", style="bold red blink")
        subline = Text("Developed by BlackTechX", style="dim green")
        
        console.print(Align.center(Banner.get_ascii_art()))
        console.print(Align.center(tagline))
        console.print(Align.center(subline))
        console.print(Panel("", border_style="green", height=1))
