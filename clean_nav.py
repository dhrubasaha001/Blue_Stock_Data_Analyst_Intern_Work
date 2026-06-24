import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort properly
df = df.sort_values(
    ["amfi_code", "date"]
)

# Fill missing NAV values
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

# Remove duplicates
df = df.drop_duplicates()

# Keep only valid NAVs
df = df[df["nav"] > 0]

# Save cleaned file
df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV History Cleaned Successfully")
print(df.shape)