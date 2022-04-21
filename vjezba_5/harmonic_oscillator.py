import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self):
        self.t = []
        self.x = []
        self.v = []
        self.a = []
        self.om = 0

    def set_initial_conditions(self,x0,v0,k,m,dt=0.01):
        self.k =k
        self.m = m
        self.om = np.sqrt(self.k/self.m)
        self.x.append(x0)
        self.v.append(v0)
        self.a.append(-(self.k/self.m)*x0)
        self.t.append(0)
        self.dt=dt

    def reset(self):
        self.x.clear()
        self.v.clear()
        self.a.clear()
        self.t.clear()

    def oscillation(self,time=10):
        N = int(time/self.dt)
        for i in range(1,N+1):
            self.t.append(self.t[i-1]+self.dt)
            self.a.append(-1*(self.k/self.m)*self.x[i-1])
            self.v.append(self.v[i-1] + self.a[i]*self.dt)
            self.x.append(self.x[i-1]+self.v[i]*self.dt)
            
    def plotanje(self):
        self.oscillation()
        fig, axes = plt.subplots(1, 3)
        axes[0].plot(self.t,self.x)
        axes[0].set_title("x-t")
        axes[1].plot(self.t,self.v)
        axes[1].set_title("v-t")
        axes[2].plot(self.t,self.a)
        axes[2].set_title("a-t")
        plt.tight_layout()
        plt.show()

    def t_titranja(self,dt=0.001):
        t1=[]
        self.t=[0]
        b = 0
        while b<2:
            self.v.append(self.v[-1]+self.a[-1]*dt)
            self.x.append(self.x[-1]+self.v[-1]*dt)
            self.a.append(-1*(self.k/self.m)*self.x[-1])
            self.t.append(self.t[-1]+dt)
            if (self.x[-1]>=0 and self.x[-2]<0) or (self.x[-1]<=0 and self.x[-1]>0):
                t1.append(self.t[-1])
                b+=1
        return (t1[-1]-t1[-2])*2

            


