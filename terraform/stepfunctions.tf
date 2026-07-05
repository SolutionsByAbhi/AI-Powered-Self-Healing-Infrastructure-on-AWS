resource "aws_sfn_state_machine" "self_healing" {

  name     = "self-healing-workflow"
  role_arn = aws_iam_role.step_function_role.arn

  definition = file("${path.module}/../stepfunctions/self_healing_workflow.asl.json")

  tags = local.common_tags
}
