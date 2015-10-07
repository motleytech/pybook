from pprint import pprint as pp
from time import time

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
gl['pp'] = pp
gl['timeit'] = timeit
