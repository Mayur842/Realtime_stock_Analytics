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
# PRICE CHANGE
# -----------------------------

data["Price_Change_%"] = (
    (data["Close"] - data["Open"])
    / data["Open"]
) * 100


# -----------------------------
# VOLUME ANALYSIS
# -----------------------------

data["Volume_MA_20"] = (
    data["Volume"].rolling(window=20).mean()
)

data["Volume_Ratio"] = (
    data["Volume"] / data["Volume_MA_20"]
)


# -----------------------------
# VOLUME ANOMALY
# -----------------------------

data["Volume_Anomaly"] = (
    data["Volume_Ratio"] >= 2
)


# -----------------------------
# PRICE ANOMALY
# -----------------------------

data["Price_Anomaly"] = (
    data["Price_Change_%"].abs() >= 0.10
)


# -----------------------------
# COMBINED ANOMALY
# -----------------------------

data["Combined_Anomaly"] = (
    data["Volume_Anomaly"]
    & data["Price_Anomaly"]
)


# -----------------------------
# DISPLAY RESULT
# -----------------------------

print("\n--- ANOMALY DETECTION ---")

print(
    data[
        [
            "Close",
            "Price_Change_%",
            "Volume_Ratio",
            "Volume_Anomaly",
            "Price_Anomaly",
            "Combined_Anomaly"
        ]
    ].tail(10)
)