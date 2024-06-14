
#Varios exemplos de codigo condicional!!!

count = 0
while count < 20:
    print(count)
    count = count + 1

x = 0

while x < 10:
    print (f'O valor de x nesta iteração é: {x}')
    print (f' {x} ainda é menor que 10, somando 1 a {x}')
    x += 1
    
else:
    print ('Loop concluído!')

counter = 0
while counter < 100:
    if counter == 4:
        break
    print(counter)
    counter = counter + 1

for verificador in "python":
    if verificador == "h":
        continue
    print(verificador)

# O que faz a função "range"? Exemplos!
# A função "range" retorna uma sequência de números.
# Ele é usado principalmente para iterar em loops.
# Exemplo:
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Podemos criar sequências de números a partir de 1 número, 2 números, ou até mesmo de uma razão.
# Exemplo:
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Se você quiser uma lista com os números da sequência, pode usar a função "list".
my_list = list(range(1, 6))
print(my_list)  # [1, 2, 3, 4, 5]



