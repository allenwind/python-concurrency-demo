import random
import time

def consumer():
    r = None
    while True:
        data = yield r
        print("consuming: {}".format(data))
        time.sleep(random.random())
        r = data + 1

def producer(consumer):
    n = 5
    consumer.send(None)
    while n:
        data = random.choice(range(100))
        print("prducing: {}".format(data))
        rs = consumer.send(data)
        print("consumer return:{}".format(rs))
        n -= 1
    consumer.close()

if __name__ == '__main__':
    c = consumer()
    producer(c)

