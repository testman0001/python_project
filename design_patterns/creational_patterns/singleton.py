# 单例模式
# 保证每个类只有一个实例
from pypattyrn.creational.singleton import Singleton


# 下面两个类都继承了Singleton，实例化时每个类只会有一个实例，且互不干扰
class DummySingletonOne(object, metaclass=Singleton):

    def __init__(self):
        pass


class DummySingletonTwo(object, metaclass=Singleton):

    def __init__(self):
        pass


dummy_class_one_instance_one = DummySingletonOne()
dummy_class_one_instance_two = DummySingletonOne()

dummy_class_two_instance_one = DummySingletonTwo()
dummy_class_two_instance_two = DummySingletonTwo()

# 判断同一个类实例化两次是不是同一个实例（是）
assert id(dummy_class_one_instance_one) == id(dummy_class_one_instance_two)
assert id(dummy_class_two_instance_one) == id(dummy_class_two_instance_two)

# 判断不同类各自实例化一次是不是同一个实例（不是）
assert id(dummy_class_one_instance_one) != id(dummy_class_two_instance_one)
assert id(dummy_class_one_instance_two) != id(dummy_class_two_instance_two)