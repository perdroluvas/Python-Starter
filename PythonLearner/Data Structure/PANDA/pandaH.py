import pandas as pd
import numpy as np

s = pd.Series([1,3,4,np.nan,6,8]) #np.nan: Not a number
print(s) #NaN é o sinal de que falta o dado padrão de pandas.

#criar uma series com nd.array

data = np.array(['a','b', 'c', 'd'])
s = pd.Series(data)
print(s)

#criar uma series de um dict

data1 = {'a': 0, 'c': 1, 'd': 2.}
s = pd.Series(data1)
print(s)

#DataFrame é uma estrutura de dados Bidimensional com colunas de tipos potencialmente diferentes.
#É uma spreadsheet ou uma dict de Series de objetos. É o tipo mais comum usado em PANDAS.

df = pd.DataFrame(np.random.randn(7,4), index=[2,3,4,5,6,7,8], columns=list('ABCD'))
print(df)

df1 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20241006'),
    'C': pd.Series(1,index=list(range(4)), dtype='float32'),
    'D': np.array([3]*4, dtype='int32'),
    #Categoricals can only take a limited
    'E': pd.Categorical(['test', 'train','test', 'train']),
    'F': 'foo'})
print(df1)
