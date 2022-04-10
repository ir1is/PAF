import harmonic_oscillator as ho
import matplotlib.pyplot as plt
import numpy as np
objekt = ho.HarmonicOscillator()
objekt.set_initial_conditions(1,3,10,3)
dt=[]
period =[]
period_analiticki = []

for i in range (1,100):
    period_analiticki.append(2*np.pi/objekt.kutna_frek)
    dt.append(i/1000)
    period.append(objekt.t_titranja(dt[-1]))
    objekt.reset()
plt.plot(dt,period)
plt.plot(dt,period_analiticki)
plt.show()


