import boto3
import json

runtime = boto3.client(
    "sagemaker-runtime"
)


class Predictor:

    def __init__(

        self,

        endpoint

    ):

        self.endpoint = endpoint

    def predict(

        self,

        metrics

    ):

        response = runtime.invoke_endpoint(

            EndpointName=self.endpoint,

            Body=json.dumps(metrics),

            ContentType="application/json"

        )

        return json.loads(

            response["Body"].read()

        )
