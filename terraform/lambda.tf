resource "aws_lambda_function" "anomaly_handler" {

function_name = "anomaly-handler"

role = aws_iam_role.lambda_role.arn

runtime = "python3.11"

handler = "anomaly_handler.lambda_handler"

filename = "../build/anomaly_handler.zip"

timeout = 60

environment {
variables = {
INCIDENT_TABLE = aws_dynamodb_table.incident_history.name
INCIDENT_BUCKET = aws_s3_bucket.incident_store.bucket
}
}

tags = local.common_tags
}
