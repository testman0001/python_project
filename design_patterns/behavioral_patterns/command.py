# 命令模式
# 请求以命令的形式包裹到对象中，传给调用对象，调用对象寻找可以处理该命令的合适的对象，并把该命令传给相应的对象，该对象执行命令
from pypattyrn.behavioral.command import Receiver, Command, Invoker


# 命令接受者，包含命令对应的方法
class Thermostat(Receiver): 

    def raise_temp(self, amount):
        print("Temperature raised by {0} degrees".format(amount))
        return "Temperature raised by {0} degrees".format(amount)

    def lower_temp(self, amount):
        print("Temperature lowered by {0} degrees".format(amount))
        return "Temperature lowered by {0} degrees".format(amount)

# “命令”对象
class RaiseTempCommand(Command):

    # 重写init以携带amount参数
    def __init__(self, receiver, amount=5):
        super().__init__(receiver)
        self.amount = amount

    # 调用reciver的方法
    def execute(self): 
        return self._receiver.action('raise_temp', self.amount) 

    def unexecute(self): 
        return self._receiver.action('lower_temp', self.amount) 
                                                     

class LowerTempCommand(Command): 
 
    def __init__(self, receiver, amount=5):
        super().__init__(receiver)
        self.amount = amount

    def execute(self):
        return self._receiver.action('lower_temp', self.amount) 

    def unexecute(self):
        return self._receiver.action('raise_temp', self.amount) 

# 提供execute、undo（即执行上一个传进来的命令对象的unexecute方法）两个接口
class Worker(Invoker): 

    # 用接受的命令来初始化
    def __init__(self): 
        super().__init__([LowerTempCommand, RaiseTempCommand]) 


thermostat = Thermostat() # Create a Receiver.
worker = Worker() # Create an Invoker.

assert "Temperature lowered by 5 degrees" == worker.execute(LowerTempCommand(thermostat)) # Have the Invoker execute a LowerTempCommand
                                                                                          # which uses the thermostat Receiver.
assert "Temperature raised by 5 degrees" == worker.execute(RaiseTempCommand(thermostat)) # Have the Invoker execute a RaiseTempCommand
                                                                                          # which uses the thermostat Receiver.
assert "Temperature lowered by 5 degrees" == worker.undo() # Undo the previous command (Calls the RaiseTempCommand unexecute method.)