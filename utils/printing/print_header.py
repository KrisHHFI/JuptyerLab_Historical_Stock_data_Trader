from rich.console import Console


console = Console()


def print_header(title: str) -> None:
    console.rule(f"[bold cyan]{title}[/bold cyan]")
