# server
from time import sleep
import rpyc
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):
    # 以exposed_开头的方法才能被客户端调用
    def exposed_greet(self, name):
        sleep(2)
        return "Hello, {}!".format(name)
    
    def exposed_bye(self, name):
        sleep(2)
        return "Bye, {}!".format(name)

if __name__ == "__main__":
    t = ThreadedServer(MyService, port=18861)
    t.start()