from rich.console import Console

from utils.create_metadata_table import create_metadata_table


def print_metadata_tables(
    file_metadata_rows: list[tuple[str, str]], stock_metadata_rows: list[tuple[str, str]]
) -> None:
    console = Console()
    console.print(create_metadata_table("File Metadata", file_metadata_rows))
    console.print(create_metadata_table("Stock Metadata", stock_metadata_rows))
