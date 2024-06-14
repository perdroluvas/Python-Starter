import pandas as pd
import numpy as np

#Continuação, Head and Tail

data2 = np.arange(300).reshape(60,5)
#print(data2)
df2 = pd.DataFrame(data2)
print(df2)
#HEad mostra as primeiras linhas do objeto baseado na posição, útil para testar rapidamente se o objeto tem o tipo certo de dado e tail os ultimos

print(df2.head(3))
print(df2.tail(3))

#exemplo de checagem de Index
df = pd.DataFrame(np.random.randn(7,4), index=[2,3,4,5,6,7,8], columns=list('ABCD'))
print(df.index)
print(df.columns)
print(df.values)

#loc, iloc, .loc is primarily label based but may also be used with a boolean array. .loc will raise KeyError when the items are not found

df1 = pd.DataFrame(np.random.randn(6,4),
                   index=list('abcdef'),
                   columns=list('ABCD'))
print(df1)
#corta o C do dataframe, o loc serve para o slicing de dataframes, muito ú
print(df1.loc[['a','b','d'], :])
#Usa a posição para o slaiced
print(df1.iloc[[0,1,3], :])

#statistica descritiva
print(df1.count())
print(df1.mean())
print(df1.std())
print(df1.sum())
#mts mts dados
print(df1.describe())
#Delete elementos do dataframe!!
data3 = np.arange(30).reshape(6,5)
df3 = pd.DataFrame(data3, index=['a', 'b', 'c', 'd', 'e', 'f'], columns = ['A', 'B', 'C', 'D', 'E'])
print(df3)
a = df3.drop(['a'], axis = 0) #axis = 0, delete as linhas
print(a)
b = df3.drop(['A'], axis = 1) # axis=1, delete as colunas
print(b)
print(' ')
#Adicione/Append/Ajoute elementos ao dataframe!!!
c = b._append(a)
print(c)

#Reindexando os elementos do dataframe
s = pd.Series(np.random.randn(5), index = ['a', 'b', 'c' , 'd', 'e'])
print(s)
print(s.reindex(['e', 'b', 'f', 'd']))
#Iteravellll
df4 = pd.DataFrame(np.random.randn(4,3), columns = ['A', 'B', 'C'])
df4
i = 1
for s in df4.iterrows():
    print('collumn: %d value: %s'%(i,s))
    i +=1
#Mudança percentual entre os proximos valores
s = pd.Series([1,2,3,4,5,4])
print(s.pct_change())
#Covariancia(Nao sei oq é mas é em pares)
s1 = pd.Series(np.random.randn(1000))
s2 = pd.Series(np.random.randn(1000))
print(s1.cov(s2))
#tbm pode ser em dataframe
frame = pd.DataFrame(np.random.randn(1000,5),
                     columns=['a','b','c','d','e'])
print(frame.cov())

#SORTING
#Tres tipos: pelo label de index, pelos valores de colunas e pela combinação de ambos

#por IndexError
df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a', 'b','c']),
    'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
    'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})
print(df)

unsorted_df = df.reindex(index = ['d', 'a' ,'c', 'b'],
                         columns= ['three', 'two', 'one'])
print(unsorted_df)
print(unsorted_df.sort_index())
print(unsorted_df.sort_index(ascending=False))

df5 = pd.DataFrame({'one': [2,1,1,1],
                    'two': [1,3,2,5],
                    'three': [5,4,3,2]})
print(df5.sort_values(by='one'))

#Trabalhando com dados que faltam(CONT)



