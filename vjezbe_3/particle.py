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

    def reset(self):
        self.__init__()
    

    def __move(self):
        self.dt = 0.1
        self.t.append(self.t[-1]+ self.dt)
        self.vy.append(self.vy[-1]-self.ay[-1] * self.dt)
        self.vx.append(self.vx[-1]+self.ax[-1] * self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
        #print(self.vy)
    def range(self):
        while self.y[-1]>=0:
            self.__move()
            #print(self.y[-1])
        return self.x[-1]

    def plot_trajectory(self):
        self.listaX = []
        self.listaY = []

        self.__move()
        for i in self.y:
            if i>0:
                self.listaX.append(i)
                self.listaY.append(i)
            elif i<0:
                break
            plt.plot(self.listaX,self.listaY)
            plt.show()
            

