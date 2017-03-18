import multiprocessing
import time

def consumer(input_q):
    while True:
        item = input_q.get()

        if item is None: #设置哨兵 sentinel
            break
        print(item)
        time.sleep(1)
    print('comsumer done')

def producer(sequence, output_q):
    for item in sequence:
        output_q.put(item)

if __name__ == '__main__':
    q = multiprocessing.Queue()
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.start()

    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    q.put(None) #设置哨兵 sentinel
    cons_p.join()