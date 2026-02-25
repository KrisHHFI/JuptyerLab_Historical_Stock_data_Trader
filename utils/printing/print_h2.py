from rich.console import Console


console = Console()


def print_h2(title: str) -> None:
    console.print(f"[bold cyan]{title}[/bold cyan] [cyan]{'─' * 40}[/cyan]")
