with open("text1.txt", 'w') as f:
    f.write("python is cool\n this is a pen \n I like apple")
with open("text1.txt", 'r') as f:
    print(f.read())