#!/usr/bin/python -tt

import sys
import boto.utils
import json
 
class AwsInstanceDetails(object):

  def __init__(self):

    try:
      self.instance = boto.utils.get_instance_metadata() 
    except Exception as e:
      print "FATAL: Could not grab instance information from boto"
      sys.exit(2)
 

  def getPublicHost(self):

    return self.instance['public-hostname']
 
  def getInstanceId(self):

    return self.instance['instance-id']


def main(argv):

  ###########################################
  # some test code, never runs when included
  # This must be run from an AWS box
  ###########################################
  
  k = AwsInstanceDetails()
  
  j = {

    "public-host": k.getPublicHost(),
    "instance-id": k.getInstanceId()
  }

  print json.dumps(j)


if __name__ == "__main__":
  main(sys.argv[1:])