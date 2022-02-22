# Creation of ECS cluster
resource "aws_ecs_cluster" "ecs_cluster" {
  name = "ecs-cluster"
}

# ECS Task definition
resource "aws_ecs_task_definition" "pytest-task" {
  family                   = "pytest-task"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  memory                   = 512
  cpu                      = 256
  execution_role_arn       = aws_iam_role.ecsTaskExecutionRole.arn
  container_definitions    = <<DEFINITION
  [
    {
      "name": "pytest-task",
      "image": "${var.app_image}",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 8080,
          "hostPort": 8080
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/fargate/service/app",
          "awslogs-region": "${var.region}",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "memory": 512,
      "cpu": 256
    }
  ]
  DEFINITION
}

# Service definition
resource "aws_ecs_service" "pytest_service" {
  name            = "pytest-service"
  cluster         = "${aws_ecs_cluster.ecs_cluster.id}"  # created Cluster
  task_definition = "${aws_ecs_task_definition.pytest-task.arn}" # task our service
  launch_type     = "FARGATE"
  desired_count   = 1 # number of containers we want deploy

  # Reference srv to public subnet
  network_configuration {
      subnets          = ["${aws_subnet.public.id}"]
      assign_public_ip = true # Providing our containers with public IPs
    }
}

#
# ARN Role for logs
#

resource "aws_iam_role" "ecsTaskExecutionRole" {
  name               = "app-ecs"
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
}

data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "ecsTaskExecutionRole_policy" {
  role       = aws_iam_role.ecsTaskExecutionRole.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

variable "logs_retention_in_days" {
  type        = number
  default     = 1
  description = "Specifies the number of days you want to retain log events"
}

resource "aws_cloudwatch_log_group" "logs" {
  name              = "/fargate/service/app"
  retention_in_days = var.logs_retention_in_days
  #tags
}
