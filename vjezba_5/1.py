import harmonic_oscillator as ho
import matplotlib.pyplot as plt

ho1 = ho.HarmonicOscillator()
# ho1.set_initial_conditions(0,4,41,10)
# ho1.plotanje()


#preciznost


dt_lista= [0.5,0.1,0.05]
for i in dt_lista:
    ho1.set_initial_conditions(1,2,41,10,dt=i)
    ho1.oscillation()
    plt.scatter(ho1.t,ho1.x)
    ho1.reset()
plt.show()


