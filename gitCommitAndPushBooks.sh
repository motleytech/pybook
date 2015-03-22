#!/bin/bash

if [ "$1" == "" ]; then
    echo "Error : You need to provide a commit message"
    exit
fi

if [ "$2" != "" ]; then
    echo "Error : Provide only 1 argument. Put the commit message in quotes if it contains spaces."
    exit
fi

git add books
git add export
echo 'git commit -m"'$1'"'
# git commit -m'"'$1'"'
# git push origin master

