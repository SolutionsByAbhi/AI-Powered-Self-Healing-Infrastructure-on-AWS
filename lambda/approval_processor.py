from notifier import (

    notify_email,

    notify_slack

)


def lambda_handler(event, context):

    message = f"""

Approval Required

Incident:

{event["incident_id"]}

Action:

{event["action"]}

"""

    notify_email(message)

    notify_slack(message)

    return {

        "approval_sent": True

    }
