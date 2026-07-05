variable "aws_region" {
default = "us-east-1"
}

variable "project_name" {
default = "ai-self-healing"
}

variable "environment" {
default = "dev"
}

variable "sagemaker_endpoint_name" {
default = "anomaly-detector-endpoint"
}

variable "slack_webhook_url" {
sensitive = true
}

variable "approval_sns_email" {
default = "[admin@example.com](mailto:admin@example.com)"
}
