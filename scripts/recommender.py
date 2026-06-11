"""
Fund Recommendation Module.

This script recommends mutual funds
based on investor risk appetite
using performance and risk metrics.
"""

import pandas as pd
import os

def recommend_funds(risk_appetite, data_path='../data/raw/07_scheme_performance.csv'):
    perf_df = pd.read_csv(data_path)
    risk_map = {
        'Low'      : ['Low'],
        'Moderate' : ['Moderate'],
        'High'     : ['High', 'Very High']
    }
    grades = risk_map.get(risk_appetite, [])
    if not grades:
        print("Invalid input! Choose: Low / Moderate / High")
        return
    filtered = perf_df[perf_df['risk_grade'].isin(grades)]
    top3 = (filtered.sort_values('sharpe_ratio', ascending=False)
                    .head(3)[['scheme_name','category','risk_grade',
                               'sharpe_ratio','return_3yr_pct']])
    print(f"\n--- Top 3 Funds for {risk_appetite} Risk Appetite ---")
    print(top3.to_string(index=False))

if __name__ == "__main__":
    user_input = input("Enter risk appetite (Low / Moderate / High): ")
    recommend_funds(user_input)
