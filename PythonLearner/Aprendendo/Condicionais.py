#Estrutura das condicionais!

'''
categoria = int(input('Digite a categoria do produto: '))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 28
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else: 
    print('Categoria inválida, digite categoria de 1 a 5')
    preco = 0
print(f'O preço do produto {categoria} é R$: {preco}')
'''
x  =  2 
if x == 1 : print('Bom'); print('Mal'); print('Mau') 
elif x == 2 : print('legal'); print('Ruim') 
else : print('Preto'); print('Branco')

#Especificidades do python!
#O faz nada, porém sem ele não funciona a condicional if em caso de precisar passar void
if True:
    pass
print('oi')



# Tipos de loops do for

# Loop para contagem decrescente
for i in range(6, 0, -1):
    print(i)

# Loop para contagem crescente com incremento de 2
for i in range(0, 10, 2):
    print(i)

# Loop com iteração sobre uma lista
lista = ['a', 'b', 'c']
for elem in lista:
    print(elem)

# Loop com iteração sobre um string
string = 'pedro'
for char in string:
    print(char)


#Funciona que nem nas outras linguagens
n = 6
while n > 0:
    n -= 1
    print(n)

#Essa ação perdura até nas listas, tuplas e dicionários
a = ['bolo', 'refri', 'agua']
while a:
    print(a.pop(-1))

#O break quebra qualquer fluxo de código e o continue pula para o proximo
n  =  5 
while n > 0: 
    n -= 1
    if n == 2: 
        break
print(n) 
print('Loop 1 finalizado')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop 2 finalizado.')

#While e Else exemplo 
n = 5
while n > 0:
    n -= 1
    if n > 2:
        print(n)
    else:
        break
print('Loop 3 finalizado.')

a = ['foo', 'bar']
#print('Hello', a.pop(0))
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
        print('>', b.pop(0))

# Isso vai funcionar
n = 6 
while n > 0: n -= 1; print(n)

