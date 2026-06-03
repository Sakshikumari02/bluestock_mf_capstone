import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Numeric return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "expense_ratio_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check missing values after conversion
print("\nMissing Values:")
print(df[return_cols].isnull().sum())

# Expense ratio validation
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Records:")
print(len(invalid_expense))

# Remove rows with missing critical values
df = df.dropna(subset=return_cols)

print("\nCleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("Saved Successfully")