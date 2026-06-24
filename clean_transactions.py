import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Date conversion
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

allowed = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

df = df[
    df["transaction_type"].isin(allowed)
]

# Amount validation
df = df[
    df["amount_inr"] > 0
]

# KYC validation
allowed_kyc = [
    "Verified",
    "Pending"
]

df = df[
    df["kyc_status"].isin(
        allowed_kyc
    )
]

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print(
    "Investor Transactions Cleaned"
)
print(df.shape)