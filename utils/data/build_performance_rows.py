def build_performance_rows(performance: dict) -> list[tuple[str, str]]:
    return [
        ("Strategy", performance["strategy"]),
        ("Initial capital", f"${performance['initial_capital']:,.2f}"),
        ("Final capital", f"${performance['final_capital']:,.2f}"),
        ("Net P&L", f"${performance['net_pnl']:,.2f}"),
        ("Total fees", f"${performance.get('total_fees_paid', 0.0):,.2f}"),
        ("Return %", f"{performance['return_pct']:.2f}%"),
        ("Trades", str(performance["trade_count"])),
        ("Winning trades", str(performance["winning_trades"])),
        ("Losing trades", str(performance["losing_trades"])),
        ("Win rate", f"{performance['win_rate_pct']:.2f}%"),
        ("Average trade return", f"{performance['avg_trade_return_pct']:.2f}%"),
    ]
