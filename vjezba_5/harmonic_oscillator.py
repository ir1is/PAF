import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self):
        self.t = [0]
        self.x = []
        self.v = []
        self.a = []

    def set_initial_conditions(self,x0,v0,k,m):
        self.kutna_frek.append(np.sqrt(k/m))
        self.x.append(x0)
        self.v.append(v0)
        self.a.append(-k/m*x0)

    def reset(self):
        self.x = [self.x0]
        self.v = [self.v0]
        self.a = [self.a[0]]
        self.t = [0]

    def oscillation(self,t,dt = 0.1):
        self.t = 0
        self.N = int(t/dt)
        for i in self.N:
            self.x.append(self.x[i-1]+self.v[i]*dt)
            self.v.append(self.v[i-1] + self.a[i-1]*dt)
            self.a.append(-1*self.kutna_frek**2*self.x[i-1])
            self.t += i*dt

    def plotanje(self):
        self.oscillation()
        fig, axes = plt.subplots(1, 2, figsize=(10,4))
        axes[0].plot(t,x)
        axes[0].set_title("x-t")
        axes[1].plot(t,v)
        axes[1].set_title("v-t")
        axes[2].plot(t,a)
        axes[2].set_title("a-t")
        plt.tight_layout()
        plt.show()

            


