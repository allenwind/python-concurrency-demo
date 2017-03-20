import time
import random

from multiprocessing.connection import Client

conn = Client(('localhost', 15000), authkey=b'key')

conn.send((3, 4))
r = conn.recv()

print(r)

conn.send(('hello', 'world'))
r = conn.recv()

print(r)
conn.close()