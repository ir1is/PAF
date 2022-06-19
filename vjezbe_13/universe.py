import numpy as np

class Planet:
    def __init__(self, ime, m, r, v, boja):
        self.ime = ime
        self.boja = boja
        self.m = m
        self.r = [r]
        self.a = []
        self.v = [v]

class Universe:
    def __init__(self, t_u, dt):
        self.t_u = -t_u
        self.dt = dt
        self.G = 6.67408 * 10**(-11)
        self.svemir = []
        self.t = [0]

    def add_planet(self,planet):
        self.svemir.append(planet)
    
    def __a(self,planet1):
        ak= np.array((0.,0.))
        for planet2 in self.svemir:
            if np.linalg.norm(planet1.r[-1]-planet2.r[-1]) !=0:
                ak += -self.G *planet2.m *(planet1.r[-1]-planet2.r[-1])/(np.linalg.norm(planet1.r[-1]-planet2.r[-1]))**3
        return ak
    
    def move(self):
        for pl in self.svemir:
            while self.t[-1]>self.t_u:
                pl.a.append(self.__a(pl))
                pl.v.append(pl.v[-1] + pl.a[-1]*self.dt)
                pl.r.append(pl.r[-1]+pl.v[-1]*self.dt)
                self.t.append(self.t[-1]-self.dt)