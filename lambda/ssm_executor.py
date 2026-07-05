import boto3

from runbook_selector import select

ssm = boto3.client("ssm")


def execute(action):

    document = select(action)

    response = ssm.start_automation_execution(

        DocumentName=document

    )

    return response


def lambda_handler(event, context):

    response = execute(

        event["action"]

    )

    return {

        "automation_execution_id":

        response["AutomationExecutionId"]

    }
