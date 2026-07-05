from notifier import (
    notify_email,
    notify_slack
)


def lambda_handler(event, context):

    severity = event.get(

        "severity",

        "LOW"

    )

    message = event.get(

        "message"

    )

    if severity == "LOW":

        notify_slack(message)

    else:

        notify_email(message)

        notify_slack(message)

    return {

        "sent": True

    }
