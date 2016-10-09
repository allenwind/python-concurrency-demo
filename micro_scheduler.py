from collections import deque
from collections import OrderDict

def countdown(n):
    while n > 0:
        n -= 1
        print('T-minus', n)
        yield n

def countup(n):
    x = 0
    while n > x:
        x += 1
        print('T-up', x)
        yield n

class TaskScheduler:
    """加入一些特性：
    1.优先级
    2.else
    """
    def __init__(self):
        self._task_queue = deque()
        self._result = OrderDict()

    def new_task(self, task):
        self._task_queue.append(task)

    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                result = next(task) #do with result
                self._task_queue.append(task)
            except StopIteration:
                pass
            
    def add_result(self, result):
        pass

    def show_result(self):
        pass

if __name__ == '__main__':
    
     sched = TaskScheduler()
     sched.new_task(countdown(10))
     sched.new_task(countdown(5))
     sched.run()
     
