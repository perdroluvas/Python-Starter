def decorate(func):
    def decorated():
        print("I got decorated!")
        func()
    return decorated

@decorate #se remover, tira a decoração
def plain():
    print("I am plain")

plain()