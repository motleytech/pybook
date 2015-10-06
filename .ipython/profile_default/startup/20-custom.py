import io
from IPython.nbformat import current
from pprint import pprint as pp
from time import time

def execute_notebook(nbfile, name=None):
    global __name__
    with io.open(nbfile) as f:
        nb = current.read(f, 'json')

    ip = get_ipython()

    if name is None:
        name = ".".join(nbfile.split(".")[:-1])

    old_name = __name__
    __name__ = name

    try:
        for cell in nb.worksheets[0].cells:
            if cell.cell_type != 'code':
                continue
            ip.run_cell(cell.input)
    finally:
        __name__ = old_name

    return

def timeit(func):
    def wrapper(*a, **kw):
        startTime = time()
        try:
            rv = func(*a, **kw)
        except:
            raise
        finally:
            endTime = time()
            print "Time = {etime}".format(etime=(endTime - startTime))
        return rv
    return wrapper



gl = globals()

gl['execute_notebook'] = execute_notebook
gl['pp'] = pp
gl['timeit'] = timeit

