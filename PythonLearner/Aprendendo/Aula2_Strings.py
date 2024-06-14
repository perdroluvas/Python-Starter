x = 5
x < 10
print(x<10 and callable(x))

#STRINGS!!!!!

#Strings sao imutaveis
s = "Olá"
s = 'Ola'
s = '''Ola'''
s = """Ola"""

x = 'Meu nome '
y = 'é '
z = 'Pedro'

print(x + y + z)
#Não é válido!! print(x*y)
print((x+y+z)*4)


#Strings builtin!

print(ord('a'))
print(ord('z'))
print(chr(97))
print(chr(224))

string = 'Eu sou uma string bonitinhaaaar'
print(len(string))

print(str(3232323.23))
#Mostra o indice da string
print(string[-2])

#Substring ou slicing
#print(string[0:6])
print(string[2:len(string)])
#Mais metodos de string(OOP)
print(string.capitalize())
print(string.lower())
print(string.swapcase())
print(string.title())
print(string.upper())
print(string.count('E',0,10))
