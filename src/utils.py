"""
Utility functions for the Moroccan E-Commerce Data Platform.
"""

import random
from pathlib import Path

import numpy as np
import pandas as pd

from config import (
    RANDOM_SEED,
    BRL_TO_MAD,
    YEAR_OFFSET,
    ZIP_MIN,
    ZIP_MAX,
    LAT_MIN,
    LAT_MAX,
    LON_MIN,
    LON_MAX,
)

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# CSV LOADER
def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

# CSV SAVER
def save_csv(df: pd.DataFrame, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Saved -> {path}")

#MAPPING LOADER

def load_mapping(path, source_column, target_column):
    mapping = pd.read_csv(path)
    return dict(
        zip(
            mapping[source_column],
            mapping[target_column]
        )
    )

#CURRENCY
def convert_currency(series):
    return (series * BRL_TO_MAD).round(2)

#DATE
def shift_dates(df, columns):
    df = df.copy()
    for column in columns:
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )
        df[column] = (
            df[column]
            + pd.DateOffset(years=YEAR_OFFSET)
        )
    return df

#ZIP CODES
def generate_zip_codes(size):
    return np.random.randint(
        ZIP_MIN,
        ZIP_MAX,
        size=size
    )

#LATITUDE
def generate_latitudes(size):
    return np.random.uniform(
        LAT_MIN,
        LAT_MAX,
        size
    ).round(6)

#LONGITUDE
def generate_longitudes(size):
    return np.random.uniform(
        LON_MIN,
        LON_MAX,
        size
    ).round(6)

#SUMMARY
def summarize_dataset(name, df):

    print("=" * 80)

    print(name.upper())

    print("=" * 80)

    print(f"Rows    : {df.shape[0]:,}")

    print(f"Columns : {df.shape[1]}")

    print(f"Missing : {df.isna().sum().sum():,}")

    print(f"Duplicates : {df.duplicated().sum():,}")

    print()

#LOGGER
def log_transformation(message):

    print(f"[INFO] {message}")

#VALUE COUNT
def compare_before_after(before, after, column):

    comparison = pd.DataFrame({

        "Before": before[column].value_counts(),

        "After": after[column].value_counts()

    })

    return comparison.fillna(0)

#UNIQUE VALUE
def unique_count(df):

    return pd.DataFrame({

        "Unique Values": df.nunique()

    })