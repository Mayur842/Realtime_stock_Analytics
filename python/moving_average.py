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
# MOVING AVERAGE
# -----------------------------

data["MA_20"] = data["Close"].rolling(window=20).mean()


# -----------------------------
# DISPLAY RESULT
# -----------------------------

print("\n--- MOVING AVERAGE ANALYSIS ---")

print(
    data[
        ["Close", "MA_20"]
    ].tail(10)
)