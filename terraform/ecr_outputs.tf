output "lambda_repository" {

  value = aws_ecr_repository.lambda_repo.repository_url
}

output "ml_repository" {

  value = aws_ecr_repository.ml_repo.repository_url
}
