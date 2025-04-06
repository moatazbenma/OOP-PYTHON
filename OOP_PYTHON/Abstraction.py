from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta): #you can't use it , you are able just to do inheretance

    @abstractmethod
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    @abstractmethod
    def sound(self):
        return ""

        
class cat(Animal):
    def __init__(self, name, speed):
        Animal.__init__(self, name, speed)
        
    def sound(self):
        return "meow"

        
class dog(Animal):
    def __init__(self, name, speed):
        Animal.__init__(self, name, speed)
        
    def sound(self):
        return "haw haw"

        
dog1 = dog("BO3O", 120)  

print(dog1.name)
print(dog1.sound())
    