import os
from testinfra import get_host

jenkins_workspace = os.getenv('WORKSPACE')
job_name = os.getenv('JOB_NAME', 'noName')
env = os.getenv('PROJECT_ENV','development')
project = os.getenv('PROJECT_NAME','local')
host = get_host(os.getenv("HOST", "local://"))
