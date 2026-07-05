import json

import boto3

logs = boto3.client("logs")


def write(

    group,

    stream,

    payload

):

    logs.put_log_events(

        logGroupName=group,

        logStreamName=stream,

        logEvents=[

            {

                "timestamp": 0,

                "message": json.dumps(payload)

            }

        ]

    )
