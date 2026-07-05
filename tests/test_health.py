from lambda.healthcheck import lambda_handler


def test_health():

    result = lambda_handler(

        {},

        None

    )

    assert result["status"] == "UP"
