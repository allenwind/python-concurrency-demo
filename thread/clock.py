import threading
import time

def clock(interval):
    while True:
        print('the clock1 time is %s' % time.ctime())
        time.sleep(interval)

class ClockThread(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        #self.daemon = True
        self.interval = interval

    def run(self):
        while True:
            print('the clock2 time is %s' % time.ctime())
            time.sleep(self.interval)

if __name__ == '__main__':
    t1 = threading.Thread(target=clock, args=(3,))
    #t1.daemon = True
    t2 = ClockThread(5)

    t1.start()
    t2.start()