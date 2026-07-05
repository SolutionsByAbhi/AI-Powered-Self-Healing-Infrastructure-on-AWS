from logger import log


def lambda_handler(event, context):

    detail = event.get("detail", {})

    service = detail.get("service", "ecs")

    metrics = detail.get("metrics", {})

    log(

        "INFO",

        "Event Received",

        service=service

    )

    return {

        "service": service,

        "metrics": metrics

    }
