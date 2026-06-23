import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Remove duplicates (safety)
df = df.drop_duplicates()

# Standardize text columns
df["risk_grade"] = df["risk_grade"].str.strip()
df["category"] = df["category"].str.strip()
df["plan"] = df["plan"].str.strip()

# Save cleaned dataset
df.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print("Clean scheme performance file saved successfully!")
print("Rows:", len(df))