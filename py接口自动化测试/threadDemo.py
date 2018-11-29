import threading
import time


stime=time.time()
def demo1(m):
    for i in range(1000):
        print(i+m)
    time.sleep(2)

def demo2(m):
    for i in range(2000):
        print(i+m)
    time.sleep(2)

def demo3(m):
    for i in range(500):
        print(i+m)
    time.sleep(2)

# demo1(1)
# demo2(2)
# demo3(3)

t1=threading.Thread(target=demo1,args=(1,))
t2=threading.Thread(target=demo2,args=(2,))
t3=threading.Thread(target=demo3,args=(3,))
t1.start()
t2.start()
t3.start()
t1.join()#等待主线程
t2.join()
t3.join()


etime=time.time()
print(etime-stime)