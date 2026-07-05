resource "aws_kms_key" "incident_key" {

  description = "Encryption Key"

  deletion_window_in_days = 7

  enable_key_rotation = true

  tags = local.common_tags
}
