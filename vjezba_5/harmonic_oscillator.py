import numpy as np

class HarmonicOscillator:
     def __init__(self):
        self.t = []
        self.x = []
        self.vx = []
        self.ax = []

    def set_initial_conditions(t,faza,x,v,a):
        self.t.append(t)
        self.faza.append(faza)
        self.x.append(x)
        self.v.append(v)
        self.a.append(a)

    def reset(self):
        self.__init__()

    def __move(self)
        self.x.append(x[-1]+self[-1]*dt))
        self.v.append(self.v0 + self.a[-1]*dt)
        self.a.append(-k/m)*self.x[-1])
        self.dt = 0.1