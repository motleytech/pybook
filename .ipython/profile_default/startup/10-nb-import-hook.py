import os
import imp
import sys
import io
from IPython.nbformat import current
from traceback import print_exc

def import_notebook(nbname, loader=None):
    fullpath = "{}/{}.ipynb".format(os.getcwd(), nbname)

    if not os.path.exists(fullpath):
        raise Exception("Failed to find ipython notebook: {}.ipynb".format(nbname))

    if nbname in sys.modules:
        mod = sys.modules[nbname]
        return mod

    moduleName = nbname
    nbFilename = nbname + ".ipynb"

    print "Importing ipynb file : {}".format(nbFilename)

    with io.open(nbFilename) as f:
        nb = current.read(f, 'json')

    newModule = imp.new_module(moduleName)

    try:
        for cell in nb.worksheets[0].cells:
            if cell.cell_type != 'code':
                continue
            exec cell.input in newModule.__dict__
    except:
        print "Error in importing ipython notebook."
        print_exc()
        raise

    # Set a few properties required by PEP 302
    newModule.__file__ = nbname
    newModule.__name__ = nbname
    newModule.__path__ = [ nbname ]
    newModule.__loader__ = loader
    newModule.__package__ = '' # no package

    sys.modules[moduleName] = newModule
    return newModule


class IpynbImportFinder(object):
    def __init__(self):
        return

    def find_module(self, modname, path=None):
        modpath = "{}/{}.ipynb".format(os.getcwd(), modname)
        if os.path.exists(modpath):
            return IpynbImportLoader()
        return None


class IpynbImportLoader(object):
    def __init__(self):
        return

    def load_module(self, modname):
        return import_notebook(modname, self)


# Install our custom importer
sys.meta_path.append(IpynbImportFinder())
