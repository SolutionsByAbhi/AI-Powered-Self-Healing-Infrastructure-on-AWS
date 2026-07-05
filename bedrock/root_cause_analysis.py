import json
import boto3

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)


MODEL_ID = "amazon.titan-text-lite-v1"


PROMPT = """
You are an AWS Site Reliability Engineer.

Analyze the infrastructure metrics and determine:

1. Root Cause
2. Severity
3. Recommended Action
4. Confidence

Metrics:

{}
"""


def analyze(metrics):

    body = {
        "inputText": PROMPT.format(
            json.dumps(metrics, indent=2)
        ),
        "textGenerationConfig": {
            "maxTokenCount": 300,
            "temperature": 0.2,
            "topP": 0.9
        }
    }

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    result = json.loads(
        response["body"].read()
    )

    return result["results"][0]["outputText"]
