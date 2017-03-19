import threading
import time
import random

class LifoQueue:

    def __init__(self):
        self._list = []
        self._lock = threading.Lock()

    def put(self, item):
        self._lock.acquire()
        self._list.append(item)
        self._lock.release()

    def get(self):
        self._lock.acquire()
        item = self._list.pop()
        self._lock.release()
        return item

class Consumer(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue
        #self.daemon = True

    def run(self):
        while True:
            item = random.randint(1, 100)
            self._queue.put(item)
            print("put item {}".format(item))
            time.sleep(random.random() * 2)

class Producer(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue
        #self.daemon = True #当非后台线程退出后，解析器自动退出，不管后台线程

    def run(self):
        while True:
            time.sleep(random.random() * 2)
            item = self._queue.get()
            print("get item {}".format(item))

if __name__ == '__main__':
    q = LifoQueue()
    c1 = Consumer(q)
    c2 = Consumer(q)

    p1 = Producer(q)
    p2 = Producer(q)

    c1.start()
    c2.start()
    p1.start()
    p2.start()





