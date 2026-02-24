from rich.console import Console


console = Console()


def print_subheader(title: str) -> None:
    console.print(f"[bold cyan]{title}[/bold cyan]")
