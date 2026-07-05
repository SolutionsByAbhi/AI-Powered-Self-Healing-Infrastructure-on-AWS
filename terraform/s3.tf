resource "aws_s3_bucket" "incident_store" {
bucket = "${var.project_name}-${var.environment}-incident-store"

tags = local.common_tags
}

resource "aws_s3_bucket_versioning" "incident_store" {
bucket = aws_s3_bucket.incident_store.id

versioning_configuration {
status = "Enabled"
}
}
