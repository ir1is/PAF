import numpy as np
import matplotlib.pylab as plt

v  = int(input("Pocetna brzina je: "))
g = 9.8
alfa = int(input("Pocetni kut je:"))

t = np.linspace(0, 10, 100) 

x = ((v)* np.cos(alfa)) *t
y = ((v)* np.sin(alfa* np.pi/180) *t) - (0.5*g*(t**2))

kada_padne = 0
for i in range (len(y)):
    if y[i+1] <= 0:
        kada_padne = i
        break
    
x1 = [None] * kada_padne
y1 = [None] * kada_padne

for i in range(kada_padne):
    x1[i]= x[i]
    y1[i]= y[i]
 
t1 = np.linspace(0,10,kada_padne)

plt.plot(t1, y1 , label= " y - t") 
plt.plot(t1, x1, label = "x - t")
plt.plot(x1,y1, label = " x- y")


plt.legend()
plt.show() 