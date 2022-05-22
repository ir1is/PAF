import numpy as np
import matplotlib.pyplot as plt


class Bungee:
    def __init__(self):
        self.x = []
        self.E =[]
        self.t = []
        self.g =9.81
        self.U = []
        self.C = 0
        self.A = 0
        self.v = []
        self.a_oz = []
        self.a = 0
        self.kin =  []
        self.poten = []
        self.elasticna = []
    def set_init(self,vi,k,m,h,l,rho,C,A,q,xi,o_z=True,dt=0.1):
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
        self.v.append(vi)
        self.dt = dt
        self.kin.append(0)
        self.poten.append(m*self.g*h)
        self.elasticna.append(0)

    def __move(self):
        dx = self.h-self.l-self.x[-1]
        self.t.append(self.t[-1]+ self.dt)
        if dx<0:
            a_elast = 0
        else:
            a_elast= np.sqrt(self.k/self.m)*dx
        self.a_oz.append(-self.g-np.sign(self.v[-1])*(self.rho*self.C*self.A/2*self.m)*self.v[-1]**2)
       
        a_f = -self.g + a_elast + self.a_oz[-1]
        self.v.append(self.v[-1]+a_f * self.dt)
        self.x.append(self.x[-1]+self.v[-1]*self.dt)
        self.kin.append(0.5*self.m*self.v[-1]**2)
        self.poten.append(self.m*self.g*(self.h-self.x[-1]))
        self.elasticna.append(0.5*self.k*dx**2)
    
    def __jump(self,trajanje):
        while self.t[-1]<trajanje:
            self.__move()

    def plotanje(self):
        self.__jump(50)
        fig,(p1,p2,p3)=plt.subplots(1,3)
        p1.plot(self.t,self.poten)
        p2.plot(self.t,self.kin)
        p3.plot(self.t,self.elasticna)
        plt.show()
    