#!/usr/bin/env python
import argparse
import os
import subprocess
import sys
from shutil import copyfile

def arg_parse():
  parser = argparse.ArgumentParser()
  parser.add_argument('-v', '--version', dest='version', default='latest')
  return parser.parse_args()

def setup_credentials():
  credential_config = os.path.abspath("config/credentials.xml")
  cert_paths = {"{{ docker_client_cert }}": os.path.abspath("/root/certs/docker/cert.pem"),
                "{{ docker_client_key }}": os.path.abspath("/root/certs/docker/key.pem"),
                "{{ docker_server_cert }}": os.path.abspath("/root/certs/docker/ca.pem"),
                "{{ jenkins_slave_ssh }}": os.path.abspath("/root/certs/docker_container/jenkins-slave/id_rsa"),
  }
  
  print "Setting up credentials"
  with open(credential_config, "r") as file_in:
    with open("tmp.xml", "w") as file_out:
      for line in file_in:
        for match, path in cert_paths.iteritems():
          if match in line:
            cert_value = ""
            with open(path, "r") as cert:
              cert_value = cert.read()
            line = line.replace(match, cert_value) 
        file_out.write(line)
  copyfile("tmp.xml", credential_config)
  os.remove("tmp.xml")

def build_container(args):
  subprocess.call("docker build -t hpcl/jenkins:{vrsn} .".format(vrsn=args.version), shell=True)

def main():
  args = arg_parse()
  setup_credentials()
  build_container(args)


if __name__ == "__main__":
  main()
  

