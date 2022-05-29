import numpy as np

class Gravitacija:
    def __init__(self):
        self.ms = 0
        self.mz = 0
        self.xs = []
        self.ys = 0
        self.xz = []
        self.yz = 0
        self.vxs = 0
        self.vys = 0
        self.vxz = 0
        self.vyz = 0
        
        
    def set_init(self,ms,mz,xs,ys,xz,yz,vxs,vys,vxz,vyz):
        self.ms = ms
        self.mz = mz
        self.xs.append(xs)
        self.ys = yz
        self.xz.append(xz)
        self.yz = yz
        self.vxs = vxs
        self.vys = vys
        self.vxz = vxz
        self.vyz = vyz
        self.v_s.append(np.sqrt(vxs**2+vys**2))
        self.v_z.append(np.sqrt(vxz**2+vyz**2))

    def a_s(self):
        return -9.81*(self.ms/(self.xs[-1]-self.xz[-1])**2)
    def a_z(self):
        return -9.81*(self.mz/(self.xs[-1]-self.xz[-1])**2)


    def move(self,dt =0.01):
        self.v_s.append(np.sqrt( (self.vxs + self.a_s*dt)**2+(self.vys+self.a_s*dt)**2))
        self.r_s.append(self.xs[-1] + self.v_s[-1])
        self.v_z.append(np.sqrt( (self.vxz[-1] +self.a_z*dt)**2+(self.vyz[-1]+self.a_z*dt)**2))
        self.r_z.append(self.xz[-1] + self.v_z[-1])

