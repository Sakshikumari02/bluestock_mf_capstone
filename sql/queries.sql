-- Query 1: Top 5 funds by AUM
SELECT fund_house, SUM(aum_lakh_crore) as total_aum
FROM aum_by_fund
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- Query 2: Average NAV per month
SELECT strftime('%Y-%m', date) as month, 
       AVG(nav) as avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- Query 3: SIP YoY growth
SELECT year, SUM(sip_inflow_crore) as total_sip
FROM monthly_sip
GROUP BY year
ORDER BY year;

-- Query 4: Transactions by state
SELECT state, COUNT(*) as total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Query 5: Funds with expense ratio less than 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct;

-- Query 6: Top 5 funds by 1 year return
SELECT scheme_name, return_1yr_pct
FROM scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- Query 7: Category wise average return
SELECT category, AVG(return_1yr_pct) as avg_return
FROM scheme_performance
GROUP BY category
ORDER BY avg_return DESC;

-- Query 8: Total SIP inflow per year
SELECT year, SUM(sip_inflow_crore) as yearly_sip
FROM monthly_sip
GROUP BY year;

-- Query 9: Top 10 portfolio holdings
SELECT stock_name, SUM(weightage_pct) as total_weight
FROM portfolio_holdings
GROUP BY stock_name
ORDER BY total_weight DESC
LIMIT 10;

-- Query 10: Benchmark indices performance
SELECT index_name, AVG(close_value) as avg_close
FROM benchmark_indices
GROUP BY index_name;