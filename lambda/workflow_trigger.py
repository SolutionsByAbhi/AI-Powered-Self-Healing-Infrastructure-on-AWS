import json

from config import STEP_FUNCTION

from stepfunction import Workflow


workflow = Workflow(STEP_FUNCTION)


def lambda_handler(event, context):

    execution = workflow.start(

        json.dumps(event)

    )

    return {

        "executionArn": execution

    }
