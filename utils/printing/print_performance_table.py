from rich.console import Console

from utils.printing.create_metadata_table import create_metadata_table
from utils.printing.print_h2 import print_h2


def print_performance_table(rows: list[tuple[str, str]]) -> None:
    console = Console()
    print_h2("Mock Trading Results")
    console.print(create_metadata_table(rows))
