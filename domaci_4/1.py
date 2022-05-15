import projectile as pro
import matplotlib.pyplot as plt
p1 = pro.Particle()
p2 = pro.Particle()

p1.set_initial_conditions(0,0,30,5,0.0001,0.3,3,3)
p2.set_initial_conditions(0,0,30,5,0.0001,0.3,3,3)


#p1.kugla_kocka(3,'kugla')
xi,yi = p1.kugla_kocka(2,'kugla')
xii,yii = p2.kugla_kocka(4,'kocka')

plt.plot(xi,yi)
plt.scatter(xii,yii)
plt.show()

