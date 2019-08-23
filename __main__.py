#!/usr/bin/env python3

import os,sys
import re

from __args__ import mainVars


def _arguments_parser(arguments):
  try:
    _function_name=mainVars['actions_list'][arguments[0]]
  except:
    print("E! Not supported action. Try to use help.")
    sys.exit(1)
  return _function_name


def checkFunc(function):

  print("Inframig v%s" % mainVars['inframig_version'])

  def wrappers():

    def checkCredsWrapper():
      try:
        AWS_KEY = os.environ['aws_access_key_id']
        AWS_SECRET = os.environ['aws_secret_access_key']
      except:
        print("E! AWS credeitals weren't specified.\n")
        print("E! Please be sure that \"aws_access_key_id\" and \"aws_secret_access_key\" variables were exported.")
        sys.exit(1)
      return AWS_KEY, AWS_SECRET


    def argumentsWrapper():
      if len(sys.argv) == 1:
        print("I! No actions were specified. Closed.")
        sys.exit(0)
      else:
        function_id=_arguments_parser(sys.argv[1::])
        return function_id


    def terraformCheckWrapper(system):
      if "Linux" in system:
        try:
          terraformVersion = os.popen('terraform --version').read()
          if re.compile(r"[A-z]\s+v\d+.\d+.\d+").search(terraformVersion) != None:
            return re.sub(r"[A-z\s+]", "", terraformVersion)
          else:
            raise Exception()
#            print("E! Terraform not found. Please install it before starting an agent.")
#            sys.exit(1)
        except:
          print("E! Terraform not found. Please install it before starting an agent.")
          sys.exit(1)
      else:
        print("E! Unfortunately Inframig agent is not supporting your OS yet.")
        print("E! We will working on it! Exit.")
        sys.exit(1)


    def executorWrapper():
      system = os.uname()
      AWS_KEY, AWS_SECRET = checkCredsWrapper()
      function_id = argumentsWrapper()
      terraformVersion = terraformCheckWrapper(system)
      return getattr(function(system, AWS_KEY, AWS_SECRET, terraformVersion, sys.argv[1::]), mainVars['functions_list'][function_id])()

    return executorWrapper()

  return wrappers()

@checkFunc
class StartUp(object):
 
  def __init__(self, system, AWS_KEY, AWS_SECRET, terraformVersion, command_line):
    self.AWS_KEY = AWS_KEY
    self.AWS_SECRET = AWS_SECRET
    self.command_line = command_line
    self.terraformVersion = terraformVersion


  def printVersion(self):
    print("Version: %s\nRelease date: %s\nWebsite: inframig.com\nTerraform: %s" %
          (mainVars['inframig_version'],
          mainVars['inframig_release_date'],
          self.terraformVersion))
    sys.exit(0)


  def printHelp(self):
    from __help__ import HelpMessage
    helpClass = HelpMessage()
    helpClass.printMessage()
    sys.exit(0)

