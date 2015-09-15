import io
from IPython.nbformat import current
from pprint import pprint as pp

def execute_notebook(nbfile):
    
    with io.open(nbfile) as f:
        nb = current.read(f, 'json')
    
    ip = get_ipython()
    
    for cell in nb.worksheets[0].cells:
        if cell.cell_type != 'code':
            continue
        ip.run_cell(cell.input)
    return

gl = globals()

gl['execute_notebook'] = execute_notebook
gl['pp'] = pp
