import asyncio

async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('localhost', 8080, loop=loop)

    print('send: %r' % message)
    writer.write(message.encode())

    data = await reader.read(100)
    print('received: %r' % data.decode())

    print('close the socket')
    writer.close()

message = 'I am allenwind'

loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()