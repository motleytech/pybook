import subprocess
import sys

def runCommandAndGetOuput(command):
    import subprocess

    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (stdoutdata, stderrdata) = proc.communicate()
    return stdoutdata

try:
    builtins = sys.modules['__builtins__'].__dict__
except KeyError:
    builtins = sys.modules['builtins'].__dict__

builtins['runCommand'] = runCommandAndGetOutput
del runCommandAndGetOuput

