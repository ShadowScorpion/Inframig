#!/usr/bin/env python3

import os,sys
from __args__ import mainVars
 
def _arguments_parser(arguments):
  try:
    _function_name=mainVars['actions_list'][arguments[0]]
  except:
    print("E! Not supported action. Try to use help.")
    sys.exit(1)
  return _function_name


def checkCredentials(function):

  print("Inframig v%s" % mainVars['inframig_version'])

  try:
    AWS_KEY = os.environ['aws_access_key_id']
    AWS_SECRET = os.environ['aws_secret_access_key']
  except:
    print("E! AWS credeitals weren't specified.\n")
    print("E! Please be sure that \"aws_access_key_id\" and \"aws_secret_access_key\" variables were exported.")
    sys.exit(1)

  def arguments_reader():
    if len(sys.argv) == 1:
      print("I! No actions were specified. Closed.")
      sys.exit(0)
    else:
      function_id=_arguments_parser(sys.argv[1::])
      return getattr(function(AWS_KEY, AWS_SECRET, sys.argv[1::]), mainVars['functions_list'][function_id])()

  return arguments_reader()


@checkCredentials
class StartUp(object):
  
  def __init__(self, AWS_KEY, AWS_SECRET, command_line):
    self.AWS_KEY = AWS_KEY
    self.AWS_SECRET = AWS_SECRET
    self.command_line = command_line
    self.system = os.uname()

  def printVersion(self):
    print("Version: %s\nRelease date: %s\nWebsite: inframig.com" %
          (mainVars['inframig_version'],
          mainVars['inframig_release_date']))
    sys.exit(0)

  def printHelp(self):
    from __help__ import HelpMessage
    helpClass = HelpMessage()
    helpClass.printMessage()
    sys.exit(0)

