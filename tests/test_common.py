from lambda.common import (

    generate_id,

    success,

    failure

)


def test_success():

    response = success(

        {

            "hello": "world"

        }

    )

    assert response["statusCode"] == 200


def test_failure():

    response = failure(

        "failed"

    )

    assert response["statusCode"] == 500


def test_uuid():

    assert generate_id()
