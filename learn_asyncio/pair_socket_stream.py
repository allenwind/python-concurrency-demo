import asyncio

try:
    from socket import socketpair
except ImportError:
    from asyncio.windows_utils import socketpair

async def wait_for_data(loop):

    rsock, wsock = socketpair()
    reader, writer = await asyncio.open_connection(sock=rsock, loop=loop)
    loop.call_soon(wsock.send, 'I am allenwind'.encode()) # simulate the reception of data from the network
    
    data = await reader.read(100)

    print('received:', data.decode())
    writer.close()

    wsock.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(wait_for_data(loop))
loop.close()