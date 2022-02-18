# -*- coding: utf-8 -*-

import os

jenkins_workspace = os.getenv('WORKSPACE')
job_name = os.getenv('JOB_NAME', 'noName')
remote = False if job_name == 'noName' else True
absPath = os.path.abspath('.')
env = os.getenv('PROJECT_ENV','development')
project = os.getenv('PROJECT_NAME','local')
xmlPathToSave = jenkins_workspace if jenkins_workspace else '%s/xmlresult/' % os.getcwd()
