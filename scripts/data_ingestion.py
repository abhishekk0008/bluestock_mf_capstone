import pandas as pd
import os

data_path = "data/raw"

files = os.listdir(data_path)

for file in files:

    if file.endswith(".csv"):

        print("\n" + "=" * 70)
        print(f"DATASET: {file}")
        print("=" * 70)

        file_path = os.path.join(data_path, file)

        try:
            df = pd.read_csv(file_path)

            print(f"\nShape: {df.shape}")

            print("\nColumns:")
            print(df.columns.tolist())

            print("\nData Types:")
            print(df.dtypes)

            print("\nMissing Values Per Column:")
            print(df.isnull().sum())

            print("\nTotal Missing Values:")
            print(df.isnull().sum().sum())

            print("\nDuplicate Rows:")
            print(df.duplicated().sum())

            print("\nFirst 5 Rows:")
            print(df.head())

        except Exception as e:
            print(f"\nError reading file: {e}")