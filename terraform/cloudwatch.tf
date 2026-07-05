resource "aws_cloudwatch_log_group" "lambda_logs" {

  name = "/aws/lambda/anomaly-handler"

  retention_in_days = 30

  tags = local.common_tags
}

resource "aws_cloudwatch_metric_alarm" "high_cpu" {

  alarm_name = "HighCPU"

  comparison_operator = "GreaterThanThreshold"

  evaluation_periods = 2

  metric_name = "CPUUtilization"

  namespace = "AWS/EC2"

  period = 300

  statistic = "Average"

  threshold = 80

  alarm_description = "High CPU detected"

  alarm_actions = [
    aws_sns_topic.approval_topic.arn
  ]
}
