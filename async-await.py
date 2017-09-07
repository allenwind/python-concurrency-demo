import asyncio

async def print_a_c():
    print("A")
    await asyncio.sleep(0)
    print("C")

async def print_b_d():
    print("B")
    await asyncio.sleep(0)
    print("D")

async def main():
    await asyncio.wait([print_b_d(), print_a_c()])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


