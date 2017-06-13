import asyncio

class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport 

    def data_received(self, data):
        message = data.decode()
        print("data received: {!r}".format(message))

        print("send: {!r}".format(message))
        self.transport.write(data)

        print("close the client socket")
        self.transport.close()

loop = asyncio.get_event_loop()

coro = loop.create_server(EchoServerClientProtocol, 'localhost', 8080)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

