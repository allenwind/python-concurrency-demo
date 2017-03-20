import multiprocessing
import time

#托管对象

def watch(d, evt):
    while True:
        evt.wait()
        print(d)
        evt.clear()

if __name__ == '__main__':
    m = multiprocessing.Manager()
    d = m.dict()
    evt = m.Event()

    p = multiprocessing.Process(target=watch, args=(d, evt))
    p.daemon=True
    p.start()

    d['foo'] = 42
    evt.set()
    time.sleep(3)

    d['bar'] = 37
    evt.set()
    time.sleep(3)

    p.terminate()
    m.shutdown()