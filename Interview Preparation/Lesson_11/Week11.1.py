from threading import Lock, Thread

lock1 = Lock()
lock2 = Lock()
lock1.acquire()

def f():
    print(0)
    lock1.acquire()
    print(1)

def g():
    print(0)
    lock1.release()
    print(1)


t1 = Thread(target=f)
t2 = Thread(target=g)
t1.start()
t2.start()