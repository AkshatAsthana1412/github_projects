from threading import Thread
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(threadName)s :: %(message)s')
class MyThread(Thread):
    def __init__(self, name=None, args=(), kwargs=None):
        super().__init__(name = name)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug(f'running with args: {self.args}, kwargs: {self.kwargs}')
        logging.debug('sleeping for 4 sec')
        time.sleep(4)
        logging.debug('ending...')
        return
if __name__=='__main__':
    t1 = MyThread('mythread', (1,3), {'a': 1, 'b': 90})
    t1.start()