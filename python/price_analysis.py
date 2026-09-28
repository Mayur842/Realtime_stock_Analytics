import pandas as pd
from pathlib import Path


# -----------------------------
# PROJECT PATH
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "reliance_1min.csv"


# -----------------------------
# LOAD DATA
# -----------------------------

data = pd.read_csv(DATA_FILE)


# -----------------------------
# PRICE CHANGE ANALYSIS
# -----------------------------

data["Price_Change_%"] = (
    (data["Close"] - data["Open"])
    / data["Open"]
) * 100


# -----------------------------
# DISPLAY RESULT
# -----------------------------

print("\n--- PRICE CHANGE ANALYSIS ---")

print(
    data[
        ["Open", "Close", "Price_Change_%"]
    ].tail(10)
)