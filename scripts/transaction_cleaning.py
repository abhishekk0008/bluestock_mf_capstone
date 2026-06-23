import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("=" * 60)
print("BEFORE CLEANING")
print("=" * 60)

print(df.dtypes)

# Convert transaction date to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

print("\n" + "=" * 60)
print("AFTER CLEANING")
print("=" * 60)

print(df.dtypes)

# Save cleaned file
df.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("\nClean dataset saved successfully!")