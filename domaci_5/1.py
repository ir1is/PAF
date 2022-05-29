from putanja import particle
import matplotlib.pyplot as plt
import numpy as np

e1 = particle(1,1,1,0,0,0,0,0,0,1,1)
e1.move(10,np.array((0,0,0.1)),np.array((0,0,0.1)),0,0,0)
x1,y1,z1=e1.koordinate()

e2 = particle(1,1,1,0,0,0,0,0,0,1,1)
e2.move(10,np.array((0,0,0)),np.array((0,0,0)),0,0,0)
x2,y2,z2=e2.koordinate()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x1, y1, z1, label='promjenjivo polje')
ax.plot(x2, y2, z2, label='nepromjenjivo polje')
ax.set_xlabel('x/m')
ax.set_ylabel('y/m')
ax.set_zlabel('z/m')
ax.legend()
plt.show()