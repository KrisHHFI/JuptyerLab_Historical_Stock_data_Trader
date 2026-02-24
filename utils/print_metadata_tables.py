from rich.console import Console

from utils.create_metadata_table import create_metadata_table
from utils.print_h2 import print_h2


def print_metadata_tables(
    file_metadata_rows: list[tuple[str, str]], stock_metadata_rows: list[tuple[str, str]]
) -> None:
    console = Console()
    print_h2("File Metadata")
    console.print(create_metadata_table(file_metadata_rows))
    print_h2("Stock Metadata")
    console.print(create_metadata_table(stock_metadata_rows))
