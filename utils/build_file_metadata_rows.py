def build_file_metadata_rows(metadata: dict, stock_data_location: str) -> list[tuple[str, str]]:
    exported_at = metadata["exported_at"]
    return [
        ("File name", metadata["file_name"]),
        ("Export timestamp token", metadata["timestamp_token"]),
        ("Exported at", f"{exported_at:%Y-%m-%d %H:%M:%S}"),
        ("Export date", f"{exported_at:%Y-%m-%d}"),
        ("Export time", f"{exported_at:%H:%M:%S}"),
        ("File age", str(metadata["file_age"])),
        ("Stock data source", stock_data_location),
    ]
