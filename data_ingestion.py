import pandas as pd
import os

DATA_PATH = "data/raw"

for file in os.listdir(DATA_PATH):

    if file.endswith(".csv"):

        path = os.path.join(DATA_PATH, file)

        try:
            df = pd.read_csv(path)

            print("\n" + "="*70)
            print(f"FILE: {file}")

            print("\nShape:")
            print(df.shape)

            print("\nData Types:")
            print(df.dtypes)

            print("\nMissing Values:")
            print(df.isnull().sum())

            print("\nDuplicate Rows:")
            print(df.duplicated().sum())

            print("\nHead:")
            print(df.head())

        except Exception as e:
            print(f"Error reading {file}: {e}")