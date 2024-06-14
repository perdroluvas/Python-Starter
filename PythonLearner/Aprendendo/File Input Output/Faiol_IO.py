f = open('text.txt', 'a')
f.write(' i appended more content!!!')
print(f.read())
f.close()