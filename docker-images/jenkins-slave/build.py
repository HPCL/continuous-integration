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
  authorized_user_path = "/root/certs/docker_container/jenkins-slave/authorized_users"
  copyfile(authorized_user_path, "config/authorized_users")
  

def build_container(args):
  subprocess.call("docker build -t jenkins-slave:{vrsn} .".format(vrsn=args.version), shell=True)


def main():
  args = arg_parse()
  setup_credentials()
  build_container(args)


if __name__ == "__main__":
  main()
  

