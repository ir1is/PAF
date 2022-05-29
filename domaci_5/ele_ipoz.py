from putanja import particle
import matplotlib.pyplot as plt
import numpy as np

el = particle(-1,1,0,0,0,0,0,0,1,1,1)
poz= particle(1,1,0,0,0,0,0,0,1,1,1)

el.move(10,np.array((0,0,0.1)),np.array((0,0,0.1)),0,0,0)
xe,ye,ze = el.koordinate()

poz.move(10,np.array((0,0,0.1)),np.array((0,0,0.1)),0,0,0)
xp,yp,zp = poz.koordinate()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(xe, ye, ze, label='elektron')
ax.plot(xp, yp, zp, label='pozitron')
ax.set_xlabel('x/m')
ax.set_ylabel('y/m')
ax.set_zlabel('z/m')
ax.legend()
plt.show()