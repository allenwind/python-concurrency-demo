import threading
import time
import random

from collections import deque

class List(object):

	def __init__(self, size=10):
        #with capacity, set two lock to exchange status of list
		self._size = size
		self._lock = threading.RLock()
		self._not_empty = threading.Condition() #分别代表list的状态
		self._not_full = threading.Condition()
		self._list = deque()

	def write(self, value):
		with self._lock:
			while self._list.size() == self._size:
				self._not_full.wait()
			self._list.append(value)
			self._not_empty.notify_all()

	def read(self):
		with self._lock:
			while self.is_empty():
				self._not_empty.wait()
			value = self._list.popleft()
			self._not_full.notify_all()
		return value

	def is_empty(self):
		with self._lock:
			return self.size() == 0

	def size(self):
		with self._lock:
			return len(self._list)

class Queue(object):

    def __init__(self, size):
        self._size = size
        self._list = deque()
        self._lock = threading.RLock()
        self._status = threading.Condition() #use condition lock to change queue' status

    def write(self, value):
        with self._lock:
            if self.size() < self._size:
                self._list.append(value)
                self._status.notify_all()
                return
            else:
                self._status.wait()
                self.write(value)

    def read(self):
        with self._lock:
            if self.size() > 0:
                value = self._list.popleft()
                self._status.notify_all()
                return value 
            else:
                self._status.wait()
                self.read()

    def size(self):
        with self._lock:
            return len(self._list)

class Consumer(threading.Thread):
    
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
            delay = random.random()
            time.sleep(delay)
            value = random.randint(1, 100)
            self.queue.write(value)

class Producer(threading.Thread):
    
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
            delay = random.random()
            time.sleep(delay)
            value = self.queue.read()

if __name__ == '__main__':
	queue = List()
    producer = Producer(queue)
    consumer = Consumer(queue)

    producer.start()
    consumer.start()