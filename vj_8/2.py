import projectile as pro
import matplotlib.pyplot as plt

p1 = pro.Particle()
p2 = pro.Particle()
p1.set_initial_conditions(0,0,30,5,0.01,0.7,1,2)
p2.set_initial_conditions(0,0,30,5,0.01,0.7,1,2)

p1.range(0.01)

p2.runge_kutta()
plt.plot(p1.x[:-1],p1.y[:-1],'r')
plt.scatter(p2.x[:-1],p2.y[:-1])
plt.show()