import projectile as pro 
import matplotlib.pyplot as plt

prt1 = pro.Particle()

prt1.set_initial_conditions(0,0,30,10,0.0001,10,0.5,5)
prt1.range(0.01)

plt.plot(prt1.x[:-1],prt1.y[:-1])

plt.xlabel('x')
plt.ylabel('y')
plt.show()



