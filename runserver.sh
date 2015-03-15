#!//bin/bash

SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

cd $SCRIPTPATH
source ./env.sh
ipython notebook --profile=pybook
