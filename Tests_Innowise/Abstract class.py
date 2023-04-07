from abc import ABC, abstractmethod
class Basic (ABC):
     @abstractmethod #им мы обязываем исполнять этот метод у наследников
     def hello (self):
         print('HEllO')
class Next (Basic):
    def hello (self):
        super().hello() #дополнительно вызывает HELLO
        print('Bye')

b=Next()
b.hello()