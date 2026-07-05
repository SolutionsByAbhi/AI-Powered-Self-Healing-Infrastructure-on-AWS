from unittest.mock import patch

from lambda.stepfunction import Workflow


@patch(
    "lambda.stepfunction.client.start_execution"
)
def test_workflow(mock_execution):

    mock_execution.return_value = {

        "executionArn": "arn"

    }

    wf = Workflow("arn")

    execution = wf.start("{}")

    assert execution == "arn"
