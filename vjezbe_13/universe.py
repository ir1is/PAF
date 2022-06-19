from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
fig,ax = plt.subplots()
x = []
y = []
ln,=plt.plot([],[],label='svemir')
class Planet:
    def __init__(self,planet,m,r0,v0,boja):
        self.planets = [planet]
        self.m = m
        self.r = [r0]
        self.x = [r0[0]]
        self.y =[r0[1]]
        self.v = v0
        self.boja = boja

class Universe:
    def __init__(self,time,dt):
        self.time = time
        self.dt = dt
        self.G = 6.67408 *(10**(-11))
        self.universe = []
        self.t = [0]

    def add_planet(self,planet):
        self.universe.append(planet)
    
    def __a(self,planet1):
        ak= np.array((0.,0.))
        for planet2 in self.universe:
            if np.linalg.norm(planet1.r[-1]-planet2.r[-1]) !=0:
                ak += -self.G *planet2.m *(planet1.r[-1]-planet2.r[-1])/(np.linalg.norm(planet1.r[-1]-planet2.r[-1]))**3
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
        while self.t[-1]<self.time:
            self.move()
        a =[]
        for pl in self.universe:
            f = []
            for i in range(len(pl.x)):
                f.append([pl.x[i],pl.y[i],pl.boja])

            a.append(FuncAnimation(fig,dodaj,init_func=postavi,blit=True,frames=f))
        plt.show()
def postavi():
    ax.set_xlim(-6*(10**11),6*(10**11))
    ax.set_ylim(-3*(10**11),3*(10**11))
    return ln,
def dodaj(frame):
    x.append(frame[0])
    y.append(frame[1])
    a =plt.plot(x,y,color=frame[2])
    #ln.set_data(x,y)
    return a
        