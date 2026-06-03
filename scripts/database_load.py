import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# Database connection
engine = create_engine("sqlite:///data/db/bluestock_mf.db")

# Load all cleaned CSVs
files = {
    "fund_master": "data/raw/01_fund_master.csv",
    "nav_history": "data/raw/02_nav_history.csv",
    "aum_by_fund": "data/raw/03_aum_by_fund_house.csv",
    "monthly_sip": "data/raw/04_monthly_sip_inflows.csv",
    "category_inflows": "data/raw/05_category_inflows.csv",
    "industry_folio": "data/raw/06_industry_folio_count.csv",
    "scheme_performance": "data/raw/07_scheme_performance.csv",
    "investor_transactions": "data/raw/08_investor_transactions.csv",
    "portfolio_holdings": "data/raw/09_portfolio_holdings.csv",
    "benchmark_indices": "data/raw/10_benchmark_indices.csv"
}

for table_name, file_path in files.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Loaded: {table_name} — {len(df)} rows")

print("\nAll tables loaded into SQLite!")