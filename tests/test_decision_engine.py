from lambda.decision_engine import lambda_handler


def test_ecs():

    result = lambda_handler(

        {

            "service": "ecs"

        },

        None

    )

    assert result["action"] == "restart_ecs"

    assert result["risk"] == "LOW"


def test_database():

    result = lambda_handler(

        {

            "service": "database"

        },

        None

    )

    assert result["risk"] == "HIGH"
