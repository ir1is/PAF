import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self):
        self.t = []
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ay =[]
        self.ax = []
        
    def set_initial_conditions(self,x0,y0,kut,v0,p,c,A,m):
        self.t.append(0)  
        self.x.append(x0)
        self.y.append(y0)
        self.v_x = v0 * np.cos(np.radians(kut))
        self.v_y = v0 * np.sin(np.radians(kut))
        self.vx.append(self.v_x)
        self.vy.append(self.v_y)
        self.a_x = 0
        self.a_y = 9.81
        self.ay.append(self.a_y)
        self.ax.append(self.a_x)
        self.g = 9.81
        self.dt = 0.01
        self.p = p
        self.c = c
        self.A = A 
        self.m = m

    def reset(self):
        self.__init__()
    
    
    def __move(self):
        self.t.append(self.t[-1]+ self.dt)
        self.ax.append(-np.sign(self.vx[-1])*(self.p*self.c*self.A/2*self.m)*self.vx[-1]**2)
        self.ay.append(-self.g-np.sign(self.vy[-1])*(self.p*self.c*self.A/2*self.m)*self.vy[-1]**2)
        self.vy.append(self.vy[-1]+self.ay[-1] * self.dt)
        self.vx.append(self.vx[-1]+self.ax[-1] * self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
        
        
    def range(self,dt):
        while self.y[-1]>=0:
            self.__move()
        return self.x[-1]

    def plot_trajectory(self):
        self.range()
        plt.plot(self.x[:-1],self.y[:-1])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

    def a_rk(self,x,v,t):
        return -1*np.sign((v*self.p*self.c*self.A/2*self.m)*v**2)


    def runge_kutta(self):
        i=0
        while self.y[i]>=0:

            self.t.append(self.t[i-1]+self.dt)
            k1vx = (self.a_rk(self.x[i-1],self.vx[i-1],self.t[i-1]))*self.dt
            k1x = self.vx[i-1]*self.dt
            k1vy = (-self.g + self.a_rk(self.x[i-1],self.vx[i-1],self.t[i-1]))*self.dt
            k1y = self.vy[i-1]*self.dt
            
            k2vx = (self.a_rk( self.x[i-1]+k1vx/2, self.vx[i-1]+k1vx/2,self.t[i-1]+self.dt/2))*self.dt
            k2x = (self.vx[i-1]+k1vx/2)*self.dt
            k2vy = (-self.g + self.a_rk( self.y[i-1]+k1vy/2, self.vy[i-1]+k1vy/2,self.t[i-1]+self.dt/2))*self.dt
            k2y = (self.vy[i-1]+k1vy/2)*self.dt

            k3vx = (self.a_rk(self.x[i-1]+k2vx/2,self.vx[i-1]+k2vx/2,self.t[i-1]+self.dt/2))*self.dt 
            k3x = (self.vx[i-1]+k2vx/2)*self.dt
            k3vy = (-self.g + self.a_rk(self.y[i-1]+k2vy/2,self.vy[i-1]+k2vy/2,self.t[i-1]+self.dt/2))*self.dt 
            k3y = (self.vy[i-1]+k2vy/2)*self.dt

            k4vx = (self.a_rk(self.x[i-1]+k3vx/2,self.vx[i-1]+k3vx/2,self.t[i-1]+self.dt/2))*self.dt
            k4x = (self.vx[i-1]+k3vx/2)*self.dt
            k4vy = (-self.g + self.a_rk( self.y[i-1]+k3vy/2, self.vy[i-1]+k3vy/2,self.t[i-1]+self.dt/2))*self.dt
            k4y = (self.vy[i-1]+k3vy/2)*self.dt

            self.vx.append(self.vx[i-1] +1/6*(k1vx + 2*k2vx + 2*k3vx +k4vx))
            self.vy.append(self.vy[i-1] +1/6*(k2vy + 2*k2vy + 2*k3vx +k4vy)) 

            self.x.append(self.x[i-1]+1/6*(k1x + 2*k2x + 2*k3x +k4x))
            self.y.append(self.y[i-1]+1/6*(k1y + 2*k2y + 2*k3y +k4y))
            i+=1
            print(self.x)
            return self.x,self.y
            