# AGENTS.md

## Development Rules

1. **One function per file**
   - Each standalone function must live in its own Python file.
   - Keep files small, focused, and single-purpose.

2. **Sensitive data must be git-ignored**
   - Never commit secrets or sensitive artifacts.
   - Examples: API keys, tokens, credentials, local env files, generated private datasets, and large downloaded outputs.
   - Ensure `.gitignore` is updated whenever new sensitive/generated paths are introduced.

3. **Keep this document up to date**
   - Update `AGENTS.md` whenever project structure, conventions, or workflow rules change.

4. **Reuse active runtime sessions**
   - Do not repeatedly establish a new notebook kernel or Python environment when one is already active and working.
   - Only restart or reconfigure the kernel/environment when there is a concrete execution/import failure that requires it.

## Project Architecture

```text
historicalStockTrader/
├── .gitignore
├── AGENTS.md
├── README.md
├── constants.py
├── main.ipynb
└── utils/
    ├── __init__.py
   ├── build_file_metadata_rows.py
   ├── build_stock_metadata_rows.py
   ├── create_metadata_table.py
   ├── parse_stock_filename_metadata.py
   ├── plot_compressed_trading_chart.py
   ├── print_header.py
   └── print_metadata_tables.py
```

## Notes

- `main.ipynb` is the main execution entry for this project.
- Utility logic is separated under `utils/` using the one-function-per-file convention.
- The project charts from a configured CSV path and does not include in-project data download functions.
- The notebook parses ticker/interval/period/timestamp from the CSV filename and prints metadata in separate `File Metadata` and `Stock Metadata` tables.
