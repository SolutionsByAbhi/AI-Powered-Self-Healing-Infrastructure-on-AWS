import boto3

client = boto3.client(
    "sagemaker"
)


def deploy(

    endpoint,

    config

):

    client.create_endpoint(

        EndpointName=endpoint,

        EndpointConfigName=config

    )
