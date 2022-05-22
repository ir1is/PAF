import matplotlib.pyplot as plt
import projectile as pro
p1 = pro.Particle()
#p1.meta(5,5,1)
ro,x,y = p1.meta(1,0.3,0.1)
#plt.plot(x,y)
c1=plt.Circle((1,0.3),0.1)
plout= plt.subplot()
plout.add_patch(c1)
plout.plot(x,y)
plt.show()