resource "aws_cloudwatch_metric_alarm" "high_memory" {

  alarm_name = "HighMemory"

  namespace = "CWAgent"

  metric_name = "mem_used_percent"

  comparison_operator = "GreaterThanThreshold"

  threshold = 85

  evaluation_periods = 2

  statistic = "Average"

  period = 300

  alarm_actions = [

    aws_sns_topic.approval_topic.arn

  ]
}

resource "aws_cloudwatch_metric_alarm" "high_disk" {

  alarm_name = "HighDisk"

  namespace = "CWAgent"

  metric_name = "disk_used_percent"

  comparison_operator = "GreaterThanThreshold"

  threshold = 90

  evaluation_periods = 2

  statistic = "Average"

  period = 300

  alarm_actions = [

    aws_sns_topic.approval_topic.arn

  ]
}
