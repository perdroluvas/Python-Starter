# Listas e tuplas
# Listas são mutáveis, permitem adicionar e remover itens.
# Tuplas são imutáveis, não permitem adicionar nem remover itens.

# Criação de listas
lista = [1, 2, 3, 4, 5]
print(lista)

lista_vazia = []
print(lista_vazia)

lista_unidimensional = ['a', 'b', 'c']
print(lista_unidimensional)

lista_multi = [['a', 'b', 'c'], ['d', 'e', 'f']]
print(lista_multi)

# Acesso a elementos
print(lista[0])
print(lista[-1])

# Métodos de lista
lista.append(6)
print(lista)
lista.extend([7, 8, 9])
print(lista)
lista.insert(2, 'meio')
print(lista)
lista.remove('meio')
print(lista)
lista.pop()
print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)
lista.clear()  # Remove todos os elementos
print(lista)


# Criação de tuplas
tupla = (1, 2, 3, 4, 5)
print(tupla)

tupla_vazia = ()
print(tupla_vazia)

tupla_unidimensional = ('a', 'b', 'c')
print(tupla_unidimensional)

tupla_multi = (('a', 'b', 'c'), ('d', 'e', 'f'))
print(tupla_multi)

# Acesso a elementos
print(tupla[0])
print(tupla[-1])

# Tuplas não permitem alteração
#lista.append(6)  # Erro
#lista.extend([7, 8, 9])  # Erro
#lista.insert(2, 'meio')  # Erro
#lista.remove('meio')  # Erro
#lista.pop()  # Erro
#lista.reverse()  # Erro
#lista.sort()  # Erro
#lista.clear()  # Erro
x  =  ['Pera', 'Maçã', 'Banana', 'Goiaba'] 
y  =  ['Goiaba', 'Banana', 'Maçã', 'Pera'] 
print(x == y) 
