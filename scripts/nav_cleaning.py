import pandas as pd

# Load data
df = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 60)
print("BEFORE CONVERSION")
print("=" * 60)

print(df.dtypes)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

print("\n" + "=" * 60)
print("AFTER CONVERSION")
print("=" * 60)

print(df.dtypes)

# Save cleaned file
df.to_csv("data/processed/clean_nav_history.csv", index=False)

print("\nClean file saved successfully!")