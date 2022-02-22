
# Fetch AZs in the current region
data "aws_availability_zones" "available" {
  state = "available"
}

# ECS VPC
resource "aws_vpc" "ecs_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "VPC for ecs"
  }
}

# Public subnet
resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.ecs_vpc.id
  cidr_block = "10.0.0.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "Public Subnet"
  }
}

# Gateway VPC allow Internet traffic flow to the Public Subnet
resource "aws_internet_gateway" "ecs_vpc_igw" {
  vpc_id = aws_vpc.ecs_vpc.id

  tags = {
    Name = "ECS VPC - Internet Gateway"
  }
}

# Public Route table for the VPC Gateway
resource "aws_route_table" "vpc_us_east_1a_public" {
    vpc_id = aws_vpc.ecs_vpc.id

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.ecs_vpc_igw.id
    }

    tags = {
        Name = "Public Subnet Route Table."
    }
}

# Create association between the Route Table and Subnet
resource "aws_route_table_association" "vpc_us_east_1a_public" {
    subnet_id = aws_subnet.public.id
    route_table_id = aws_route_table.vpc_us_east_1a_public.id
}

# SG for allow http
resource "aws_security_group" "allow_http" {
  name        = "allow_http_sg"
  description = "Allow http inbound connections"
  vpc_id = aws_vpc.ecs_vpc.id

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_http_sg"
  }
}
