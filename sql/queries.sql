-- 1 Top 5 Funds by AUM

SELECT *
FROM performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV

SELECT AVG(nav)
FROM nav_history;

-- 3 Funds Expense Ratio < 1%

SELECT scheme_name,
       expense_ratio_pct
FROM performance
WHERE expense_ratio_pct < 1;

-- 4 Top Alpha Funds

SELECT scheme_name,
       alpha
FROM performance
ORDER BY alpha DESC
LIMIT 5;

-- 5 Highest Sharpe Ratio

SELECT scheme_name,
       sharpe_ratio
FROM performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 6 Risk Distribution

SELECT risk_grade,
       COUNT(*)
FROM performance
GROUP BY risk_grade;

-- 7 Transactions By State

SELECT state,
       COUNT(*)
FROM transactions
GROUP BY state
ORDER BY COUNT(*) DESC;

-- 8 Average Investment By State

SELECT state,
       AVG(amount_inr)
FROM transactions
GROUP BY state;

-- 9 Transaction Type Distribution

SELECT transaction_type,
       COUNT(*)
FROM transactions
GROUP BY transaction_type;

-- 10 Top Fund Houses

SELECT fund_house,
       COUNT(*)
FROM fund_master
GROUP BY fund_house
ORDER BY COUNT(*) DESC;