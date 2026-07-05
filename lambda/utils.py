import json
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
s3 = boto3.client("s3")

def generate_incident_id():
return str(uuid.uuid4())

def timestamp():
return datetime.utcnow().isoformat()

def save_incident(
table_name,
incident
):

```
table = dynamodb.Table(table_name)

table.put_item(
    Item=incident
)
```

def archive_incident(
bucket,
incident_id,
payload
):

```
s3.put_object(
    Bucket=bucket,
    Key=f"incidents/{incident_id}.json",
    Body=json.dumps(payload)
)
```
