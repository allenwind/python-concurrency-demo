import threading
import time

class Timer:
    def __init__(self, interval, n_loop):
        self._interval = interval
        self._n = n_loop
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        thread = threading.Thread(target=self.run)
        thread.daemon = True
        thread.start()

    def run(self):
        
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                
                self._cv.notify_all()

    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()


def countdown(nticks):
    while nticks > 0:
        timer.wait_for_tick()
        print("T-minus", nticks)
        nticks -= 1

def countup(last):
    n = 0
    while n < last:
        timer.wait_for_tick()
        print("counter", n)
        n += 1

if __name__ == '__main__':
    timer = Timer(2, 5)
    timer.start()
    threading.Thread(target=countdown, args=(5,)).start()
    threading.Thread(target=countup, args=(5,)).start()























                
            
    
