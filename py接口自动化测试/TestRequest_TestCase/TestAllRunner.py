import threading
from testAllCase import *


def thread():
    threads=[]
    threads.append(threading.Thread(target=TestCase_Case1))
    threads.append(threading.Thread(target=TestCase_Case2))
    for t in threads:
        t.start()
    t.join()
