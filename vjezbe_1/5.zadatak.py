import matplotlib.pyplot as plt

import numpy as np



def pravac(x1,y1,x2,y2):
    a=(y2-y1)/(x2-x1)
    b= y1 - a*x1 
    print('y=', a, 'x +', b)

    x = np.array([x1,y1])
    y = np.array([x2,y2])
    plt.plot(x,y)
    
    odgovor = input('ako želite prikazati graf upisite br 1, a ako želite spremiti u pdf upišite 2')
    if odgovor == '1':
        plt.show()
    elif odgovor =='2':
        plt.savefig(input('upisite ime pdf-a'))

pravac(2,4,5,2)





