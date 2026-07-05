import json
import boto3

client = boto3.client("s3")


class Archive:

    def __init__(

        self,

        bucket

    ):

        self.bucket = bucket

    def store(

        self,

        incident

    ):

        client.put_object(

            Bucket=self.bucket,

            Key=f"incidents/{incident['incident_id']}.json",

            Body=json.dumps(

                incident,

                indent=2

            )

        )
