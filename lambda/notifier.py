import json
import os
import boto3
import urllib3

sns = boto3.client("sns")

http = urllib3.PoolManager()

SNS_TOPIC = os.environ["SNS_TOPIC"]

SLACK_WEBHOOK = os.environ["SLACK_WEBHOOK"]


def notify_slack(message):

    payload = {
        "text": message
    }

    http.request(
        "POST",
        SLACK_WEBHOOK,
        body=json.dumps(payload),
        headers={
            "Content-Type": "application/json"
        }
    )


def notify_email(message):

    sns.publish(
        TopicArn=SNS_TOPIC,
        Subject="Self Healing Notification",
        Message=message
    )
