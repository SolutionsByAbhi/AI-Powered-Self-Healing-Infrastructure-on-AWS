import json
import boto3
import os

from utils import (
generate_incident_id,
save_incident,
archive_incident,
timestamp
)

lambda_client = boto3.client("lambda")

TABLE_NAME = os.environ["INCIDENT_TABLE"]
BUCKET_NAME = os.environ["INCIDENT_BUCKET"]

def lambda_handler(event, context):

```
incident_id = generate_incident_id()

anomaly_score = event.get(
    "anomaly_score",
    0
)

service = event.get(
    "service",
    "unknown"
)

incident = {
    "incident_id": incident_id,
    "service": service,
    "anomaly_score": anomaly_score,
    "created_at": timestamp(),
    "status": "OPEN"
}

save_incident(
    TABLE_NAME,
    incident
)

archive_incident(
    BUCKET_NAME,
    incident_id,
    incident
)

response = lambda_client.invoke(
    FunctionName="remediation-engine",
    InvocationType="Event",
    Payload=json.dumps(incident)
)

return {
    "statusCode": 200,
    "incident_id": incident_id
}
```
