import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)

# Dataset overview
print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

# Unique fund houses
if "fund_house" in df.columns:
    print("\nUnique Fund Houses:")
    print(df["fund_house"].unique())
    print(f"Total Fund Houses: {df['fund_house'].nunique()}")

# Unique categories
if "category" in df.columns:
    print("\nUnique Categories:")
    print(df["category"].unique())
    print(f"Total Categories: {df['category'].nunique()}")

# Unique sub categories
if "sub_category" in df.columns:
    print("\nUnique Sub Categories:")
    print(df["sub_category"].unique())
    print(f"Total Sub Categories: {df['sub_category'].nunique()}")

# Check if any risk-related column exists
risk_cols = [col for col in df.columns if "risk" in col.lower()]

if risk_cols:
    for col in risk_cols:
        print(f"\nUnique Values in {col}:")
        print(df[col].unique())
else:
    print("\nNo risk-related column found in dataset.")