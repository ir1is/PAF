import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self):
        self.t = []
        self.x = []
        self.v = []
        self.a = []
        self.kutna_frek = 0
        self.x0 = 0
        self.v0 = 0
        self.a0 = 0

    def set_initial_conditions(self,x0,v0,k,m):
        self.x0 = x0
        self.v0 = v0
        self.a0 = -k/m *x0
        self.kutna_frek = np.sqrt(k/m)
        self.x.append(x0)
        self.v.append(v0)
        self.a.append(self.a0)

    def reset(self):
        self.x = [self.x0]
        self.v = [self.v0]
        self.a = [self.a0]
        self.t = []

    def oscillation(self,t=10,dt = 0.1):
        self.t = [0]
        self.N = int(t/dt)
        for i in range(1,self.N+1):
            self.v.append(self.v[i-1] + self.a[i-1]*dt)
            self.x.append(self.x[i-1]+self.v[i]*dt)
            self.a.append(-1*self.kutna_frek**2*self.x[i])
            self.t.append(i*dt)

    def plotanje(self,t=10,dt=0.001):
        self.oscillation(t,dt)
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
            self.a.append(-1*self.kutna_frek**2*self.x[-1])
            self.t.append(self.t[-1]+dt)
            if (self.x[-1]>=0 and self.x[-2]<0) or (self.x[-1]<=0 and self.x[-1]>0):
                t1.append(self.t[-1])
                b+=1
        return (t1[-1]-t1[-2])*2

            


