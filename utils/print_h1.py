from rich.console import Console


console = Console()


def print_h1(title: str) -> None:
    console.rule(f"[bold cyan]{title}[/bold cyan]")
