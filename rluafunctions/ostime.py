# based off of the library "os"

import time

def tick():
    return time.time()

def difftime(t_0,t_1):
    return t_0 - t_1

def date(format = "%a %b %d %H:%M:%S %Y"):
    return time.strftime(format)

def clock():
    return time.perf_counter()
