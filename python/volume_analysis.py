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
# VOLUME MOVING AVERAGE
# -----------------------------

data["Volume_MA_20"] = (
    data["Volume"].rolling(window=20).mean()
)


# -----------------------------
# VOLUME RATIO
# -----------------------------

data["Volume_Ratio"] = (
    data["Volume"] / data["Volume_MA_20"]
)


# -----------------------------
# DISPLAY RESULT
# -----------------------------

print("\n--- VOLUME ANALYSIS ---")

print(
    data[
        ["Volume", "Volume_MA_20", "Volume_Ratio"]
    ].tail(10)
)