from datetime import datetime
from pathlib import Path
import re


def parse_stock_filename_metadata(stock_data_location: str) -> dict:
    file_name = Path(stock_data_location).name
    match = re.match(
        r"^(?P<ticker>[^_]+)_(?P<interval>[^_]+)_(?P<period>[^_]+)_(?P<timestamp>\d{8}_\d{6})\.csv$",
        file_name,
    )
    if not match:
        raise ValueError(
            "Invalid stock file name format. Expected: <ticker>_<interval>_<period>_<YYYYMMDD_HHMMSS>.csv"
        )

    ticker = match.group("ticker")
    interval = match.group("interval")
    period = match.group("period")
    timestamp_token = match.group("timestamp")
    exported_at = datetime.strptime(timestamp_token, "%Y%m%d_%H%M%S")

    interval_match = re.match(r"^(\d+)([a-zA-Z]+)$", interval)
    interval_quantity = int(interval_match.group(1)) if interval_match else None
    interval_unit = interval_match.group(2) if interval_match else None
    is_max_history = period.lower() == "max"
    file_age = datetime.now() - exported_at

    return {
        "file_name": file_name,
        "ticker": ticker,
        "interval": interval,
        "period": period,
        "timestamp_token": timestamp_token,
        "exported_at": exported_at,
        "interval_quantity": interval_quantity,
        "interval_unit": interval_unit,
        "is_max_history": is_max_history,
        "file_age": file_age,
    }
