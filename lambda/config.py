import os

AWS_REGION = os.getenv(
    "AWS_REGION",
    "us-east-1"
)

INCIDENT_TABLE = os.getenv(
    "INCIDENT_TABLE"
)

INCIDENT_BUCKET = os.getenv(
    "INCIDENT_BUCKET"
)

SNS_TOPIC = os.getenv(
    "SNS_TOPIC"
)

STEP_FUNCTION = os.getenv(
    "STEP_FUNCTION"
)

MODEL_ENDPOINT = os.getenv(
    "MODEL_ENDPOINT"
)

SLACK_WEBHOOK = os.getenv(
    "SLACK_WEBHOOK"
)

RISK_THRESHOLD = float(
    os.getenv(
        "RISK_THRESHOLD",
        "0.75"
    )
)
