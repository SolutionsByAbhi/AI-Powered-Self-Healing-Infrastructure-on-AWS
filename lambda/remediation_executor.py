import boto3

ssm = boto3.client("ssm")

DOCUMENTS = {

    "restart_ecs": "RestartECS",

    "restart_pod": "RestartEKSPod",

    "scale_out": "ScaleASG",

    "flush_cache": "FlushCache",

    "restart_ec2": "RestartEC2",

    "database_failover": "FailoverRDS"

}


def lambda_handler(event, context):

    action = event["action"]

    document = DOCUMENTS[action]

    response = ssm.start_automation_execution(

        DocumentName=document

    )

    return {

        "status": "EXECUTED",

        "automation_execution_id":

        response["AutomationExecutionId"]

    }
