try:
      import asyncio
except ImportError:
      ## Trollius >= 0.3 was renamed
      import trollius as asyncio
from autobahn.asyncio.websocket import WebSocketClientProtocol, WebSocketClientFactory
import time


class MyClientProtocol(WebSocketClientProtocol):
   def onOpen(self):
      self.sendMessage(u"Hello, world!".encode('utf8'))

   def onMessage(self, payload, isBinary):
      if isBinary:
         print("Binary message received: {0} bytes".format(len(payload)))
      else:
         print("Text message received: {0}".format(payload.decode('utf8')))

class Client(object):
    def __init__(self, ip = '127.0.0.1', port = 58000) -> None:
        self.factory = WebSocketClientFactory()
        self.factory.protocol = MyClientProtocol
        self.event_loop = asyncio.get_event_loop()
        # 协程，建立与服务器的连接
        self.coro = self.event_loop.create_connection(self.factory, ip, port)

    def run(self):
        try:
            # 驱动协程，等待连接就绪
            self.event_loop.run_until_complete(asyncio.ensure_future(self.coro))
            # 停顿2s，可以看到服务端接收到连接
            time.sleep(2)
            # 正式启动客户端服务，可以看到服务端收到客户端消息，客户端收到服务端消息
            self.event_loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self.event_loop.close()

if __name__ == '__main__':
    cli = Client()
    cli.run()