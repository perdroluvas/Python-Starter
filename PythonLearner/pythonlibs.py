import sys
import os

for i in range(100):
    print(i)

print("process id: ", os.getpid())
print(os.getppid())

cwd = os.getcwd()
print("current directory: ", cwd)

os.chdir("/")
print("new directory ", os.getcwd())
print("all the files: ", os.listdir(cwd))


for root, dirs, files in os.walk(cwd):
    for name in files:
        print(os.path.join(root,name))
    for name in dirs:
        print(os.path.join(root,name))

print("absolute pathname:", os.path.abspath("text.txt"))
print('exists or not: ', os.path.exists("text.txt"))
#print("size: ", os.path.getsize("text.txt"))
print("is file> ", os.path.isfile("text.txt"))
print("is folder: ", os.path.isdir("text.txt"))

