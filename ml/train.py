"""
Model Training

Isolation Forest is used because
most production incidents are anomalies.
"""

import joblib

from sklearn.ensemble import IsolationForest

from preprocessing import (
    load_dataset,
    prepare
)

MODEL_FILE = "model.joblib"


def train():

    df = load_dataset("sample_dataset.csv")

    df = prepare(df)

    features = df.drop(columns=["timestamp"])

    model = IsolationForest(

        contamination=0.02,

        random_state=42,

        n_estimators=200
    )

    model.fit(features)

    joblib.dump(

        model,

        MODEL_FILE
    )

    print("Training Complete")


if __name__ == "__main__":

    train()
