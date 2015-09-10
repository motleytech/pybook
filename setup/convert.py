import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(THIS_DIR)

convert_cmd = "jupyter nbconvert --template full ../../books/*.ipynb"
command = "/bin/bash -c 'cd %s; source env.sh; cd export/full; %s'" % (ROOT_DIR, convert_cmd)
print "Running command :\n%s\n" % command
os.system(command)

convert_cmd = "jupyter nbconvert --template basic ../../books/*.ipynb"
command = "/bin/bash -c 'cd %s; source env.sh; cd export/basic; %s'" % (ROOT_DIR, convert_cmd)
print "Running command :\n%s\n" % command
os.system(command)
