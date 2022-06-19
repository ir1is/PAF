from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x = np.array([[]])
y = np.array([[]])
lines = []
colors = []
lc = LineCollection(lines, cmap="viridis", lw=4)
ax.add_collection(lc)
class Planet:
    def _init_(self,planet,m,r0,v0,boja):
        self.planets = [planet]
        self.m = m
        self.r = [r0]
        self.x = [r0[0]]
        self.y =[r0[1]]
        self.v = v0
        self.boja = boja

class Universe:
    def _init_(self,time,dt):
        self.time = time
        self.dt = dt
        self.G = 6.67408 (10*(-11))
        self.universe = []
        self.t = [0]

    def add_planet(self,planet):
        self.universe.append(planet)
    
    def __a(self,planet1):
        ak= np.array((0.,0.))
        for planet2 in self.universe:
            if np.linalg.norm(planet1.r[-1]-planet2.r[-1]) !=0:
                ak += -self.G *planet2.m *(planet1.r[-1]-planet2.r[-1])/(np.linalg.norm(planet1.r[-1]-planet2.r[-1]))*3
        return ak
    
    def move(self):
        for pl in self.universe:
            a = self.__a(pl)
            pl.v = pl.v + a*self.dt
            pl.r.append(pl.r[-1]+pl.v*self.dt)
            pl.x.append(pl.r[-1][0])
            pl.y.append(pl.r[-1][1])
            self.t.append(self.t[-1]+self.dt)
            
    def trajectory(self):
        while self.t[-1]<self.time:
            self.move()
        for pl in self.universe:
            plt.plot(pl.x,pl.y,color= pl.boja)
        plt.show()

    def animate(self):
        global x, y, colors
        while self.t[-1]<self.time:
            self.move()
        x = []
        y = []
        for pl in self.universe:
            x.append(pl.x)
            y.append(pl.y)
        l = len(x[0])
        x = np.array(x)
        y = np.array(y)
        colors = np.arange(1, len(self.universe) + 1, 1)
        a = FuncAnimation(fig,dodaj,x.shape[1],interval=l,init_func=postavi,blit=True)
        plt.show()
def postavi():
    ax.set_xlim(-3*(10*11),3(10**11))
    ax.set_ylim(-6*(10*11),6(10**11))
    return lc,
def dodaj(num):
    new_x = x[:, :num]
    new_y = y[:, :num]
    lines = [np.column_stack([xi, yi]) for xi, yi in zip(new_x, new_y)]
    lc.set_segments(lines)
    lc.set_array(colors)
    return lc,
