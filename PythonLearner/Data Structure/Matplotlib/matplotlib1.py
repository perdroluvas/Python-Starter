import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#gere o data para plotar
x = np.arange(0,3 * np.pi, 0.1)
y = np.sin(x)
#matplotlib.pyplot.plot(*args, scalex = true, scaley = True, data = None, **kwargs)
#plot y versus x as lines and/or markers. *args includes data, color, format... etc

plt.plot(x,y)
plt.show()

#outro grafico
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.subplot(1,2,1)
plt.plot(x,y_sin)
plt.title('Sine')
plt.subplot(1,2,2)
plt.plot(x,y_cos)
plt.title('Cosine')
plt.show()

#8 por 6(inches), dpi é a resolução da figura(dot per inch)
plt.figure(figsize=(8,6), dpi=80)

#gere a data
X = np.linspace(-np.pi, np.pi, 256, endpoint = True)
C,S = np.cos(X), np.sin(X)

#desenhe uma curva azul com um formato customizado
plt.plot(X, C, color = "blue", linewidth=1.0, label="Blue", linestyle="--")
#desenhe uma curva verde com um formato customizado
plt.plot(X, S, color="green", linewidth=1.0, label="Green", linestyle="-.")

plt.legend()#Legenda
plt.xlim(-4.0,4.0) #escala do eixo X
plt.xticks(np.linspace(-4,4,9,endpoint=True))#localização dos ticks atuais
plt.ylim(-1.0,1.0)#escala do eixo Y
plt.yticks(np.linspace(-1.0,1.0,5,endpoint=True))
#plt.savefig("exercicio.png",dpi=72) para salvar a figure
plt.show()

#mudar cor e linewidth
plt.figure(dpi=80)
plt.plot(X,C,color="blue", linewidth=3.5, linestyle="--")
plt.plot(X,S, color="red", linewidth=2.5, linestyle="-")
plt.show()


#scatterplot!

a = np.random.randint(0,20,15)
b = np.random.randint(0,20,15)
print(a)
print(b)

#matplotlib.pyplot,scatter(x,y, s=None, c=None, marker= None, cmap=None)
#scatter plot of y vs. x with varying marker size and/or color.
plt.scatter(a,b,c='blue', s=100, marker='.')#plot scatter
plt.show()

#bar plot!!!
level = ['Excellent', 'good', 'soso']
x = range(len(level)) #eixo x
y = [1,3,2] #eixo y
plt.figure(dpi=100)

#matplotlib.pyplot.bar(x,heigh,width=0.8,bottom=None, *, align='center')
#make a bar plot
plt.bar(x,y,width=0.5, color=['b', 'r', 'g'])#plot figure
plt.xticks(x,level)
#add grid

plt.grid(linestyle="--", alpha=0.5)
plt.show()

#histograma

t = np.random.randint(0,30,90)
print(t)

#cria uma figura
plt.figure(dpi=100)
group_num = 14
#matplotlib.pyplot.hist(x,bins=None,range=None,density=False, weights=None)
#plota um histograma, x indica a data, bins indica o numero de bins
plt.hist(t,facecolor="blue", edgecolor="black", bins=group_num, alpha=1)
plt.xticks(range(min(t), max(t))[::2])
plt.grid(linestyle="--",alpha=0.5)
plt.show()
