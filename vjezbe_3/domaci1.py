import numpy as np
import matplotlib.pyplot as plt
import math

class Particle:
    def __init__(self):
        self.t = []
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ay =[]
        self.ax = []
        
    def set_initial_conditions(self,x0,y0,kut,v0):
        self.t.append(0)  
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v0 * np.cos(np.radians(kut)))
        self.vy.append(v0 * np.sin(np.radians(kut)))
        self.ay.append(9.81)
        self.ax.append(0)
        self.dt = 0.1

    def reset(self):
        self.__init__()
    
    def __move(self):
        self.t.append(self.t[-1]+ self.dt)
        self.vy.append(self.vy[-1]-self.ay[-1] * self.dt)
        self.vx.append(self.vx[-1]+self.ax[-1] * self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
        
    def range(self):
        while self.y[-1]>=0:
            self.__move()
        return self.x[-1]

    def velocity_to_hit_target(self,xi,yi,r,kut):
        v=1
        dv=0.01
        self.set_initial_conditions(0,0,kut,v)
        while True:
            while (math.dist([xi,yi],[self.x[-1],self.y[-1]]))>r and self.y[-1]>=0:
                self.__move()
            if self.y[-1]<0:
                v+=dv
            else:
                break
            self.reset()
            self.set_initial_conditions(0,0,kut,v)
        return v

    def angle_to_hit_target(self,xi,yi,r,v0):
        kut=1
        dkut=0.1
        self.set_initial_conditions(0,0,kut,v0)
        while kut<90:
            while ((self.x[-1]-xi)**2+(self.y[-1]-yi)**2)>r**2 and self.y[-1]>=0:
                self.__move()
            if self.y[-1]<0:
                kut+=dkut
            else:
                break
            self.reset()
            self.set_initial_conditions(0,0,kut,v0)
        return kut



