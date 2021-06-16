from threading import Semaphore, Thread
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def read_line(fptr):
    global count, mutex, barrier, sno
    data = fptr.read(64)
    while data:
        mutex.acquire()
        count += 1
        sno += 1
        logging.info(data)
        data = fptr.read(64)
        if count == 2:
            barrier.release()
            barrier2.acquire()
        mutex.release()

        barrier.acquire()
        barrier.release()

        mutex.acquire()
        count -= 1
        if count == 0:
            barrier.acquire()
            barrier2.release()
        mutex.release()

        barrier2.acquire()
        barrier2.release()

        
    
    

mutex = Semaphore(1)  #mutex for controlled access to 'count'
barrier = Semaphore(0)  #barrier for phase 1
barrier2 = Semaphore(1)  #barrier for phase 2 i.e. to prevent a thread from getting ahead of other threads through iteration
count = 0
sno = 0
fptr1 = open('temp_file.txt', 'r', )
fptr2 = open('temp_file.txt', 'r')
t1 = Thread(name= 'thread A', target=read_line, args=(fptr1,))
t2 = Thread(name='thread B', target=read_line, args=(fptr2,))
t1.start()
t2.start()

