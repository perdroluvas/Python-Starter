dicionario1 = {"blender": 3.70, "python" : 3.8}
k = dicionario1.keys()
v = dicionario1.values()
print(k,v)

dict = {'nome': "Vinicius", 'idade' : 20, 'nota' : 9.5}
valor_1 = input("Digite o valor para chave_1: ")
valor_2 = int(input("Digite o valor para chave_2: "))
valor_7 = input("Digite o valor para chave_7: ")

meu_dicionario = {'chave_1': valor_1, 'chave_2': valor_2, 'chave_7': valor_7}
print(meu_dicionario['chave_2']) #Saida: valor_2
print(type(meu_dicionario['chave_2']))
del(meu_dicionario['chave_1'])
meu_dicionario['chave_4'] = 'valor_4'
print(meu_dicionario)

#Uma lista é composta dessa forma
lista_estudantes = ["Sávio", 35, "Priscila", 21, "Tatiane", 21, "Vinícius", 25] 
#E o dict é dessa forma
dict_estudantes = {"Sávio":35, "Priscila":21, "Tatiane":21, "Vinícius":25}  
print(lista_estudantes)

estudantes2 = {"Jaum":27}
dict_estudantes.update(estudantes2)
print(dict_estudantes)


#Outras operações com dict_estudantes
print(len(dict_estudantes)) #tamanho do dict
print(dict_estudantes.keys()) #chaves do dict
print(dict_estudantes.values()) #valores do dict
print(dict_estudantes.items()) #pares chave-valor
print(dict_estudantes.get('Sávio')) #valor da chave 'Sávio'
print(dict_estudantes.get('João', -1)) #valor da chave 'João' ou -1 caso não exista

dict_estudantes['Sávio'] = 36 #atualizar valor de uma chave
del dict_estudantes['Tatiane'] #remover uma chave
print(dict_estudantes.pop('Vinícius')) #remover e retornar um valor
print(dict_estudantes.popitem()) #remover o último par chave-valor
print(dict_estudantes.clear()) #remover todos os pares chave-valor
print(dict_estudantes)

