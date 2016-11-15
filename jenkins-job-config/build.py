#!/usr/bin/env python
import os
import subprocess

jobs_config_path = "jobs"
jobs_list = ["orio-tests.yaml",
            ]
command = "jenkins-job-builder --conf /home/jenkins_home/jjb.conf update {}"

for job in jobs_list:
  path = os.path.join(jobs_config_path, job)
  cmd = command.format(path)
  subprocess.call(cmd.split())

