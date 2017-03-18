import multiprocessing
import time
import random

def consumer(input_q):
    while True:
        item = input_q.get()
        print(item)
        time.sleep(random.random() * 3)

        #消费者返回信号，表示item已经被处理
        input_q.task_done() #send message notify task done

def producer(sequence, output_q):
    for item in sequence:
        output_q.put(item)

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.daemon = True #创建它的进程终止，该进程也终止
    cons_p.start()

    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p2.daemon = True
    cons_p2.start()

    sequence = [1, 2, 3, 4]
    producer(sequence, q)
    q.join()

