import json
import uuid
from datetime import datetime


def generate_id():

    return str(uuid.uuid4())


def utc_now():

    return datetime.utcnow().isoformat()


def success(data):

    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }


def failure(message, code=500):

    return {
        "statusCode": code,
        "body": json.dumps(
            {
                "error": message
            }
        )
    }
