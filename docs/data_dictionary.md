# Data Dictionary — Bluestock MF Capstone

## 1. fund_master (01_fund_master.csv)
| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| scheme_name | String | Full name of mutual fund scheme |
| fund_house | String | Name of AMC/fund house |
| category | String | Fund category (Equity/Debt/Hybrid) |
| sub_category | String | Sub-category of fund |
| risk_category | String | Risk grade (Low/Moderate/High) |

## 2. nav_history (02_nav_history.csv)
| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | AMFI scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value on that date |

## 3. scheme_performance (07_scheme_performance.csv)
| Column | Data Type | Description |
|--------|-----------|-------------|
| scheme_name | String | Fund scheme name |
| return_1yr_pct | Float | 1 year return percentage |
| return_3yr_pct | Float | 3 year return percentage |
| return_5yr_pct | Float | 5 year return percentage |
| expense_ratio_pct | Float | Annual expense ratio |

## 4. investor_transactions (08_investor_transactions.csv)
| Column | Data Type | Description |
|--------|-----------|-------------|
| transaction_type | String | SIP/Lumpsum/Redemption |
| amount | Float | Transaction amount |
| date | Date | Transaction date |
| state | String | Investor state |
| kyc_status | String | KYC verification status |