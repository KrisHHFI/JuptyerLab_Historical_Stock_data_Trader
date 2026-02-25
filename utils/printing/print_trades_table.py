from rich import box
from rich.console import Console
from rich.table import Table

from utils.printing.print_h2 import print_h2


def print_trades_table(trades: list[dict]) -> None:
    console = Console()
    print_h2("Trades")

    table = Table(
        show_header=True,
        header_style="bold cyan",
        box=box.SQUARE,
        show_lines=True,
    )
    table.add_column("#", justify="right")
    table.add_column("Entry Time")
    table.add_column("Exit Time")
    table.add_column("Entry")
    table.add_column("Exit")
    table.add_column("Shares", justify="right")
    table.add_column("P&L", justify="right")
    table.add_column("Return %", justify="right")

    if not trades:
        table.add_row("-", "No trades", "-", "-", "-", "-", "-", "-")
    else:
        for trade in trades:
            entry_time = trade["entry_time"]
            exit_time = trade["exit_time"]
            table.add_row(
                str(trade["trade"]),
                entry_time.strftime("%Y-%m-%d %H:%M") if hasattr(entry_time, "strftime") else str(entry_time),
                exit_time.strftime("%Y-%m-%d %H:%M") if hasattr(exit_time, "strftime") else str(exit_time),
                f"{trade['entry_price']:.2f}",
                f"{trade['exit_price']:.2f}",
                str(trade["shares"]),
                f"${trade['pnl']:.2f}",
                f"{trade['return_pct']:.2f}%",
            )

    console.print(table)
