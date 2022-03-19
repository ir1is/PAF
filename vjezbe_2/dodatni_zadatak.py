from re import T
import numpy as np
import matplotlib.pyplot as plt

def x_y(theta,v0):
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

    plt.plot(x1,y1)
    plt.set_xlabel('x')
    plt.show()

def max_visina(v0,theta):
    t = 0
    x = [0]
    y = [0]
    v_x=v0*np.cos(theta/180 *np.pi)
    v_y=[v0 * np.sin(theta /180 * np.pi)]
    a_y= [9.81]
    dy = 0.01
    dt = 0.01
    while True:
        x.append(x[-1] +v_x* dt)
        y.append(y[-1] + v_y[-1] * dt)
        v_y.append(v_y[-1]- a_y[-1] * dt)
        if abs(y[-1]- y[-2])<= dy:
            break
        elif y[-1]<y[-2]:
            dt=-dt/2
    
    print('max y je',y[-1] )

def domet(v0,theta):
    t = 0
    x = [0]
    y = [0]
    v_x=v0*np.cos(theta/180 *np.pi)
    v_y=[v0 * np.sin(theta /180 * np.pi)]
    a_y= [9.81]
    dt = 0.01
    dy = 0.01
    while True:
        x.append(x[-1] +v_x* dt)
        y.append(y[-1] + v_y[-1] * dt)
        v_y.append(v_y[-1]- a_y[-1] * dt)
        if abs(y[-1]-0)<dy:
            break
        elif y[-1]<0 and y[-2]>0 or y[-1]>0 and y[-2]<0:
            dt = -dt/2
    print('domet je', x[-1])

def max_brzina(v0,theta):
    t = 0
    x = [0]
    y = [0]
    v_x=v0*np.cos(theta/180 *np.pi)
    v_y=[v0 * np.sin(theta /180 * np.pi)]
    a_y= [9.81]
    v=[v0]
    dt = 0.01
    dy = 0.01
    while True:     
        x.append(x[-1] +v_x* dt)
        y.append(y[-1] + v_y[-1] * dt)
        v_y.append(v_y[-1]- a_y[-1] * dt)
        v.append(np.sqrt(v_x**2 + v_y[-1]**2))
        if abs(y[-1]-0)<dy:
            break
        elif y[-1]<0 and y[-2]>0 or y[-1]>0 and y[-2]<0:
            dt = -dt/2
    print('najveca brzina je ', v[-1])

def meta(v0,theta,xi,yi,r):
    t = 0
    x = [0]
    y = [0]
    v_x=v0*np.cos(theta/180 *np.pi)
    v_y=[v0 * np.sin(theta /180 * np.pi)]
    a_y= [9.81]
    d =[np.sqrt(xi**2+yi**2)-r]
    dt= 0.01
    while True:
        x.append(x[-1] +v_x* dt)
        y.append(y[-1] + v_y[-1] * dt)
        v_y.append(v_y[-1]- a_y[-1] * dt)
        d.append(np.sqrt((xi-x[-1])**2+(yi-y[-1])**2)-r)
        if d[-1]<0:
            print('meta je pogođena')
            break
        elif y[-1]<0:
            print('meta nije pogođena,projektil je pao, najbliža udaljenost je', min(d))
            break
    me_ta = plt.Circle((xi,yi),r)
    figure,axes = plt.subplots()
    axes.add_patch(me_ta)
    axes.plot(x,y)
    plt.show()
        



        

        









