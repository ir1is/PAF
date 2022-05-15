import projectile as pro
import matplotlib.pyplot as plt
import numpy as np
p1 = pro.Particle()
#p1.set_initial_conditions(0,0,30,5,0.0001,0.5,5.4)

c_lista = np.linspace(0.1,1,100)
x_lista = []
for c in c_lista:
    p1.set_initial_conditions(0,0,30,5,0.001,c,1,4)
    p1.range(0.01)
    x_lista.append(p1.x[-1])
    p1.reset()

fig,(f1,f2)=plt.subplots(1,2)
f1.plot(c_lista,x_lista,label='x-c')


m_lista=np.linspace(1,100,100)
x_lista = []
for m in m_lista:
    p1.set_initial_conditions(0,0,30,5,0.001,0.5,1,m)
    p1.range(0.01)
    x_lista.append(p1.x[-1])
    p1.reset()

f2.plot(m_lista,x_lista,label='x-m')
plt.show()
plt.legend()
