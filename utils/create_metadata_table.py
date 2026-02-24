from rich import box
from rich.table import Table


def create_metadata_table(title: str, rows: list[tuple[str, str]]) -> Table:
    table = Table(
        title=title,
        show_header=True,
        header_style="bold cyan",
        box=box.SQUARE,
        show_lines=True,
    )
    table.add_column("Field")
    table.add_column("Value", overflow="fold")

    for field, value in rows:
        table.add_row(field, value)

    return table
