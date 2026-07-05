from bedrock.root_cause_analysis import analyze


def lambda_handler(event, context):

    metrics = event["metrics"]

    analysis = analyze(metrics)

    return {

        "analysis": analysis,

        "metrics": metrics

    }
