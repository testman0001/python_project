# 工厂模式
# 实现解耦，将对象创建和初始化的逻辑解耦出来，集中管理创建流程，增加灵活性和可维护性
from pypattyrn.creational.factory import Factory  


# 定义两个类，speak内部实现有差异
class Cat(object):

    def speak(self):
        print('meow')


class Dog(object):

    def speak(self):
        print('woof')


# 定义工厂，根据需要创建出不同类的实例，创建过程延迟
class AnimalFactory(Factory):  

    def create(self, animal_type):  
        if animal_type == 'cat':
            return Cat()
        elif animal_type == 'dog':
            return Dog()
        else:
            return None


animal_factory = AnimalFactory()

cat = animal_factory.create('cat')
dog = animal_factory.create('dog')

# 不同参数创建出的实例基于不同的类，行为有差异
cat.speak()  # 'meow'
dog.speak()  # 'woof'