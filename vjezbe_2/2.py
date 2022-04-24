
import numpy as np
import matplotlib.pylab as plt
import math as m

def kosi_hitac(v0,theta):
    v0_x = v0 * np.cos((theta/180)* np.pi)
    v0_y = v0*np.sin((theta/180)*np.pi)
    t = list(np.arange(0.0,10,0.1))
    #t =[0]
    x=[0]
    y= [0]
    v_x =[v0_x]
    v_y =[v0_y]
    a_x = [0]
    a_y =[9.81]
    dt =0.1
    for i in range(len(t)-1):
        #t.append(i*dt)
        a_x.append(0)
        a_y.append(9.81)
        v_y.append(v_y[i] - a_y[i] *dt )
        v_x.append(v0_x)
        x.append(x[i]+v_x[i+1]*dt)
        y.append(y[i]+v_y[i+1]*dt)

    pad = 0
    for i in range(len(y)):
        if y[i+1]<= 0:
            pad = i
            break
    x1 = [None]*pad
    y1 = [None]* pad

    for i in range(pad):
        x1[i]=x[i]
        y1[i]= y[i]
    t1 = np.linspace(0,100,pad)


# print(x1)
# print(y1)

    figure,axis = plt.subplots(3,1)
    axis[0].plot(t1,y1)
    axis[1].plot(t1,x1)
    axis[0].set_xlabel('t')
    axis[1].set_xlabel('t')
    axis[0].set_ylabel('y')
    axis[1].set_ylabel('x')
    axis[2].plot(x1,y1)
    axis[2].set_xlabel('x')
    axis[2].set_ylabel('y')



    # v[i+1]=v[i] + a *dt
    # x[i+1]=x[i]+ v[i] *dt
# fig, axis = plt.subplots(1, 1, figsize=(14, 4))

# axis[0].plot(t, x)
# axis[0].set_title("x-t")

# axis[1].plot(t,y)
# axis[1].set_title("y-t")
    
    figure.tight_layout()
    plt.show()

kosi_hitac(23,43)


