cat = 100
name = 'Hello'
List1 = [1,2,3,4]
print(List1[1])


tupla = (1, 2, 3, 4)
print(tupla[2])

dict_example = {"name": "John", "age": 30}
print(dict_example["name"])
print(dict_example.get("age"))


# Pass data to a function with no arguments
def my_func():
    print('No arguments passed')

my_func()

# Pass a single argument
def my_func(x):
    print(x)

my_func(5)

# Pass multiple arguments
def my_func(x, y, z):
    print(x, y, z)

my_func(1, 2, 3)

# Pass a list of arguments
def my_func(*args):
    for item in args:
        print(item)

my_func(1, 2, 3, 4, 5)

# Pass a dictionary of arguments
def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')

my_func(name='John', age=30)

# Pass a combination of arguments and keyword arguments
def my_func(x, y, z, **kwargs):
    print(x, y, z)
    for key, value in kwargs.items():
        print(f'{key}:{value}')

my_func(1, 2, 3, name='John', age=30)
