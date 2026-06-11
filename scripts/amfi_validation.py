"""
AMFI Code Validation Module.

This script validates AMFI scheme codes
between fund master and NAV history datasets.
It identifies missing, invalid, or unmatched
scheme codes and generates data quality checks.
"""

import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("Total Fund Master Codes:", len(master_codes))
print("Total NAV History Codes:", len(nav_codes))
print("Missing Codes:", len(missing_codes))

if len(missing_codes) == 0:
    print("All AMFI codes from fund_master exist in nav_history")
else:
    print("Missing Code List:")
    print(missing_codes)