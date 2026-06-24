-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month
SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. SIP Inflow YoY Growth
SELECT
strftime('%Y', transaction_date) AS year,
SUM(amount_inr) AS sip_inflow
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

-- 4. Transactions by State
SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
WHERE expense_ratio_pct < 1;

-- 6. Top 5 Funds by 5-Year Return
SELECT
scheme_name,
return_5yr_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 7. Average Return by Category
SELECT
category,
AVG(return_3yr_pct) AS avg_return
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
GROUP BY category;

-- 8. Fund Count by Risk Grade
SELECT
risk_grade,
COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade;

-- 9. Total Investment by Transaction Type
SELECT
transaction_type,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 10. Top 10 Cities by Transaction Volume
SELECT
city,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY city
ORDER BY transactions DESC
LIMIT 10;