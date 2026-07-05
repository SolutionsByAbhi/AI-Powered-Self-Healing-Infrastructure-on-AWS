import json
import boto3
from generate_metrics import metric

events = boto3.client("events")


def publish():

    payload = metric()

    events.put_events(

        Entries=[

            {

                "Source": "selfhealing.anomaly",

                "DetailType": "AnomalyDetected",

                "Detail": json.dumps(payload),

                "EventBusName": "default"

            }

        ]

    )

    print("Published Event")


if __name__ == "__main__":

    publish()
