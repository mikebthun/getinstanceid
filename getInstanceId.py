#!/usr/bin/python -tt

import sys,getopt
import commands 
import logging
import json

logger = logging.getLogger('stencil')
hdlr = logging.StreamHandler(sys.stdout)
#hdlr = logging.FileHandler('stencil.log') 
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO) #logging.DEBUG


def help():

  print " Usage: getInstanceId.py > instance.json [--help] "



def Run(cmd):
 
  logger.debug("** Running: %s" % cmd)

  (status,output) = commands.getstatusoutput(cmd)

  if status > 0:
    logger.error(output)
    sys.exit(2)
 
  logger.debug('[OK]')
  return output



def main(argv):

  # make sure command line arguments are valid
  try:
    options, args = getopt.getopt(

       argv, 
      'hv', 
      [ 
        'help',
        'verbose' 
    
      ])
 
  except getopt.GetoptError:
    logging.fatal("Bad options!")
    help()
    sys.exit(2)


  # handle command line arugments
  for opt, arg in options:
    if opt in ('-h', '--help'):
      help()
      sys.exit(2)
    elif opt in ('-v', '--verbose'):
      logger.setLevel(logging.DEBUG) 
 

  ###################################
  # main code starts here
  ###################################

  cmd = "wget --timeout 3 --tries 1 -q -O - http://169.254.169.254/latest/meta-data/instance-id"
  instance_id = Run(cmd) 

  j = {

    "instanceId":instance_id

  }

  print json.dumps(j)


if __name__ == "__main__":
  main(sys.argv[1:])
 

 


