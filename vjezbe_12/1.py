from universe import Planet, Universe 
import numpy as np
au = 1.496e11

zemlja = Planet('zemlja',5.972e24,np.array((-1*au,0.)),np.array((0.,-29783)),'black')
sunce = Planet('sunce',1.989e30,np.array((0.,0.)),np.array((0.,0.)),'yellow')
merkur = Planet("Merkur", 3.3e24, np.array((0, 0.466*au)), np.array((-47362, 0)),'green')
venera =Planet("Venera", 4.8685e24, np.array((0.723*au, 0)), np.array((0, 35020)),'red')
mars = Planet("Mars", 6.417e23, np.array((0, -1.666*au)), np.array((24007, 0)),'gray')


svemir = Universe(5*365.242*3600*24,60*60*24)
svemir.add_planet(zemlja)
svemir.add_planet(sunce)
svemir.add_planet(merkur)
svemir.add_planet(venera)
svemir.add_planet(mars)
svemir.trajectory()