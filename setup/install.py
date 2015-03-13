import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(THIS_DIR)

# check if venv folder exists
VENV_NAME = "venv"
VENV_FOLDER = os.path.join(ROOT_DIR, VENV_NAME)

if not os.path.isdir(VENV_FOLDER):
    # if not, create new venv
    os.system("rm -rf %s" % VENV_FOLDER)
    os.system("cd %s; virtualenv %s" % (ROOT_DIR, VENV_NAME))
else:
    answer = raw_input("%s exists. Delete and recreate? (y/n)" % VENV_FOLDER)
    if answer.strip() == 'y':
        os.rmdir(VENV_FOLDER)
        os.system("cd %s; virtualenv %s" % (ROOT_DIR, VENV_NAME))

# install pip dependencies
os.system("/bin/bash -c 'source %s/%s; pip install ipython[notebook]'" %
          (VENV_FOLDER, "bin/activate"))

# install mathjax
os.system("/bin/bash -c 'source %s/%s; python -m IPython.external.mathjax'" %
          (VENV_FOLDER, "bin/activate"))

# install pandoc to export to pdf
os.system("sudo apt-get -y install pandoc")



#
# create