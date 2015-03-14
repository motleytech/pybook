import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(THIS_DIR)

convert_cmd = "ipython nbconvert --profile=pybook ../books/*.ipynb"
command = "cd %s; source env.sh; cd export; %s" % (ROOT_DIR, convert_cmd)
print "Running command :\n%s\n" % command
os.system(command)
