import threading
import logging
import random
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def f():
    r = random.randint(1,12)
    t = threading.currentThread()
    logging.debug(f'sleeing {r} seconds')
    time.sleep(r)
    logging.debug('ending')
    return

main_thread = threading.currentThread()
logging.debug('main thread starting')
for i in range(3):
    t = threading.Thread(target=f)
    t.setDaemon(True)   
    t.start()

for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug(f'joining: {t.getName()}')
    t.join()

