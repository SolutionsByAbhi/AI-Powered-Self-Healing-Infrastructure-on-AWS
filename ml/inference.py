"""
Inference Module

Loads trained model
and predicts anomaly.
"""

import joblib
import pandas as pd

MODEL = joblib.load("model.joblib")


def predict(metrics):

    df = pd.DataFrame([metrics])

    prediction = MODEL.predict(df)

    score = MODEL.decision_function(df)

    return {

        "prediction": int(prediction[0]),

        "score": float(score[0])

    }
