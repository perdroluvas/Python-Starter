#use isinstaance function to check if an object is iterable
#Generator: Função que retorna um lazy iterator(só é iteravel quando __call__())

def fib(n):
    current = 0
    num1, num2, = 0, 1
    while current<n:
        num = num1
        num1, num2 = num2, num1+num2
        current+= 1
        yield num
    yield "done"

g = fib(5)
for x in g:
    print(x)

g = (x*2 for x in range(5))

for x in g:
    print(x)

