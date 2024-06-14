for i in range(1,10,1):
    print(i)

dict_estudantes = {'Larissa':25, 'Claudinha' : 27}

for i in dict_estudantes:
    print(dict_estudantes.items())

print(iter(dict_estudantes))
# conjuntos(sets)
iter({'filme', 'série', 'desenho'})

a = (['manga', 'bacurí', 'ata'])
itr = iter(a)
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
#print(itr.__next__()) impossível iterar mais

d = {'um': 1, 'dois': 2, 'tres': 3}
for k in d.values():
    print(k)


d = {'um': 1, 'dois': 2, 'tres': 3}
for k in d.keys():
    print(k)

for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

for k in d.items():
    print(k)    

d = {'um': 1, 'dois': 2, 'tres': 3}
for k, v in d.items():
    print('k =', k, ', v =', v)


listaC = [9, 7, 10, 15, 19]
count = 0
for item in listaC:
    count += 1
    
print(count)


listaD = [[3, 6, 9], [12, 17, 10], [10, 8, 2]]
primeira_linha = listaD[0]
count = 0
for column in primeira_linha:
    count = count + 1
    
print(count)
