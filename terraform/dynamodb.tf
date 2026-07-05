resource "aws_dynamodb_table" "incident_history" {

name         = "incident-history"
billing_mode = "PAY_PER_REQUEST"

hash_key = "incident_id"

attribute {
name = "incident_id"
type = "S"
}

tags = local.common_tags
}
