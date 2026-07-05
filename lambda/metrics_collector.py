import boto3

cloudwatch = boto3.client("cloudwatch")


def get_metric(namespace, metric):

    response = cloudwatch.get_metric_statistics(

        Namespace=namespace,

        MetricName=metric,

        StartTime="2026-01-01T00:00:00Z",

        EndTime="2026-01-01T00:10:00Z",

        Period=300,

        Statistics=["Average"]

    )

    datapoints = response.get("Datapoints", [])

    if not datapoints:

        return 0

    return datapoints[-1]["Average"]


def lambda_handler(event, context):

    return {

        "cpu": get_metric(

            "AWS/EC2",

            "CPUUtilization"

        )

    }
