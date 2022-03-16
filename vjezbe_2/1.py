import numpy as np
import matplotlib.pyplot as plt
t = []
x= []
v= []
a = []

def gibanje(F,m):
    a.append(F/m)
    dt = 0.1
    t.append(0)
    x.append(0)
    v.append(0)
    for i in range(0,10):
        t.append(i * dt)
        v.append(v[i]+ a[i]*dt)
        x.append( x[i]+v[i]* dt)
        a.append(F/m)

    plt.plot(t,x, label= 'x-t')
    plt.plot(t,v, label= 'v-t')
    plt.plot(t,a, label='a-t')
    plt.legend()
    plt.show()

gibanje(100,10)