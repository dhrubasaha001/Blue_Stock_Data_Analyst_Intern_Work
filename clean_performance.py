import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Remove rows with invalid returns
df = df.dropna(
    subset=return_cols
)

# Expense ratio validation
df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]

# Flag anomalies
df["anomaly_flag"] = (
    (df["return_1yr_pct"] > 100)
    |
    (df["return_1yr_pct"] < -100)
)

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print(
    "Scheme Performance Cleaned"
)

print(df.shape)

print(
    "\nAnomalies Found:",
    df["anomaly_flag"].sum()
)