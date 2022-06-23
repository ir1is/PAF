from VertikalniHitac import VertikalniHitac
import matplotlib.pyplot as plt
objekt = VertikalniHitac(10,10)
dt_l = [0.01,0.05,0.1]
h =[]
t= []
for i in dt_l: 
    h.append(objekt.max_h_otporz(3,5,dt=i))
    t.append(objekt.vrijeme_trajanja_otporz(3,5,dt=i))
fig,(p1,p2)= plt.subplots(2,1)
p1.plot(dt_l,h,label='hmax-dt')
p2.plot(dt_l,t,label='vrijeme-dt')
plt.tight_layout()
plt.show()