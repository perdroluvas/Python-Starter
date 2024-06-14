with open('text1.txt', "r") as f:
    line = f.readline()
    print("read one line: %s" % (line))

    lines = f.readlines()
    print(lines)