"""
NAV History Cleaning Module.

This script cleans historical NAV data
by converting date formats, removing duplicates,
forward-filling missing NAV values,
and validating NAV values greater than zero.
"""

import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort values
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Validate NAV > 0
df = df[df["nav"] > 0]

print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("Saved Successfully")