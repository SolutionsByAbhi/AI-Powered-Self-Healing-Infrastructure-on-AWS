import boto3
from datetime import datetime

client = boto3.resource(
    "dynamodb"
)


class IncidentRepository:

    def __init__(

        self,

        table_name

    ):

        self.table = client.Table(

            table_name

        )

    def save(

        self,

        incident

    ):

        incident["created_at"] = (

            datetime.utcnow()

            .isoformat()

        )

        self.table.put_item(

            Item=incident

        )

    def update(

        self,

        incident_id,

        status

    ):

        self.table.update_item(

            Key={

                "incident_id": incident_id

            },

            UpdateExpression="SET #s=:s",

            ExpressionAttributeNames={

                "#s": "status"

            },

            ExpressionAttributeValues={

                ":s": status

            }

        )
