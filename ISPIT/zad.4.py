from VertikalniHitac import VertikalniHitac
import matplotlib.pyplot as plt
import numpy as np

objekt = VertikalniHitac(10,10)

dt_l = np.linspace(0.0001,0.1,1000)
t_l = []
v0=10
analiticki = 2* v0/9.81
greska = []
for i in dt_l:
    objekt.vertikalni(dt=i)
    t_l.append(objekt.vrijeme_trajanja())
    greska.append(abs( t_l[-1]-analiticki)/analiticki  )
    
plt.plot(dt_l,greska)
#plt.set_xlabel('dt')
#plt.set_ylabel('greska (%)')
plt.show()