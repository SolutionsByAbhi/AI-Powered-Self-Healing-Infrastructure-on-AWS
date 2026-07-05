locals {

  application_name = "AI Self Healing"

  owner = "Demo"

  tags = {

    Project = local.application_name

    Owner = local.owner

    Environment = var.environment

    ManagedBy = "Terraform"

  }

}
