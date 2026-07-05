import os

from notifier import notify_slack


HIGH_RISK = [
    "rollback",
    "db_failover",
    "traffic_shift"
]


def requires_approval(action):

    return action in HIGH_RISK


def lambda_handler(event, context):

    action = event["action"]

    if requires_approval(action):

        notify_slack(
            f"""
Approval Required

Service : {event['service']}

Action : {action}

Incident : {event['incident_id']}

Approve?

"""
        )

        return {
            "status": "WAITING_APPROVAL"
        }

    return {
        "status": "AUTO_APPROVED"
    }
