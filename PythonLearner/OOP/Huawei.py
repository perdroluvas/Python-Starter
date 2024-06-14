#Encapsulation, polymorphism, inheritance, absctraction

class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting")
    def run(self):
        print(self.name.title() + " is now running")

#instatiation
my_dog = Dog("Husky",3)
my_dog.sit()
my_dog.run()
print(type(my_dog.run()))

my_dog.food = 'cat food'
print(my_dog.food)

#redefine

class Dog(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "dog name: "+self.name
my_dog = Dog("Goodog")
print(my_dog)
print(type(my_dog))

#encapsulation

