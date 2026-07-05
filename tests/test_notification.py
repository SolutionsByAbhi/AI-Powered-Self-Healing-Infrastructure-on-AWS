from unittest.mock import patch

from lambda.notification_router import lambda_handler


@patch(
    "lambda.notification_router.notify_email"
)

@patch(
    "lambda.notification_router.notify_slack"
)

def test_notification(

    slack,

    email

):

    lambda_handler(

        {

            "severity": "HIGH",

            "message": "Test"

        },

        None

    )

    assert slack.called

    assert email.called
