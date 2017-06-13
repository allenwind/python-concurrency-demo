import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print('received %r from %r' % (message, addr))

    print('send: %r' % message)
    writer.write(data) # non-blocking metho

    await writer.drain()

    print('close the client socket')
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, 'localhost', 8080, loop=loop)
server = loop.run_until_complete(coro)

print('serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()