terraform {

  backend "s3" {

    bucket = "self-healing-terraform-state"

    key = "terraform.tfstate"

    region = "us-east-1"

    encrypt = true

  }

}
