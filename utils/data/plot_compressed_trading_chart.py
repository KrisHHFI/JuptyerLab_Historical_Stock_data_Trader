import matplotlib.pyplot as plt
import pandas as pd


def plot_compressed_trading_chart(csv_path: str, ticker: str, interval: str) -> None:
    price_data = pd.read_csv(csv_path)

    time_column = "Datetime" if "Datetime" in price_data.columns else "Date"
    price_data[time_column] = pd.to_datetime(price_data[time_column], errors="coerce")
    plot_data = (
        price_data.dropna(subset=[time_column])
        .sort_values(time_column)
        .reset_index(drop=True)
    )

    x_positions = range(len(plot_data))

    plt.figure(figsize=(12, 5))
    plt.plot(x_positions, plot_data["Close"], linewidth=1)
    plt.title(f"{ticker} Close Price ({interval})")
    plt.xlabel("Trading Time (compressed)")
    plt.ylabel("Close Price")
    plt.grid(True, alpha=0.3)
    plt.margins(x=0)

    if len(plot_data) > 0:
        trading_day = plot_data[time_column].dt.date
        day_start_positions = (
            plot_data.groupby(trading_day, sort=False).head(1).index.tolist()
        )
        day_labels = (
            plot_data.loc[day_start_positions, time_column]
            .dt.strftime("%b %d")
            .tolist()
        )
        plt.xticks(day_start_positions, day_labels, rotation=0, ha="center")
        plt.xlim(0, len(plot_data) - 1)

    plt.tight_layout()
    plt.show()
