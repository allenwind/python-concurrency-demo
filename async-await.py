import asyncio

async def printer():
    print("A")
    await asyncio.sleep(0)
    print("C")

async def printer2():
    print("B")
    await asyncio.sleep(0)
    print("D")

async def main():
    await asyncio.wait([printer2(), printer()])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


