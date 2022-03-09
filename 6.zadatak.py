import matplotlib.pyplot as plt
import math

def udaljenost(tx,ty,ix,iy,r):
    kruznica = plt.Circle((ix,iy),r, fill=False)
    ax = plt.subplot()
    ax.add_patch(kruznica)
    ax.plot(tx,ty)
    T = [tx,ty]
    O = [ix,iy]
    d = math.dist(T,O) - r
    if d<0:
        print('točka se nalazi unutar kružnice')
        print('udaljenost je:', abs(d) )
    elif d==0:
        print('točka je na kružnici')
    else:
        print('točka je van kružnice')
        print('udaljenost od kružnice je:',d)
    
    odgovor= input('ako želite prikazati kao sliku upisite 1, ako želite spremiti u pdf upisite 2!')
    if odgovor=='1':
        plt.show()
    elif odgovor=='2':
        ime = input('kako želite da se zove pdf file? ')
        plt.savefig(ime)



udaljenost(2,3,4,3,2)
    
    
