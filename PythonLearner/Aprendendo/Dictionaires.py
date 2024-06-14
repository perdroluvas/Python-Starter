dict_estudantes = {"Sávio":35, "Priscila":21, "Tatiane":21, "Vinícius":25}
print(dict_estudantes)

# Métodos de Dictionaries
print('\nMétodos de Dictionaries:')

# Adicionar um par chave-valor
dict_estudantes['Sávio'] = 36
print(dict_estudantes)

# Remover um par chave-valor
del dict_estudantes['Priscila']
print(dict_estudantes)

# Verificar se uma chave existe no dicionário
print('"Sávio" in dict_estudantes:', "Sávio" in dict_estudantes)
print('"Tatiane" not in dict_estudantes:', "Tatiane" not in dict_estudantes)

# Contar quantos pares existem no dicionário
print(f'len(dict_estudantes):'+str({len(dict_estudantes)}))

# Verificar se um dicionário está vazio
print('dict_estudantes:', dict_estudantes)
print('bool(dict_estudantes):', bool(dict_estudantes))

# Criar um novo dicionário a partir de um iterável de pares chave-valor
dict_novo = dict([('a', 1), ('b', 2)])
print(dict_novo)

# Copiar um dicionário
dict_novo = dict_estudantes.copy()
print(dict_novo)
print("Existe??", bool(dict_estudantes))
# Limpar um dicionário
dict_estudantes.clear()
print("Existe?", bool(dict_estudantes))
print(dict_estudantes)


# Iterar sobre os pares chave-valor de um dicionário
for chave, valor in dict_novo.items():
    print(f'{chave}: {valor}')

# Iterar sobre apenas as chaves de um dicionário
for chave in dict_novo.keys():
    print(chave)

# Iterar sobre apenas os valores de um dicionário
for valor in dict_novo.values():
    print(valor)


