import json

from logger import log

from model import Predictor

from config import MODEL_ENDPOINT


predictor = Predictor(MODEL_ENDPOINT)


def lambda_handler(event, context):

    metrics = event["metrics"]

    prediction = predictor.predict(metrics)

    log(

        "INFO",

        "Prediction Complete",

        prediction=prediction

    )

    return {

        "prediction": prediction,

        "metrics": metrics

    }
