resource "aws_sagemaker_model" "anomaly_detector" {

  name = "anomaly-detector"

  execution_role_arn = aws_iam_role.lambda_role.arn

  primary_container {

    image = "${aws_ecr_repository.ml_repo.repository_url}:latest"

    mode = "SingleModel"

    environment = {
      MODEL_NAME = "isolation-forest"
    }
  }

  tags = local.common_tags
}

resource "aws_sagemaker_endpoint_configuration" "anomaly_detector" {

  name = "anomaly-endpoint-config"

  production_variants {

    variant_name = "primary"

    model_name = aws_sagemaker_model.anomaly_detector.name

    instance_type = "ml.t2.medium"

    initial_instance_count = 1

    initial_variant_weight = 1
  }
}

resource "aws_sagemaker_endpoint" "anomaly_detector" {

  name = "anomaly-detector-endpoint"

  endpoint_config_name = aws_sagemaker_endpoint_configuration.anomaly_detector.name

  tags = local.common_tags
}
