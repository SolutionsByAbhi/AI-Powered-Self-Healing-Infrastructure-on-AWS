"""
Lambda-compatible prediction wrapper.
"""

from inference import predict


def classify(metrics):

    result = predict(metrics)

    anomaly = result["prediction"] == -1

    return {

        "anomaly": anomaly,

        "confidence": abs(result["score"]),

        "score": result["score"]

    }
