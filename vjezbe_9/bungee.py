import math
import matplotlib.pyplot as plt

class BungeeJumping:
    def __init__(self,m,k,v0,h0,l,rho=1,Cd=1,A=1,dt=0.001,o_zr = True):
        self.m=m 
        self.k=k
        self.l=l
        self.h0=h0
        self.rho=rho 
        self.Cd=Cd
        self.A=A
        self.dt=dt
        self.o_zr=o_zr
        self.h=h0
        self.v0=0 
        self.t=0 
        self.h_=[]
        self.t_=[]
        self.h_.append(self.h)
        self.t_.append(self.t)
        self.U=self.m * 9.81 * self.h
        self.K=0 
        self.Ee=0
        self.E = self.U + self.K + self.Ee
        self.U_= []
        self.K_ = []
        self.Ee_ = []
        self.E_ = []
        self.U_.append(self.U)
        self.K_.append(self.K)
        self.Ee_.append(self.Ee)
        self.E_.append(self.E)

    def reset(self):
        self.m = 0
        self.k = 0
        self.l= 0
        self.h0= 0
        self.rho= 0
        self.Cd = 0
        self.A = 0
        self.dt =0
        del self.o_zr
        self.h =0
        self.v0 = 0
        self.t = 0
        self.h_ = []
        self.t_ = []
        self.U = 0
        self.K = 0 
        self.Ee =0
        self.E = 0
        self.U_ = []
        self.K_= []
        self.Ee_ = []
        self.E_ = []

    def akceleracija(self):
        dx = self.h0 - self.l - self.h
        if dx > 0:
            a_el = (self.k/self.m)*dx
        else: 
            a_el = 0
        if self.o_zr:
            a_AR = -(abs(self.v0)*self.v0*self.rho*self.Cd*self.A)/(2*self.m)
        else:
            a__AR = 0
        a = -9.81 + a_el + a_AR
        return a

    def energija(self):
        dx = self.h0 - self.l - self.h
        if dx > 0:
            self.Ee = (1/2)*self.k*dx**2
        else:
            Ee = 0
        self.U=self.m * 9.81 * self.h
        self.K = 0.5*self.m*(self.v0)**2
        self.E = self.U + self.K + self.Ee
        

    
    def __jump(self):
        self.a = self.akceleracija()
        self.v0 += self.a*self.dt
        self.h += self.v0*self.dt
        self.t += self.dt
        self.energija()

    def jump(self,t):
        while self.t < t:
            self.__jump()
            self.h_.append(self.h)
            self.t_.append(self.t)
            self.Ee_.append(self.Ee)
            self.K_.append(self.K)
            self.U_.append(self.U)
            self.E_.append(self.E)
   