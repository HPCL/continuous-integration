#!/usr/bin/env python

import os
import sys
import subprocess

subprocess.call("java -Djenkins.install.runSetupWizard=false -jar /usr/share/jenkins/jenkins.war", shell=True)
