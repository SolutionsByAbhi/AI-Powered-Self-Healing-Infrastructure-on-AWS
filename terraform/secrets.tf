resource "aws_secretsmanager_secret" "slack" {

  name = "self-healing-slack"

  tags = local.common_tags
}

resource "aws_secretsmanager_secret_version" "slack" {

  secret_id = aws_secretsmanager_secret.slack.id

  secret_string = jsonencode({

    webhook = var.slack_webhook_url

  })
}
