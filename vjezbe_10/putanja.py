import numpy as np
class Particle:
    def __init__(self,q,m,Ex,Ey,Ez,Bx,By,Bz,vx,vy,vz):
        self.q = q
        self.m = m
        self.E = np.array((Ex,Ey,Ez))
        self.B = np.array((Bx,By,Bz))
        self.v = np.array((vx,vy,vz))
        #self.a = np.array((0,0,0))
        self.r = np.array((0,0,0))
        self.t = 0
        self.x = [0]
        self.y = [0]
        self.z = [0]
        
    def __move(self,dt=0.01):
        self.t +=dt
        self.F = self.q*(self.E+ np.cross(self.v,self.B))
        self.a = self.F/self.m
        self.v += self.a*dt     
        #self.r += np.dot(self.v,dt)
        self.x.append(self.x[-1]+ self.v[0]*dt)
        self.y.append(self.y[-1]+ self.v[1]*dt)
        self.z.append(self.z[-1]+ self.v[2]*dt)
        # self.x.append(self.r[0])
        # self.y.append(self.r[1])
        # self.z.append(self.r[2])

    def move(self,t,dt=0.01):
        while self.t<t:
            self.__move(dt)
        return self.x,self.y,self.z


    def __a(self,v):
        return self.q/self.m*(self.E+np.cross(v,self.B))
    def __move_rk(self,dt=0.01):
        k1v = self.__a(self.v)*dt
        k1xyz = self.v*dt
        k2v = self.__a(self.v+0.5*k1v)*dt
        k2xyz = (self.v+k2v*0.5)*dt
        k3v = self.__a(self.v+0.5*k2v)*dt
        k3xyz = (self.v+k3v*0.5)*dt
        k4v = self.__a(self.v+k3v*0.5)*dt
        k4xyz = (self.v+k4v)*dt
        
        self.v += (k1v + 2*k2v + 2*k3v + k4v)/6
        self.x.append(self.x[-1] + (k1xyz[0] + 2*k2xyz[0] + 2*k3xyz[0] + k4xyz[0])/6)
        self.y.append(self.y[-1] + (k1xyz[1] + 2*k2xyz[1] + 2*k3xyz[1] + k4xyz[1])/6)
        self.z.append(self.z[-1] + (k1xyz[2] + 2*k2xyz[2] + 2*k3xyz[2] + k4xyz[2])/6)   
        self.t += dt

    def move_rk(self,t):
        while self.t<t:
            self.__move_rk()
            return self.x,self.y,self.z