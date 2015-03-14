import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

command = "cd %s; git pull" % PARENT_DIR
print "Running command :\n%s\n" % command
os.system(command)
