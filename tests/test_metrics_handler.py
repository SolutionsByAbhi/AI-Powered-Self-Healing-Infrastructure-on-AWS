from lambda.metrics_handler import lambda_handler


def test_handler(

    sample_metrics,

    monkeypatch

):

    class MockPredictor:

        def predict(

            self,

            metrics

        ):

            return {

                "anomaly": True

            }

    monkeypatch.setattr(

        "lambda.metrics_handler.predictor",

        MockPredictor()

    )

    result = lambda_handler(

        {

            "metrics": sample_metrics

        },

        None

    )

    assert result["prediction"]["anomaly"]
