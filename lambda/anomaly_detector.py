from predictor import classify


class Detector:

    def detect(self, metrics):

        prediction = classify(metrics)

        return {

            "anomaly": prediction["anomaly"],

            "confidence": prediction["confidence"],

            "score": prediction["score"]

        }


detector = Detector()


def lambda_handler(event, context):

    return detector.detect(

        event["metrics"]

    )
