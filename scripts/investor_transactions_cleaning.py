"""
Investor Transactions Cleaning Module.

This script standardizes transaction types,
validates transaction amounts,
checks KYC status values,
and saves cleaned transaction data.
"""

import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Date format fix
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = df["transaction_type"].str.strip().str.title()

# Keep only valid transaction types
valid_types = ["Sip", "Lumpsum", "Redemption"]
df = df[df["transaction_type"].isin(valid_types)]

# Amount should be greater than 0
df = df[df["amount_inr"] > 0]

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("Saved Successfully")