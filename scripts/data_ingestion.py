"""
Data Ingestion Module.

This script loads raw mutual fund datasets,
fetches live NAV data from MFAPI,
and stores the data for further processing.
"""

import pandas as pd
import os

raw_path = "data/raw"

for file in sorted(os.listdir(raw_path)):
    if file.endswith(".csv"):

        file_path = os.path.join(raw_path, file)

        df = pd.read_csv(file_path)

        print("\n" + "="*50)
        print("Dataset:", file)

        print("Shape:", df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())