def execute_buy_trade(cash: float, close_price: float, trade_time) -> dict:
    shares_to_buy = int(cash // close_price)
    if shares_to_buy <= 0:
        return {
            "cash": cash,
            "shares": 0,
            "buy_price": None,
            "buy_time": None,
            "executed": False,
        }

    return {
        "cash": cash - shares_to_buy * close_price,
        "shares": shares_to_buy,
        "buy_price": float(close_price),
        "buy_time": trade_time,
        "executed": True,
    }
