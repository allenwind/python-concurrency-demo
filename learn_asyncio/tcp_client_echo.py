import asyncio
import time

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = time.ctime()
        self.loop = loop 

    def connection_made(self, transport):
        while True:
            time.sleep(1)
            transport.write(self.message.encode())
        print("data send: {!r}".format(self.message))

    def data_received(self, data):
        print("data received: {!r}".format(data.decode()))

    def connection_lost(self, exc):
        print("the server closed the connection")
        print("stop the event loop")
        self.loop.stop()

loop = asyncio.get_event_loop()
message = "I am allenwind"

coro = loop.create_connection(lambda: EchoClientProtocol(message, loop),
    'localhost', 8080)

loop.run_until_complete(coro)

loop.run_forever()
loop.close()