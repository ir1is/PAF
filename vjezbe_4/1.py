import calculus as cl 
import numpy as np
import matplotlib.pyplot as plt

def f2(x):
    return x**3

def f3(x):
    return np.sin(x)
    
#print(cl.derivacija(f2,2,0.01))
# print(cl.derivacija(f2,2,0.001))

# print(cl.derivacija(f2,2,0.001,'two_point'))

# print(cl.derivacija(f3,2,0.001))

# print(cl.derivacija(f3,2,0.001,'two_point'))
    
x,y = cl.derivacija_na_rasponu(f2,1,0,0.02)
plt.plot(x,y)
#plt.show()

x_analiticki = [0]
y_analiticki = [0]
while x_analiticki[-1]<1:
    x_analiticki.append(x_analiticki[-1]+0.02)
    y_analiticki.append(3*x_analiticki[-1]**2)
plt.plot(x_analiticki,y_analiticki,'r')
plt.show()

