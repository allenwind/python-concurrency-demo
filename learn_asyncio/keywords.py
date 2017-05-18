import asyncio

@asyncio.coroutine
def slow_operation(n):
    yield from asyncio.sleep(1)
    print("slow operation {} complete".format(n))

@asyncio.coroutine
def main():
    yield from asyncio.wait([
        slow_operation(1),
        slow_operation(2),
        slow_operation(3),
        slow_operation(4),
        slow_operation(5)
        ])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# new syntax
print("new syntax\n")

async def slow_operation(n):
    await asyncio.sleep(1)
    print("slow operation {} complete".format(n))

async def main():
    await asyncio.wait([
    slow_operation(1),
    slow_operation(2),
    slow_operation(3),
    slow_operation(4),
    slow_operation(5)
    ])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

#对比，async化简了asyncio.coroutine，await的使用化简了yield from