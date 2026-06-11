"""
Live NAV Fetch Module.

This script retrieves real-time NAV data
for selected mutual fund schemes using MFAPI
and saves the results to the raw data folder.
"""

import requests
import pandas as pd
from pathlib import Path

# Folder path
raw_path = Path("data/raw")
raw_path.mkdir(parents=True, exist_ok=True)

# Fund codes
funds = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Fetch and save
for fund_name, code in funds.items():
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data["data"])
    df["fund_name"] = fund_name
    df["scheme_code"] = code
    filename = raw_path / f"{fund_name}_nav.csv"
    df.to_csv(filename, index=False)
    print(f"Saved: {filename}")

print("All NAV data fetched!")