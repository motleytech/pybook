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

# upgrade pip
os.system("/bin/bash -c 'cd %s; source %s; pip install -U pip'" % (ROOT_DIR, "env.sh"))

# install pip dependencies
os.system("/bin/bash -c 'cd %s; source %s; pip install ipython[notebook]'" %
          (ROOT_DIR, "env.sh"))

# install mathjax
os.system("/bin/bash -c 'cd %s; source %s; python -m IPython.external.mathjax'" %
          (ROOT_DIR, "env.sh"))

# install pandoc to export to pdf
os.system("sudo apt-get -y install pandoc")

# dependencies for scipy
os.system("sudo apt-get -y install libamd2.2.0 libblas3gf libc6 libgcc1\
 libgfortran3 liblapack3gf libumfpack5.4.0 libstdc++6\
 build-essential gfortran libatlas-base-dev python-all-dev")

os.system("/bin/bash -c 'cd %s; source %s; pip install scipy'" %
          (ROOT_DIR, "env.sh"))


# upgrade distribute
os.system("/bin/bash -c 'cd %s; source %s; pip install distribute --upgrade'" %
          (ROOT_DIR, "env.sh"))

# install matplotlib
os.system("sudo apt-get -y install libfreetype6-dev libpng12-dev")
os.system("/bin/bash -c 'cd %s; source %s; pip install matplotlib'" %
          (ROOT_DIR, "env.sh"))

