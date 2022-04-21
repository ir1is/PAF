def gibanje(F,m,t,x0=0,v0=0,dt=0.01):
    t_list=[0]
    x=[x0]
    v=[v0]
    a=[F(v0,x0,t_list[0])/m]
    while t_list[-1]<t:
        t_list.append(t_list[-1]+dt)
        a.append(F(v[-1],x[-1],t_list[-1] )/m)
        v.append(v[-1]+a[-1]*dt)
        x.append(x[-1]+v[-1]*dt)
    return v[-1],x[-1],a[-1]