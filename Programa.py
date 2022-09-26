#Autor: Ichel Delgado

#Librerías a utilizar
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols

#Se define el rango y el dominio de los ejes
rango = 200
x = np.arange(-rango,rango,0.1)
y = np.arange(-rango,rango,0.1)

#Se dibujan dos líneas, una horizontal y una vertical que serán los ejes x e y respectivamente
plt.axhline(color='black', lw=0.5)
plt.axvline(color='black', lw=0.5)

#-------------------------------------------------------
#Se define una función y1, y2, y3 según la cantidad de funciones que sean.
#Con linestyle se define el estilo de linea, si es punteada o no
#con .fill_between se rellena el area abajo o arriba de la función
#Con la función grid se crea la cuadricula de fondo para ayudar a ubicarse en el plano
#Con plot() y show() se crea y se muestra el plano
#-------------------------------------------------------

#Se empiezan a graficar las soluciones de las desigualdades

#1) 2x+y<5
# y1 = -2*x+5
# plt.plot(x, y1 ,linestyle='dashed')
# plt.fill_between(x, y1 , np.min(y1), color='#539ecd', alpha=0.5)
# plt.grid()
# plt.show()

#2) y<=5
# y1 = x*0 + 5
# plt.plot(x, y1)
# plt.fill_between(x, y1 , np.min(y), color='#539ecd', alpha=0.5)
# plt.grid()
# plt.show()

#3) y>(x/2)+1
# y1 = (x/2)+1
# plt.plot(x, y1 ,linestyle='dashed')
# plt.fill_between(x, y1 , np.max(y1), color='#539ecd', alpha=0.5)
# plt.grid()
# plt.show()

#4) y> -2x+3, y > 1/2, x >= y
# y1 = -2*x+3
# y2 = 0*x+0.5
# y3 = x
# plt.plot(x,y1,linestyle='dashed')
# plt.plot(x,y2,linestyle='dashed')
# plt.plot(x,y3)

# plt.fill_between(x, y1, np.max(y1), color='#539ecd',alpha=0.5)
# plt.fill_between(x, y2, np.max(3.7*x), color='#cd8253',alpha=0.5)
# plt.fill_between(x, y3, np.min(y3), color='#9ecd53',alpha=0.5)
# plt.grid()
# plt.show()

#5) 2x+3y<=60, x>= 0, y >= 0
# y1 = -(2/3)*x+20
# y2 = 0*(x)

# plt.plot(x,y1)
# plt.plot(x,y2)

# plt.fill_between(x, y1, np.min(x), color='#539ecd',alpha=0.5)
# plt.fill_between(x, y2, np.max(x*1.5), color='#cd8253',alpha=0.5)
# plt.grid()
# plt.show()

#6) 2x+3y<=60, x>= 0, y >= 0
# y1 = -2*x+180
# y2 = -(x/2)+80
# y3 = -x+100

# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.plot(x,y3)
# plt.plot(40,60,'ro') 
# plt.plot(80,20,'ro') 
# plt.fill_between(x, y1, np.min(x*3), color='#539ecd',alpha=0.5)
# plt.fill_between(x, y2, np.min(x*3), color='#cd8253',alpha=0.5)
# plt.fill_between(x, y3, np.min(x*3), color='#9ecd53',alpha=0.5)
# plt.grid()
# plt.show()

#7) 5x+3y<=105, 2x+4y <= 70
# y1 = (105-5*x)/3
# y2 = (70-2*x)/4

# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.plot(15,10,'ro') 
# plt.fill_between(x, y1, np.min(x*3), color='#539ecd',alpha=0.5)
# plt.fill_between(x, y2, np.min(x*3), color='#cd8253',alpha=0.5)
# plt.grid()
# plt.show()