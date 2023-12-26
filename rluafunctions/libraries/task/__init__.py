# based off of the library "task"

import threading
import time

def wait(amnt = 0.01):
    time.sleep(amnt)

def waitms(amnt = 10):
    time.sleep(amnt / 1000)

def spawn(func, daemon = True, args = tuple()):
    x = threading.Thread(target=func,args=args, daemon=daemon)
    x.start()

def delay(func, daemon = True, sleep = 1, args = tuple()):
    x = threading.Thread(target=func, args=args, daemon=daemon)
    time.sleep(sleep)
    x.start()
