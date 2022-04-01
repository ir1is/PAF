import calculus as cl
import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return x**(1/2)

gornja_m = []
donja_m=[]
trapezna_rj = []
analiticki = []
dx = []

for i in range(1,10):
    N = i *100
    dx.append(N)
    gornja_m.append(cl.integral(f1,1,3,N)[0])
    donja_m.append(cl.integral(f1,1,3,N)[1])
    trapezna_rj.append(cl.trapez(f1,1,3,N))
    analiticki.append(2.797434948)
plt.plot(dx,analiticki,'r',label='analiticki')
plt.scatter(dx,gornja_m)
plt.scatter(dx,donja_m)
plt.scatter(dx,trapezna_rj,label='trapezna metoda')
plt.legend()
plt.show()

     

