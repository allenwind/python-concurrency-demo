import time
import random

from collections import deque

def foo():
    while True:
        item = random.randint(1, 100)
        time.sleep(1)
        print('foo item: {}'.format(item))
        yield

def bar():
    while True:
        item = random.randint(1, 100)
        time.sleep(1)
        print('bar item: {}'.format(item))
        yield


tasks = deque()
tasks.append(foo())
tasks.append(bar())
tasks.append(foo())
tasks.append(bar())

while tasks:
    task = tasks.pop()
    try:
        next(task)
        tasks.appendleft(task)
    except StopIteration:
        pass
