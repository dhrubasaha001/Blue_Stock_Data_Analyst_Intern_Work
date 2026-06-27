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
## Day 2 Progress

### Data Cleaning

Completed cleaning and validation for:

* NAV History
* Investor Transactions
* Scheme Performance

Validation checks included:

* Date parsing
* Missing value handling
* Duplicate removal
* Positive value validation
* Transaction type standardization
* Expense ratio validation
* Anomaly detection

### Database Development

Created SQLite database:

```text
bluestock_mf.db
```

Implemented star schema design with:

* dim_fund
* dim_date
* fact_nav
* fact_transactions
* fact_performance
* fact_aum

### SQL Analytics

Developed 10 analytical SQL queries covering:

* Assets Under Management (AUM)
* NAV analysis
* Expense ratio screening
* Risk analysis
* State-wise transaction analysis
* Investment behavior analysis

### Day 2 Deliverables

* 10 cleaned CSV files
* SQLite database
* schema.sql
* queries.sql
* data_dictionary.md
* day2_quality_report.txt

---
## Day 3 – Exploratory Data Analysis (EDA)

### Objectives

* Perform exploratory analysis on cleaned mutual fund datasets
* Visualize investment trends using Plotly, Matplotlib, and Seaborn
* Generate business insights from historical data

### Charts Created

* Daily NAV Trend
* AUM Growth by Fund House
* Monthly SIP Trend
* Category Inflow Heatmap
* Investor Age Distribution
* SIP Amount Boxplot
* Gender Distribution
* State-wise Investment Distribution
* City Tier Distribution
* Industry Folio Growth
* NAV Return Correlation Matrix
* Sector Allocation Donut Chart

### Key Findings

* Long-term NAV growth observed across schemes
* SBI Mutual Fund maintained the highest AUM
* SIP inflows reached record highs in late 2025
* Equity funds dominated net inflows
* Investor participation increased steadily
* Strong positive correlations existed among large-cap funds

### Technologies Used

* Python
* Pandas
* NumPy
* Plotly
* Matplotlib
* Seaborn
* SQLite
* SQLAlchemy
* Jupyter Notebook

### Deliverables

* EDA_Analysis.ipynb
* 15+ Visualizations
* Exported Chart Assets
* Day 3 Quality Report

---

## Author

Dhruba Saha

Data Analyst Intern
Bluestock Fintech
