resource "aws_sqs_queue" "incident_queue" {

  name = "incident-queue"

  visibility_timeout_seconds = 60

  message_retention_seconds = 86400

  tags = local.common_tags
}

resource "aws_sqs_queue" "dead_letter" {

  name = "incident-dlq"

  message_retention_seconds = 1209600

  tags = local.common_tags
}
