def build_stock_metadata_rows(metadata: dict) -> list[tuple[str, str]]:
    return [
        ("Ticker", metadata["ticker"]),
        ("Interval", metadata["interval"]),
        ("Interval quantity", str(metadata["interval_quantity"])),
        ("Interval unit", str(metadata["interval_unit"])),
        ("Period", metadata["period"]),
        ("Is max history", str(metadata["is_max_history"])),
    ]
