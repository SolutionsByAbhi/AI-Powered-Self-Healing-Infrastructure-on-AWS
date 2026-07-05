import boto3

ssm = boto3.client("ssm")


def lambda_handler(event, context):

    response = ssm.start_automation_execution(

        DocumentName="RollbackDeployment"

    )

    return {

        "rollback": True,

        "execution":

        response["AutomationExecutionId"]

    }
