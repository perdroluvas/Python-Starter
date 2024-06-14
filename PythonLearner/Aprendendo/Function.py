def func():
    print('Hello world')

func()

def fibs(num):
    result = [0,1]
    for i in range (2,num):
        a = result[i-1] + result[i-2]
        result.append(a)
    return result
print(fibs(5))
print(fibs(10))