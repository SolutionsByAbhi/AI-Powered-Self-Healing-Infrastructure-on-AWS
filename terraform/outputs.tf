output "incident_bucket" {

  value = aws_s3_bucket.incident_store.bucket
}

output "incident_table" {

  value = aws_dynamodb_table.incident_history.name
}

output "lambda_function" {

  value = aws_lambda_function.anomaly_handler.function_name
}

output "sns_topic" {

  value = aws_sns_topic.approval_topic.arn
}
