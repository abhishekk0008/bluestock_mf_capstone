import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print(df.columns.tolist())
print()
print(df.head())
print()
print(df.shape)