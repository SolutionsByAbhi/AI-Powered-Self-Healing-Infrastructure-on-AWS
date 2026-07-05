import json
import boto3

s3 = boto3.client("s3")


def generate(bucket, incident):

    filename = f"{incident['incident_id']}.json"

    s3.put_object(

        Bucket=bucket,

        Key=f"reports/{filename}",

        Body=json.dumps(

            incident,

            indent=2

        )

    )

    return filename
