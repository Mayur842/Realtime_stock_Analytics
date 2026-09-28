import pandas as pd
from pathlib import Path


# -----------------------------
# PROJECT PATH
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "reliance_1min.csv"
OUTPUT_FILE = BASE_DIR / "data" / "reliance_processed.csv"


# -----------------------------
# LOAD RAW DATA
# -----------------------------

print("\nLoading stock data...")

data = pd.read_csv(INPUT_FILE)

print(f"Rows loaded: {len(data)}")


# -----------------------------
# PRICE ANALYSIS
# -----------------------------

data["Price_Change_%"] = (
    (data["Close"] - data["Open"])
    / data["Open"]
) * 100


# -----------------------------
# VOLATILITY
# -----------------------------

volatility = data["Price_Change_%"].std()


# -----------------------------
# MOVING AVERAGE
# -----------------------------

data["MA_20"] = (
    data["Close"]
    .rolling(window=20)
    .mean()
)


# -----------------------------
# VOLUME ANALYSIS
# -----------------------------

data["Volume_MA_20"] = (
    data["Volume"]
    .rolling(window=20)
    .mean()
)

data["Volume_Ratio"] = (
    data["Volume"]
    / data["Volume_MA_20"]
)


# -----------------------------
# ANOMALY DETECTION
# -----------------------------

data["Volume_Anomaly"] = (
    data["Volume_Ratio"] >= 2
)

data["Price_Anomaly"] = (
    data["Price_Change_%"].abs() >= 0.10
)

data["Combined_Anomaly"] = (
    data["Volume_Anomaly"]
    & data["Price_Anomaly"]
)


# -----------------------------
# RISK ANALYSIS
# -----------------------------

data["Risk_Level"] = "Low"

data.loc[
    data["Volume_Anomaly"],
    "Risk_Level"
] = "Medium"

data.loc[
    data["Combined_Anomaly"],
    "Risk_Level"
] = "High"


# -----------------------------
# SAVE PROCESSED DATA
# -----------------------------

data.to_csv(
    OUTPUT_FILE,
    index=False
)


# -----------------------------
# SUMMARY
# -----------------------------

print("\n--- PROCESSING COMPLETE ---")

print(f"Rows processed: {len(data)}")
print(f"Volatility: {volatility:.4f}%")

print("\nRisk Level Count:")
print(data["Risk_Level"].value_counts())

print("\nAnomaly Count:")
print(data["Combined_Anomaly"].value_counts())

print(f"\nProcessed file saved:")
print(OUTPUT_FILE)