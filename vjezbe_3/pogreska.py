import particle as prt
import matplotlib.pyplot as plt
import numpy as np

dt = []
p1 = prt.Particle()
v0 = 10
kut = 60
p1.set_initial_conditions(0,0,kut,v0)
r_pogreska=[]

for i in range(1,1000):
    dt.append(i/1000)
    p1.dt = i/1000
    r_numericki = p1.range()
    r_analiticki = (v0**2/9.81)*np.sin(np.radians(2*kut))
    r_pogreska += [abs(r_analiticki-r_numericki)/r_analiticki] 
    p1.reset()
    p1.set_initial_conditions(0,0,kut,v0)

plt.plot(dt,r_pogreska)
plt.xlabel('dt')
plt.ylabel('relativn apogreška')
plt.show()
    


