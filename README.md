# Blue_Stock_Data_Analyst_Intern_Work

## Overview

This repository contains the Day 1 deliverables for the Bluestock Fintech Data Analyst Internship Capstone Project: **Mutual Fund Analytics**.

The objective of Day 1 was to set up the project environment, ingest mutual fund datasets, fetch live NAV data from public APIs, perform initial data validation, and establish a reproducible analytics workflow.

---

## Project Structure

```text
.
├── data/
│   └── raw/
│       ├── 01_fund_master.csv
│       ├── 02_nav_history.csv
│       ├── 03_aum_by_fund_house.csv
│       ├── 04_monthly_sip_inflows.csv
│       ├── 05_category_inflows.csv
│       ├── 06_industry_folio_count.csv
│       ├── 07_scheme_performance.csv
│       ├── 08_investor_transactions.csv
│       ├── 09_portfolio_holdings.csv
│       └── 10_benchmark_indices.csv
│
├── data_ingestion.py
├── live_nav_fetch.py
├── validate_amfi.py
├── check_fund_master.py
├── check_nav_history.py
├── requirements.txt
└── day1_quality_report.txt
```

---

## Features

* Load and validate multiple mutual fund datasets using Pandas
* Explore fund metadata and scheme information
* Fetch live NAV data using MFAPI
* Validate AMFI scheme codes across datasets
* Perform initial data quality assessment
* Maintain reproducible project structure using Git and GitHub

---

## Technologies Used

* Python
* Pandas
* NumPy
* Requests
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy
* Jupyter Notebook
* Git & GitHub

---

## Data Validation Performed

### Fund Master Exploration

* Fund Houses
* Categories
* Sub Categories
* Risk Categories
* AMFI Scheme Codes

### AMFI Validation Results

* Total Fund Master Codes: 40
* Total NAV History Codes: 40
* Missing Codes: 0

Result:

All AMFI scheme codes present in the Fund Master dataset were successfully found in the NAV History dataset.

---

## Live NAV Data Sources

The project fetches NAV data for:

* HDFC Top 100 Direct
* SBI Bluechip
* ICICI Bluechip
* Nippon Large Cap
* Axis Bluechip
* Kotak Bluechip

Source API:

https://api.mfapi.in

---

## Day 1 Deliverables

* Project Setup
* Data Ingestion Pipeline
* Live NAV Fetching
* Dataset Exploration
* AMFI Validation
* Data Quality Report
* GitHub Repository

---

## Author

Dhruba Saha

Data Analyst Intern
Bluestock Fintech
