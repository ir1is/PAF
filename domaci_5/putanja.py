import numpy as np
import matplotlib.pyplot as plt

class particle:
    def __init__(self,q,m,Bx,By,Bz,Ex,Ey,Ez,vx,vy,vz):
        self.x = []
        self.y = []
        self.z = []
        self.v = [np.array((vx,vy,vz))]
        self.E = [np.array((Bx,By,Bz))]
        self.B = [np.array((Ex,Ey,Ez))]
        self.q = q
        self.m = m
        self.t=[0]
        self.dt = 0.01

    def __move(self,dt=0.01):
        F = self.q*(self.E[-1]+np.cross(self.v[-1],self.B[-1]))
        self.a = []
        self.a.append(F/self.m)
        self.B.append(self.B[-1]+self.kB*self.t[-1])
        self.E.append(self.E[-1]+self.kE*self.t[-1])
        self.v.append(self.v[-1]+self.a[-1]*dt)
        self.r.append(self.r[-1]+self.v[-1]*dt)
        self.t.append(self.t[-1]+dt)

    def move(self,t,koeficijent_t_ovisnosti_B,koef_t_ovisnosti_E,x0,y0,z0):
        self.kB =koeficijent_t_ovisnosti_B
        self.kE = koef_t_ovisnosti_E
        self.r=[np.array((x0,y0,z0))]
        while self.t[-1]<t:
            self.__move(10)

    def koordinate(self):
        for r in self.r:
            self.x.append(r[0])
            self.y.append(r[1])
            self.z.append(r[2])
        return self.x,self.y,self.z