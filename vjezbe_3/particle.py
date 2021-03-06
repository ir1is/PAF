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

    def plot_trajectory(self):
        self.range()
        plt.plot(self.x[:-1],self.y[:-1])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

    def total_time(self):
        while self.y[-1]>=0:
            self.__move()
        return (self.t[-1])
        
    def max_speed(self):
        max_speed_y=0
        while self.y[-1]>=0:
            self.__move()
        for el in self.vy:
            if el>max_speed_y:
                max_speed_y=el
        return np.sqrt((max_speed_y)**2+(self.vx[-1])**2)

#zadatak 2
    def ovisnost_dometa(self,v0,x,y):
        kut = 0
        kutevi= []
        domet = []
        while kut <= 90:
            self.reset()
            self.set_initial_conditions(x,y,kut,v0)
            kutevi.append(kut)
            domet.append(self.range())
            kut += 0.01
        plt.plot(kutevi, domet)
        plt.xlabel('kut')
        plt.ylabel('domet')
        plt.show()

    def ovisnost_vremena(self,v0,x,y):
        tok_vremena=[]
        kutevi= []
        kut = 0
        while kut<=90:
            self.set_initial_conditions(x,y,kut,v0)
            kutevi.append(kut)
            tok_vremena.append(self.total_time())
            kut += 0.1
            self.reset()
        plt.plot(kutevi,tok_vremena)
        plt.show()


