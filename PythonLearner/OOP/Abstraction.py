from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eats_grass(self):
        pass

    def is_animal(self):
        return True
    
class Cat(Animal):
    def __init__(self):
        print("miew~~")
    def eats_grass(self):
        return False

#abstract methods must be applie to its "child"
miew = Cat()

print(miew.is_animal())
print(miew.eats_grass())

