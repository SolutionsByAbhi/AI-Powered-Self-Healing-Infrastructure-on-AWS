import boto3

cloudwatch = boto3.client(
    "cloudwatch"
)


def lambda_handler(event, context):

    cloudwatch.list_metrics()

    return {

        "status": "UP"

    }
