import numpy as np
import math
import matplotlib.pyplot as plt

class Gravitacija:
    def __init__(self,xs,ys,xz,yz,vxs,vys,vxz,vyz):
        self.mz = 5.972*(10**24)
        self.ms = 1.9891*(10**30)
        self.r_s = np.array((xs,ys))
        self.r_z = np.array((xz,yz))
        self.v_s=np.array((vxs,vys))
        self.v_z=np.array((vxz,vyz))
        self.G = 6.67426*(10**(-11))
        self.godina = 365.242*24*3600
        self.xs = [xs]
        self.xz =[xz]
        self.ys = [ys]
        self.yz = [yz]
        self.t = 0
    def a_s(self):
        return -self.G*(self.mz/(np.linalg.norm(self.r_s-self.r_z))**3)*(self.r_s-self.r_z)
    
    def a_z(self):
        return -self.G*(self.ms/(np.linalg.norm(self.r_z-self.r_s))**3)*(self.r_z-self.r_s)

    def move(self,dt =86400):     
        self.v_s = self.v_s+self.a_s()*dt
        self.r_s =(self.r_s + self.v_s*dt)
        self.v_z =self.v_z+self.a_z()*dt
        self.r_z =self.r_z+self.v_z*dt
        self.xs.append(self.r_s[0])
        self.ys.append(self.r_s[1])
        self.xz.append(self.r_z[0])
        self.yz.append(self.r_z[1])
        self.t+=dt

    def trajectory(self):
        while self.t<self.godina:
            self.move()
        # plt.plot(self.xs,self.ys,label='sunce')
        # plt.plot(self.xz,self.yz, label ='zemlja')
        figs,(p1,p2)=plt.subplots(1,2)
        p1.plot(self.xs,self.ys)
        p2.plot(self.xz,self.yz,label='zemlja')
        plt.legend()
        plt.show()
        


