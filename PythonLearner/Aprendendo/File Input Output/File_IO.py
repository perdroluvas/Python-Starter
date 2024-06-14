f = open("text.txt", 'w', encoding='utf8')#python abrirá o arquivo! ou criará
inputs = input("input: ")
f.write(inputs)
f.close()