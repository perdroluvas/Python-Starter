#Outros métodos de numpy:
import numpy as np
f = np.arange(10,20,2)
print('sequencia de numeros no vetor: ', f)

g = np.linspace(0,99,10)
print(g)

a = np.array([[1,2],[3,4],[5,6]])
print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype)

#indexing, slicing and iterating!!!

#indexing
q = np.array([[1,2],[3,4]])
w = q[0][1]
print('q: ',q)
print('w:\n ',w)

#slicing
e = np.arange(10)
print(e[2:8:2])
print(e[2:8])
print(e[2])
print(e[2:])

