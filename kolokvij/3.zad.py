from VertikalniHitac import VertikalniHitac
import matplotlib.pyplot as plt

objekt = VertikalniHitac(10,10)
h,v,t = objekt.vertikalni()
fig,(p1,p2)=plt.subplots(2,1)
p1.plot(t,h,label='h-t')
p2.plot(t,v,label='v-t')
plt.legend()
plt.show()