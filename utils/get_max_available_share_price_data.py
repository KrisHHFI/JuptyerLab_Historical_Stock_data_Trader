from datetime import datetime
from pathlib import Path
import time

import yfinance as yf

from constants import CALL_DELAY_SECONDS, CALL_LIMIT, INTERVAL, TARGET_TICKER
from utils.build_call_record import build_call_record
from utils.enforce_call_limit import enforce_call_limit
from utils.print_header import print_header
from utils.print_calls_made import print_calls_made


def get_max_available_share_price_data(
    target_ticker: str = TARGET_TICKER,
    interval: str = INTERVAL,
    delay_seconds: float = CALL_DELAY_SECONDS,
    call_limit: int = CALL_LIMIT,
    output_dir: str = "downloads",
):
    max_period_by_interval = {
        "1m": "7d",
        "2m": "60d",
        "5m": "60d",
        "15m": "60d",
        "30m": "60d",
        "60m": "730d",
        "90m": "60d",
        "1h": "730d",
        "1d": "max",
        "5d": "max",
        "1wk": "max",
        "1mo": "max",
        "3mo": "max",
    }
    period = max_period_by_interval.get(interval, "60d")

    calls_made = []

    enforce_call_limit(calls_made_count=len(calls_made), call_limit=call_limit)

    call_record = build_call_record(
        method="yf.Ticker().history",
        ticker=target_ticker,
        time_frame=period,
        delay_seconds=delay_seconds,
    )
    calls_made.append(call_record)

    print_header("REQUEST")
    print(
        f"CALL 1: yf.Ticker('{target_ticker}').history(period='{period}', interval='{interval}', auto_adjust=False)"
    )

    try:
        time.sleep(delay_seconds)
        data = yf.Ticker(target_ticker).history(
            period=period, interval=interval, auto_adjust=False
        )

        if data.empty:
            raise ValueError(f"No historical data returned for interval '{interval}'.")

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        file_name = f"{target_ticker}_{interval}_max_{datetime.now():%Y%m%d_%H%M%S}.csv"
        csv_file_path = output_path / file_name
        data.to_csv(csv_file_path)

        calls_made[-1]["status"] = "success"
        calls_made[-1]["rows"] = int(len(data))
        calls_made[-1]["interval"] = interval
        calls_made[-1]["csv_path"] = str(csv_file_path)

        print_header("RESULT")
        print(
            f"SUCCESS: Downloaded {len(data)} rows for {target_ticker} at interval '{interval}'."
        )
        print(f"CSV saved to: {csv_file_path.resolve()}")

    except Exception as error:
        calls_made[-1]["status"] = "failure"
        calls_made[-1]["error"] = str(error)
        csv_file_path = None
        print_header("RESULT")
        print(f"FAILURE: {error}")

    print_calls_made(calls_made)
    return csv_file_path, calls_made
