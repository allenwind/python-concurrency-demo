import asyncio

class EchoServerProtocol:
    def connection_made(self, transport):
        self.transport = transport 

    def datagram_received(self, data, addr):
        message = data.decode()
        print('received %r from %r' % (message, addr))
        print('send %r to %s' % (message, addr))
        self.transport.sendto(data, addr)

loop = asyncio.get_event_loop()
print('starting udp server')

listen = loop.create_datagram_endpoint(
    EchoServerProtocol, local_addr=('localhost', 8080))

transport, protocol = loop.run_until_complete(listen)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

transport.close()
loop.close()

