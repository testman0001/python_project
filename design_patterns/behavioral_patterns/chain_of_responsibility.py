# 责任链模式
# 为请求创建一个接收对象的链，每个接收者包含对另一个接受者的引用，如果不能处理则传给下一个接受者

from pypattyrn.behavioral.chain import Chain, ChainLink


class ConcreteChainLinkTwo(ChainLink): 

    def handle(self, request):
        if request == 'handle_two':
            print("Handled in chain link two")
        else:
            # 无“接班人”时触发异常并被捕获，触发chain的fail方法
            return self.successor_handle(request)


class ConcreteChainLinkOne(ChainLink): 

    def __init__(self): 
        super().__init__()
        # 设置接班人
        self.set_successor(ConcreteChainLinkTwo()) 

    def handle(self, request): 
        if request == 'handle_one':
            print("Handled in chain link one")
            # 这里也可以继续交给下一个，实现多次处理的逻辑
            # return self.successor_handle(request)
        else:
            # 处理不了给下一个“接班人”
            return self.successor_handle(request)

class ConcreteChain(Chain): 

    def __init__(self): 
        # 用chain link实例进行初始化
        super().__init__(ConcreteChainLinkOne()) 

    # 无chain link可以处理请求时, 调用fail方法
    def fail(self):
        print('Fail')


chain = ConcreteChain()

chain.handle("handle_one")
chain.handle("handle_two")
chain.handle('handle_four')