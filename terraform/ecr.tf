resource "aws_ecr_repository" "lambda_repo" {

  name = "self-healing-lambda"

  image_scanning_configuration {

    scan_on_push = true

  }

  image_tag_mutability = "MUTABLE"

  tags = local.common_tags
}

resource "aws_ecr_repository" "ml_repo" {

  name = "self-healing-ml"

  image_scanning_configuration {

    scan_on_push = true

  }

  image_tag_mutability = "MUTABLE"

  tags = local.common_tags
}
