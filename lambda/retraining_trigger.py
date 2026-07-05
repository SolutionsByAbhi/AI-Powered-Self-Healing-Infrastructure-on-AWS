import boto3

sm = boto3.client("sagemaker")


def lambda_handler(event, context):

    sm.start_pipeline_execution(

        PipelineName="self-healing-training"

    )

    return {

        "started": True

    }
