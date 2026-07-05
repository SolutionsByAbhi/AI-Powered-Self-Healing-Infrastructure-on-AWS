resource "aws_apigatewayv2_api" "self_healing_api" {

  name          = "self-healing-api"

  protocol_type = "HTTP"

  tags = local.common_tags
}

resource "aws_apigatewayv2_integration" "ingress" {

  api_id = aws_apigatewayv2_api.self_healing_api.id

  integration_type = "AWS_PROXY"

  integration_uri = aws_lambda_function.anomaly_handler.invoke_arn

  integration_method = "POST"

  payload_format_version = "2.0"
}

resource "aws_apigatewayv2_route" "ingress" {

  api_id = aws_apigatewayv2_api.self_healing_api.id

  route_key = "POST /incident"

  target = "integrations/${aws_apigatewayv2_integration.ingress.id}"
}

resource "aws_apigatewayv2_stage" "default" {

  api_id = aws_apigatewayv2_api.self_healing_api.id

  name = "$default"

  auto_deploy = true
}

resource "aws_lambda_permission" "api_gateway" {

  statement_id = "AllowAPIGatewayInvoke"

  action = "lambda:InvokeFunction"

  function_name = aws_lambda_function.anomaly_handler.function_name

  principal = "apigateway.amazonaws.com"

  source_arn = "${aws_apigatewayv2_api.self_healing_api.execution_arn}/*/*"
}
