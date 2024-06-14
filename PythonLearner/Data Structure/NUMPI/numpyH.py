import numpy as np

a = np.array([1,2,3,4,5,6])#vetor unidimensional
print('one-dimensional array: ', a)
b = np.array([[1,2,3],[4,5,6]])
print('multidimensional array: ', b)

c = np.zeros([5,5])
print('array full of zeroes:\n ',c)

d = np.ones([2,2])
print('array full of ones:\n ', d)

e = np.empty([3,3]) #randomizado
print('array vazio:\n ',e)

f = np.eye(5)
print('array 2d traço: \n', f)

g = np.asarray([1,2,3,4,5,6])
print('array asarray inputado: ', g)

#array() salva uma cópia! como default. enquanto asarray não irá a não ser que seja necessário

ar = np.array([1,2], dtype=np.float32)

print('data not changed: ',np.array(ar, dtype=np.float32) is ar)
print('data changed: ', np.array(ar, dtype = np.float64) is ar)
print('data not changed: ', np.asarray(ar, dtype=np.float32) is ar)
print('data changed: ', np.asarray(ar, dtype=np.float64) is ar)

