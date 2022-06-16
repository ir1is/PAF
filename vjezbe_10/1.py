from putanja import Particle
import matplotlib.pyplot as plt
import numpy as np

e1 = Particle(-1.,1.,0.,0.,0.,0.,0.,1.,1.,0.1,0.1)
e1.move(10)

p1 = Particle(1,1.,0.,0.,0.,0.,0.,1.,1.,1.,1.)
p1.move(10)

xe,ye,ze = e1.move(10)
xp,yp,zp = p1.move(10)

# fig = plt.figure()
# ax = plt.axes(projection = "3d")
# ax.plot3D(e1.x, e1.y, e1.z)
# #ax.plot3D(p1.x, p1.y, p1.z, linestyle = "dashed")
# plt.show()

e_rk = Particle(1.,1.,0.,0.,1.,0.,0.,1.,1.,1.,1.)
e_rk.move_rk(10)

xe_rk,ye_rk,ze_rk=e_rk.move_rk(10)

ax.plot3D(e_rk.x,e_rk.y,e_rk.z)
plt.show()

