SudoCode
========
SudoCode utilizes Jenkins, Docker and Jenkins-Job-Builder to keep contiuous integration
entirely in code. No need for manual configuration at any point. 

# Installing
- Be sure to have the latest version of Docker installed.
- Needs python 2.7
- Need appropriate credentials stored in /root/cred folder. 

```
git clone https://github.com/hpcl/continuous-integration
python continuous-integration/docker-images/jenkins/build.py
python continuous-integration/docker-images/jenkins-slave/build.py
docker run -d -p 8080:8080 hpcl/jenkins:latest
```

Installation complete!

# Creating New Jobs
The following template is provided for creating jobs. 

```
- job:
    name: JOB_NAME 
    project-type: freestyle
    properties:
      - github:
          url: GITHUB_URL 
    defaults: global
    description: 'COOL_DESCRIPTION'
    disabled: false
    display-name: 'NICELY FORMATTED NAME'
    concurrent: true
    quiet-period: 5
    node: docker-slave
    scm:
      - git:
          url: GITHUB_URL
          branches:
            - BRANCE
    builders:
      - shell: |
          # TESTS
          # EXAMPLES:
          python test.py # Runs a pythons script that in turn runs the tests.
          test.sh # runs a shell script that runs the tests.
          make tests # runs a makefile that runs the tests 
```

For a completed job please see: https://github.com/hpcl/continuous-integration/blob/master/jenkins-job-config/jobs/orio-tests.yaml

Save your job in continuous-integration/jenkins-job-config/JOB_NAME.yaml, and
update the jobs_list in continuous0integration/jenkins-job-config/build.py

Then run the build_jobs job in jenkins and your job will automagically appear!

# Creating a new Docker Slave

In the likely case that the provided slave is not sufficient I suggest just
updating the provided slave with whatever is required.

You do this by altering the Dockerfile at continuous-integration/docker-images/jenkins-slave.

The likely lines that you'll want to change are the apt-get install lines to
install your required software. 

If you do in fact want to create a new slave, I suggest using the provided on as a basis.

You'll need to make changes to the Dockerfile, add a new docker template in
jenkins, and make changes to the new slaves build.py.


