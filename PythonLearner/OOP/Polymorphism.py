print(len("Hello python!"))

print(len([1,2,3,4,5]))

class Animal:
    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        print("Miau")
class Bird(Animal):
    def sound(self):
        print("Piu piu")
class Fish(Animal):
    def sound(self):
        print("...")

gato = Cat()
passalin = Bird()
pexe = Fish()

gato.sound()
passalin.sound()
pexe.sound()

my_pets = [gato, passalin, pexe]

for x in my_pets:
    x.sound()

print(isinstance(gato, Cat))
print(isinstance(passalin, Bird))