resource "aws_cloudwatch_log_group" "stepfunctions" {

  name = "/aws/vendedlogs/states/self-healing"

  retention_in_days = 30

  tags = local.common_tags
}

resource "aws_cloudwatch_log_group" "decision_engine" {

  name = "/aws/lambda/decision-engine"

  retention_in_days = 30

  tags = local.common_tags
}
