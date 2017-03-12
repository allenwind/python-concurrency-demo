from multiprocessing import Process, Lock

err_file = r'E:\github\concurrent\error1.log'

err_fd = open(err_file, 'w')

def put(fd):
    print('put')
    fd.write("put func write")
    print('end')

