import asyncio

try:
    from socket import socketpair
except ImportError:
    from asyncio.windows_utils import socketpair

rsock, wsock = socketpair()
loop = asyncio.get_event_loop()

class Protocol(asyncio.Protocol):
    transport = None

    def connection_made(self, transport):
        self.transport = transport 

    def data_received(self, data):
        print('received:', data.decode())
        self.transport.close()

    def connection_lost(self, exc):
        loop.stop()

connect_coro = loop.create_connection(Protocol, sock=rsock)

transport, protocol = loop.run_until_complete(connect_coro)

loop.call_soon(wsock.send, 'I am allenwind'.encode())

loop.run_forever()

rsock.close()
wsock.close()
loop.close()