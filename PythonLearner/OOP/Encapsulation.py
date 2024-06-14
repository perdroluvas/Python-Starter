class Simplecounter:
    __secretCount = 0 #private variable, private data and methods with "__" at start
    publicCount = 0
    def count(self):
        self.__secretCount += 100
        print(self.__secretCount)
counter = Simplecounter()
counter.count()
print(counter.publicCount)
#não consegue acessar o secret count
#print(counter.__secretCount)