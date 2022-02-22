
# variables

variable "region" {
  default = "us-east-1"
}

variable "app_image" {
  description = "Docker image to run in the ECS cluster"
  default     = "axelherrera/pytest:latest"
}
