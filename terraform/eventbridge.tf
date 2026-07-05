resource "aws_cloudwatch_event_rule" "anomaly_detected" {

  name        = "anomaly-detected"
  description = "Triggers Lambda when an anomaly event is published."

  event_pattern = jsonencode({
    source = [
      "selfhealing.anomaly"
    ]

    detail-type = [
      "AnomalyDetected"
    ]
  })

  tags = local.common_tags
}

resource "aws_cloudwatch_event_target" "lambda_target" {

  rule = aws_cloudwatch_event_rule.anomaly_detected.name

  target_id = "AnomalyHandler"

  arn = aws_lambda_function.anomaly_handler.arn
}

resource "aws_lambda_permission" "allow_eventbridge" {

  statement_id = "AllowExecutionFromEventBridge"

  action = "lambda:InvokeFunction"

  function_name = aws_lambda_function.anomaly_handler.function_name

  principal = "events.amazonaws.com"

  source_arn = aws_cloudwatch_event_rule.anomaly_detected.arn
}
