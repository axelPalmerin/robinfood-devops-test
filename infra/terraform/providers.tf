
# AWS and docker provider

terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.15.0"
    }
  }
}

provider "docker" {}

provider "aws" {
  region = var.region
}
