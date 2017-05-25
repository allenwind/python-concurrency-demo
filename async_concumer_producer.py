import asyncio
import random
import string

async def producerA(queue):
    s = string.ascii_letters
    while True:
        item = random.choice(s)
        print('producerA - {}'.format(item))
        await queue.put(item)
        await asyncio.sleep(random.random())

async def producerB(queue):
    s = string.ascii_letters
    while True:
        item = random.choice(s)
        print('producerB - {}'.format(item))
        await queue.put(item)
        await asyncio.sleep(random.random() * 2)

async def consumer(queue):
    while True:
        item = await queue.get()
        print('consumer - {}'.format(item))
        queue.task_done()

        await asyncio.sleep(random.random())


async def main():
    queue = asyncio.Queue()

    await asyncio.wait([producerA(queue), consumer(queue), producerB(queue)])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())



        
