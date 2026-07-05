resource "aws_sns_topic" "approval_topic" {
name = "self-healing-approvals"
}

resource "aws_sns_topic_subscription" "email" {
topic_arn = aws_sns_topic.approval_topic.arn
protocol  = "email"
endpoint  = var.approval_sns_email
}
