from unittest.mock import patch

from bedrock.root_cause_analysis import analyze


@patch(
    "bedrock.root_cause_analysis.bedrock.invoke_model"
)
def test_analysis(mock_bedrock):

    mock_bedrock.return_value = {

        "body": type(

            "Mock",

            (), {

                "read": lambda self: b'{"results":[{"outputText":"CPU saturation"}]}'

            }

        )()

    }

    output = analyze(

        {

            "cpu": 95

        }

    )

    assert "CPU" in output
