## Robinfood
> DevOps Technical Test<br>
> author: eric.gnome@gmail.com

### General info

<p>The goal of this project is to implement modern automated infrastructure in wich
will be deployed a microservice using DevOps methodologies into AWS Cloud.</p>

### Tecnologies

* [Jenkins](https://www.jenkins.io)
* [Terraform 1.1.6](https://www.terraform.io)
* [Python 3](https://python.org)
* [Docker 20.10](https://www.docker.com)
* [AWS](https://aws.amazon.com)
* [Github](https://github.com/)

### Project Description

<p>The <i>Python microservice</i> executes a bounch of packages checks over a host, eather remote or local. Those automated test can be useful for testing infra, services and packages.</p>

<p>The microservice is builded and packaged with <i>Jenkins CI declarative pipeline</i> within a slave node.</p>

<p><i>Terraform and Jenkins CD pipeline</i> technologies were used for the delivery flow (infra provisioning and artifact delivery) for building the <i>ECS cluster</i>.

<p>Service's logs are sended to <i>Cloud Watch</i>, then proccess finished.</p>

### Project tree

```
. robinfood-devops-test
├── automation
│   ├── cd
│   │   └── Jenkinsfile
│   └── ci
│       └── Jenkinsfile
├── coding
│   └── checkSystemService
│       ├── defs
│       │   ├── constants.py
│       ├── Dockerfile
│       ├── __init__.py
│       ├── main.py
│       ├── requirements.in
│       ├── requirements.txt
│       └── tests
│           ├── __init__.py
│           └── tests.py
├── infra
│   └── terraform
│       ├── main.tf
│       ├── network.tf
│       ├── outputs.tf
│       ├── providers.tf
│       └── variables.tf
└── README.md
```


## Solution Design & Implementation

### Project repos
https://github.com/axelPalmerin/robinfood-devops-test<br>
https://hub.docker.com/repository/docker/axelherrera/pytest

 ### 1. Coding

<p>The microservice is written in python using the pytest serverspec. </p>

> For 3rd dependency management and project isolation we've been used pip-tools and virtualenv

#### Usage:
```
pip install virtualenv

# Create the  virtual environment
❯ cd coding/checkSystemService
❯ virtualenv myvenv

# Activate the virtualenv
❯ source myvenv/bin/activate

# Manage dependencies with pip-tools
❯ python -m pip install pip-tools
❯ pip-compile requirements.in

# Installing generated deps
❯ pip install -r requirements.txt
❯ pytest -v main.py
```

<img src="https://github.com/axelPalmerin/images/blob/main/pytest.png?raw=true" width="400"/>


#### Cleaning venv
```
❯ deactivate
❯ rm -rf myvenv
```

### 2. Infrastructure

#### Architecture Overview

The figure below shows the high-level architecture of the infrastructure we want to provision with Terraform

<img src="https://github.com/axelPalmerin/images/blob/main/infra.png?raw=true" width="500"/>

> File: infra/terraform

The main blocks of this infrastructure are the following:

* The network consisting of VPC with one public subnet and an Internet Gateway to grant public Internet access to the ECS services.
* A Route Table for the public subnet and the vpc gateway.
* An ECS cluster.
* A task definition that specifies the task to run.
* A Security group for allow http inbound connections to 8080 port and egress all traffic outbound.

> Note: The microservice doesn't creates a server, just execute the pyTest.

#### Building with terraform
```
terraform init
terraform validate
terraform plan
terraform apply --auto-approve
```
VPC

<img src="https://github.com/axelPalmerin/images/blob/main/vpc.png?raw=true" width="400" /><br>

ECS

<img src="https://github.com/axelPalmerin/images/blob/main/ecs.png?raw=true" width="100"/><br>

Services

<img src="https://github.com/axelPalmerin/images/blob/main/services.png?raw=true"  width="400" /><br>

Tasks

<img src="https://github.com/axelPalmerin/images/blob/main/tasks.png?raw=true" width="300"/><br>

Container

<img src="https://github.com/axelPalmerin/images/blob/main/container.png?raw=true" width="400"/><br>

CloudWatch

<img src="https://github.com/axelPalmerin/images/blob/main/log_group.png?raw=true" width="150"/><br>

Logs

<img src="https://github.com/axelPalmerin/images/blob/main/logs.png?raw=true" width="300"/><br>

### 3. Automation

> Overview CI/CD

<img src="https://github.com/axelPalmerin/images/blob/main/ppl_drawio.png?raw=true" width="400"/>


#### Build service with CI pipeline

> Jenkins contenerized image was used for orchestrate and automate with a persistent volume.

```
❯ docker image pull jenkins/jenkins:lts
  docker volume create jenkins-pv
  docker container run -d \
    -p 8080:8080 \
    -v jenkins-pv:/var/jenkins_home \
    --name jenkins-local \
    jenkins/jenkins:lts
```

<p>Then a slave node was configured with Terraform and Docker for run CI/CD flows.</p>


<img src="https://github.com/axelPalmerin/images/blob/main/slave.png?raw=true" width="250" /><br>


<p>Once Jenkins jobs are created, we run the CI flow.</p>

<img src="https://github.com/axelPalmerin/images/blob/main/jobs.png?raw=true" width="150" />

> File: automation/ci/Jenkinsfile

<img src="https://github.com/axelPalmerin/images/blob/main/ci.png?raw=true" width="500"/><br>

<p>A Docker image of the service is pulling in the public repository</p>

<img src="https://github.com/axelPalmerin/images/blob/main/docker_repo.png?raw=true" width="160" />


#### Deploy service with CD pipeline

<p>The CD workflow creates the AWS infra and deploy our latest dockerized service to a service->task on ECS cluster</p>

> File: automation/cd/Jenkinsfile

<p>The CD pipeline asks for automatically auto approve the terraform plan and eather keep or destroy the plan.</p>

<img src="https://github.com/axelPalmerin/images/blob/main/cd_args.png?raw=true" width="160" />

> Running the Job:

<img src="https://github.com/axelPalmerin/images/blob/main/cd.png?raw=true" width="500"/><br>

<p><b><i>Happy coding! :D</i></b></p>

### References

* [AWS ECS](https://aws.amazon.com/es/ecs/)
* [terraform ECS](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_service)
* [pytest-testinfra](https://testinfra.readthedocs.io/en/latest/)
