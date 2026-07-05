import os
import json
import urllib3

http = urllib3.PoolManager()

WEBHOOK = os.getenv("SLACK_WEBHOOK")


def send(message):

    http.request(

        "POST",

        WEBHOOK,

        body=json.dumps({

            "text": message

        }),

        headers={

            "Content-Type": "application/json"

        }

    )
