import boto3

cw = boto3.client("cloudwatch")


def publish(

    metric,

    value

):

    cw.put_metric_data(

        Namespace="SelfHealing",

        MetricData=[

            {

                "MetricName": metric,

                "Value": value,

                "Unit": "Count"

            }

        ]

    )
