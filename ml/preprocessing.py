"""
Feature Engineering Pipeline

Converts CloudWatch/Prometheus metrics into ML features.
"""

import pandas as pd


FEATURE_COLUMNS = [
    "cpu",
    "memory",
    "disk",
    "network_in",
    "network_out",
    "latency",
    "request_rate",
    "error_rate",
]


def load_dataset(filename: str):

    return pd.read_csv(filename)


def clean_dataframe(df):

    df = df.fillna(method="ffill")

    df = df.drop_duplicates()

    return df


def create_features(df):

    df["cpu_memory_ratio"] = df["cpu"] / (df["memory"] + 1)

    df["latency_error"] = (
        df["latency"] *
        df["error_rate"]
    )

    df["traffic_delta"] = (
        df["network_in"] -
        df["network_out"]
    )

    return df


def prepare(df):

    df = clean_dataframe(df)

    df = create_features(df)

    return df
