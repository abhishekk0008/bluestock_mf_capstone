# Mutual Fund Analytics Project - Data Dictionary

This document describes the datasets used in the Mutual Fund Analytics Capstone Project and explains the meaning of key fields stored in the SQLite database.

## 1. dim_fund

This table contains the master information of all mutual fund schemes.

| Column        | Description
| ------------- | -------------------------------- |
| amfi_code     | Unique identifier assigned to each mutual fund scheme |
| fund_house    | Asset Management Company (AMC) offering the scheme
| scheme_name   | Name of the mutual fund scheme     
| category      | Broad fund category such as Equity or Debt
| sub_category  | Detailed classification of the fund 
| plan          | Indicates whether the scheme is Direct or Regular
| risk_category | Risk level associated with the scheme  

---

## 2. fact_nav

This table stores historical NAV (Net Asset Value) data for mutual fund schemes.

| Column    | Description                                |
| --------- | ------------------------------------------ |
| amfi_code | Unique scheme identifier                   |
| date      | Date on which NAV was recorded             |
| nav       | Net Asset Value of the scheme on that date |

---

## 3. fact_transactions

This table captures investor transaction activity across different schemes.

| Column             | Description            
| ------------------ |---------------------------
| investor_id        | Unique identifier for each investor
| transaction_date   | Date of transaction           
| amfi_code          | Scheme identifier           
| transaction_type   | SIP, Lumpsum, or Redemption      
| amount_inr         | Transaction amount in Indian Rupees
| state              | State of the investor             
| city               | City of the investor         
| city_tier          | Classification of city (Tier 1, Tier 2, etc.)
| age_group          | Investor age category    
| gender             | Gender of the investor  
| annual_income_lakh | Annual income in lakhs
| payment_mode       | Mode used for payment    
| kyc_status         | Investor KYC verification status   

---

## 4. fact_performance

This table contains performance and risk metrics of mutual fund schemes.

| Column             |  Description
| ------------------ | --------------------------------
| return_1yr_pct     | Return generated over the last 1 year
| return_3yr_pct     | Return generated over the last 3 years
| return_5yr_pct     | Return generated over the last 5 years        |
| benchmark_3yr_pct  | Benchmark return for comparison  
| alpha              | Excess return generated relative to benchmark |
| beta               | Volatility compared to the market  
| sharpe_ratio       | Risk-adjusted performance indicator
| sortino_ratio      | Downside-risk-adjusted performance indicator
| std_dev_ann_pct    | Annualized volatility of returns              |
| max_drawdown_pct   | Maximum decline from peak value  
| aum_crore          | Assets Under Management (in crore ₹)
| expense_ratio_pct  | Annual fee charged by the fund 
| morningstar_rating | Fund rating provided by Morningstar
| risk_grade         | Overall risk classification ofthe scheme
