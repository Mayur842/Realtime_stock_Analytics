import yfinance as yf
from pathlib import Path


# -----------------------------
# PROJECT PATH
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)


# -----------------------------
# STOCK SETTINGS
# -----------------------------

TICKER = "RELIANCE.NS"
PERIOD = "1d"
INTERVAL = "1m"


# -----------------------------
# FETCH STOCK DATA
# -----------------------------

print("\nFetching stock data...")

stock = yf.Ticker(TICKER)

data = stock.history(
    period=PERIOD,
    interval=INTERVAL
)


# -----------------------------
# CHECK DATA
# -----------------------------

if data.empty:
    print("No stock data received.")
    exit()


print(f"Data fetched successfully: {len(data)} rows")


# -----------------------------
# SAVE DATA
# -----------------------------

output_file = DATA_DIR / "reliance_1min.csv"

data.to_csv(output_file)


print(f"\nData saved successfully!")
print(f"File: {output_file}")