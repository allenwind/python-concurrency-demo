import multiprocessing
import time

def adder(pipe):
    server_p, client_p = pipe
    client_p.close()

    while True:
        try:
            x, y = server_p.recv()
        except EOFError:
            break
        result = x + y
        server_p.send(result)
    print('server done')

if __name__ == '__main__':
    server_p, client_p = multiprocessing.Pipe()

    adder_p = multiprocessing.Process(target=adder, args=((server_p, client_p),))
    adder_p.start()

    server_p.close()

    client_p.send((3, 4))
    print(client_p.recv())

    client_p.send(('hello', 'world'))
    print(client_p.recv())

    client_p.close()

    adder_p.join()

