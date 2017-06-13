import asyncio
import time

class EchoClientProtocol:
    def __init__(self, message, loop):
        self.message = time.ctime()
        self.loop = loop
        self.transport = None 

    def connection_made(self, transport):
        self.transport = transport 
        print('send: ', self.message)

        for _ in range(10):
            time.sleep(1)
            self.transport.sendto(self.message.encode())

    def datagram_received(self, data, addr):
        print('received:', data.decode())
        print('close the socket')
        self.transport.close()

    def error_received(self, exc):
        print('error received:', exc)

    def connection_lost(self, exc):
        print('socket closed, stop the event loop')
        loop = asyncio.get_event_loop()
        loop.stop()

loop = asyncio.get_event_loop()
message = "I am allenwind"

connect = loop.create_datagram_endpoint(
    lambda: EchoClientProtocol(message, loop),
    remote_addr=('localhost', 8080))

transport, protocol = loop.run_until_complete(connect)

loop.run_forever()

transport.close()
loop.close()