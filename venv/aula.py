import matplotlib.pyplot as plt
x = [0,1,2,50,55,60]
y = [0,1,4,9,16,25]
z = [0,1,8,27,64,125]

plt.plot(x,y, 'r--^', label = 'Curva 1') #Desenha o gráfico
plt.plot(x,z, 'p--b', label = 'Curva 2')
plt.plot(z,y ,'g', label = 'Curva 3')
plt.legend(loc ='lower right') # Ou sem parametro
plt.show() #Mostra o gráfico


