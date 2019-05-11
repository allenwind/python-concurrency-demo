import concurrent.futures

def cpu_bound_task(size=1000000):
    for _ in range(size):
        pass

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        tasks = {executor.submit(cpu_bound_task): _id for _id in range(4)}
        