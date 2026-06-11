"""
Fund Master Analysis Module.

This script explores fund master data,
analyzes fund houses, categories,
sub-categories, and risk grades,
and validates scheme metadata.
"""
import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("===== FUND HOUSES =====")
print(fund_master["fund_house"].unique())

print("\n===== CATEGORIES =====")
print(fund_master["category"].unique())

print("\n===== SUB CATEGORIES =====")
print(fund_master["sub_category"].unique())

print("\n===== RISK CATEGORIES =====")
print(fund_master["risk_category"].unique())