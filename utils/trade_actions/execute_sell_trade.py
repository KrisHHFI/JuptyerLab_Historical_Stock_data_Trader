def execute_sell_trade(
    cash: float,
    shares: int,
    buy_price: float | None,
    buy_time,
    sell_price: float,
    sell_time,
    trade_number: int,
) -> dict:
    updated_cash = cash + shares * sell_price

    if buy_price is None or buy_price <= 0:
        return {
            "cash": updated_cash,
            "trade_return_pct": None,
            "trade_record": None,
        }

    trade_return_pct = ((sell_price - buy_price) / buy_price) * 100
    trade_pnl = (sell_price - buy_price) * shares

    return {
        "cash": updated_cash,
        "trade_return_pct": float(trade_return_pct),
        "trade_record": {
            "trade": trade_number,
            "entry_time": buy_time,
            "exit_time": sell_time,
            "entry_price": float(buy_price),
            "exit_price": float(sell_price),
            "shares": int(shares),
            "pnl": float(trade_pnl),
            "return_pct": float(trade_return_pct),
        },
    }
