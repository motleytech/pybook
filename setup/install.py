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

# install pandoc to export to pdf
os.system("sudo apt-get -y install pandoc")

os.system("/bin/bash -c 'cd %s; git clone https://github.com/ipython-contrib/IPython-notebook-extensions.git'" % (ROOT_DIR))

# dependencies for scipy
os.system("sudo apt-get -y install libamd2.2.0 libblas3gf libc6 libgcc1\
 libgfortran3 liblapack3gf libumfpack5.4.0 libstdc++6\
 build-essential gfortran libatlas-base-dev python-all-dev")

# dependencies for matlab
os.system("sudo apt-get -y install libfreetype6-dev libpng12-dev")


# upgrade pip
os.system("/bin/bash -c 'cd %s; source %s; pip install -U pip'" % (ROOT_DIR, "env.sh"))

# upgrade distribute
os.system("/bin/bash -c 'cd %s; source %s; pip install distribute --upgrade'" %
          (ROOT_DIR, "env.sh"))

os.system("/bin/bash -c 'cd %s; source %s; pip install -r %s/setup/requirements.txt'" %
          (ROOT_DIR, "env.sh", ROOT_DIR))
