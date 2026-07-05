import boto3

client = boto3.client(
    "stepfunctions"
)


class Workflow:

    def __init__(

        self,

        arn

    ):

        self.arn = arn

    def start(

        self,

        payload

    ):

        response = client.start_execution(

            stateMachineArn=self.arn,

            input=payload

        )

        return response[
            "executionArn"
        ]
