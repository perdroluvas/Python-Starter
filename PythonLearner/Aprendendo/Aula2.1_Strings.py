# exemplos de formas de se implementar strings em python

# f-string
name = 'Pedro'
age = 25
city = 'São Paulo'
print(f'Meu nome é {name}, tenho {age} anos e sou de {city}.')

# String concatenation
print('Ola, ' + name + '!')

# String repetition
print('-' * 10)

# Convert String to list
print(list('Ola, mundo!'))

# String slice
print('Ola, mundo! slice'[0:5])

# String split
print('Ola, mundo! split'.split(','))

# String find
print('Ola, mundo! find'.find('mundo'))

# String join
print(','.join(['Ola', 'mundo join', '!']))

# String upper and lower
print('ola, mundo!'.upper())
print('OLA, MUNDO!'.lower())

# String strip
print('   Ola, mundo!   '.strip())

# String replace
print('Ola, mundo!'.replace('mundo', 'Pedro'))

# String isalpha, isalnum, isdigit, islower, isupper
print('ola, mundo!'.isalpha())  # False
print('123456'.isalnum())  # True
print('123456'.isdigit())  # True
print('ola, mundo!'.islower())  # False
print('OLA, MUNDO!'.isupper())  # True

