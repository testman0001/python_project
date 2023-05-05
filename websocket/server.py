# 基于官方示例
# https://github.com/crossbario/autobahn-python
try:
      import asyncio
except ImportError:
      ## Trollius >= 0.3 was renamed
      import trollius as asyncio
from autobahn.asyncio.websocket import WebSocketServerProtocol,WebSocketServerFactory

class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {} bytes".format(len(payload)))
        else:
            print("Text message received: {}".format(payload.decode('utf8')))

        ## echo back message verbatim
        self.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))

class Server(object):
    def __init__(self, ip='127.0.0.1' , port=58000) -> None:
        self.factory = WebSocketServerFactory()
        self.factory.protocol = MyServerProtocol
        # 创建event loop
        self.event_loop = asyncio.get_event_loop()
        # 创建监听服务（协程对象，实际未执行）
        self.coro = self.event_loop.create_server(self.factory, ip, port)

    def run(self):
        try:
            # 驱动执行协程，让监听服务就绪（实际未正式启动），返回值可以用来停止监听服务
            # python 3.7 之后，run_until_complete 可以用 asyncio.run 代替
            self.server = self.event_loop.run_until_complete(asyncio.ensure_future(self.coro))
            # 真正开始监听服务
            self.event_loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self.server.close()
            self.event_loop.close()

if __name__ == '__main__':
    ser = Server()
    ser.run()