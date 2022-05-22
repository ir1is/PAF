import numpy as np

class Bungee:
    def __init__(self):
        self.x = []
        self.E =[]
        self.t = []
        self.g =9.81
        self.U = []
        self.C = C 
        self.A = A
        self.v = []
        self.a_oz = []
        self.a = 0
    def set_init(self,v,k,m,h,l,rho,C,A,q,xi,o_z=True,dt=0.1):
        self.k = k
        self.m = m
        self.h = h
        self.rho = rho
        self.C = C
        self.A = A
        self.q = q
        self.l = l
        self.o_z = o_z
        self.x.append(xi)
        self.t.append(0)
        self.U.append(m*self.g*h)
        self.vi = vi
        self.v.append(v)
        self.dt = dt

    def __move(self):
        dx=self.h-self.l-self.x[-1]
        if dx<0:
            a_elast = 0
            self.t.append(self.t[-1]+ self.dt)
            self.a_oz.append(self.g-np.sign(self.v[-1])*(self.rho*self.C*self.A/2*self.m)*self.v[-1]**2)
            self.v.append(self.v[-1]+self.a_oz[-1] * self.dt)
            self.x.append(self.x[-1]+self.v[-1]*self.dt)
            
        else:
            a_elast= np.sqrt(self.k/self.m)*dx
            self.a_oz.append(-self.g-np.sign(self.v[-1])*(self.rho*self.c*self.A/2*self.m)*self.v[-1]**2)

        a_f = -self.g + a_elast + self.a_oz[-1]

    def __jump(self):
        self.a =self.__move
        self.vi =+ self.vi + self.a
        self.x.append(self.x[-1]+self.vi*self.dt)
        self.t.append(self.t[-1]+self.dt)

