import json

SERVICE_ACTIONS = {

    "ecs": "restart_ecs",

    "eks": "restart_pod",

    "redis": "flush_cache",

    "asg": "scale_out",

    "ec2": "restart_ec2",

    "database": "database_failover"

}


LOW = [

    "restart_ecs",

    "restart_pod",

    "flush_cache",

    "scale_out"

]


def lambda_handler(event, context):

    service = event.get("service", "ecs")

    action = SERVICE_ACTIONS.get(

        service,

        "restart_ecs"

    )

    if action in LOW:

        risk = "LOW"

    else:

        risk = "HIGH"

    return {

        "action": action,

        "risk": risk,

        "incident": event

    }
