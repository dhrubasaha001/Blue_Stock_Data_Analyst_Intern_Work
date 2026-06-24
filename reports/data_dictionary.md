# Data Dictionary

## 01_fund_master.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| fund_house | TEXT | Mutual fund company |
| scheme_name | TEXT | Name of mutual fund scheme |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |

## 02_nav_history.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Scheme identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |