import harmonic_oscillator as ho
import matplotlib.pyplot as plt

ho1 = ho.HarmonicOscillator()
ho1.set_initial_conditions(0,4,41,10)
#ho1.plotanje(10)
#preciznost

ho1.reset()
dt_lista= [0.5,0.1,0.05]
for i in dt_lista:
    ho1.oscillation(10,i)
    plt.scatter(ho1.t,ho1.x)
    ho1.reset()
plt.show()


