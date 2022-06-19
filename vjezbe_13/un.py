import numpy as np

G = 6.67408*10**(-11)
godina = 365.242*24*60*60

class Planet:
    def __init__(self, m, x0, y0, v0, r):
        self.m = m
        self.v0 = v0
        self.x0 = x0
        self.y0 = y0
        self.r = r
        if self.y0 == 0:
            if self.x0>0:
                self.kut = 0
            else:
                self.kut = -np.pi
        else:
            self.kut = np.arctan(self.x0/self.y0)
        self.x = [self.x0]
        self.y = [self.y0]
        self.v = np.array([self.v0*np.sin(self.kut), self.v0*np.cos(self.kut)])
        self.a = np.array([0., 0.])

    def reset(self):
        self.x = [self.x0]
        self.y = [self.y0]
        self.v = np.array([self.v0*np.sin(self.kut), self.v0*np.cos(self.kut)])
        self.a = np.array([0., 0.])

class Universe:
    def __init__(self):
        self.svemir = []
        self.t = 0
    def add_planet(self, planet):
        self.svemir.append(planet)

    def move(self):
        for pl in self.svemir:
            F = np.array([0.,0.])
            for pl2 in self.svemir:
                if pl2 != pl:
                    