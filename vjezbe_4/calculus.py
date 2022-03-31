import numpy as np

#prva metoda
def two_point(func,x,dx=0.001):
    return (func(x+ dx)-func(x))/dx

def three_point (func,x,dx=0.001):
    return ((func(x+dx))-(func(x-dx)))/(2*dx)

def derivacija(func,x,dx=0.001,vrsta='three_point'):
    if vrsta=='three_point':
        return three_point(func,x,dx)
    else:
        return two_point(func,x,dx)

#druga metoda

def derivacija_na_rasponu(func,gornja_granica,donja_granica,dx=0.02):
    x = [donja_granica]
    y = [three_point(func,x[-1],dx)]
    while x[-1]<gornja_granica:
        y.append(three_point(func,x[-1],dx))
        x.append(x[-1]+dx)
        #y.append(three_point(func,x[-1],dx))
        print(y)
    return x,y

#zad2, prva metoda
def integral(func,a,b,N):
    dx = (b-a)/N
    gornja_m =0
    donja_m =0 
    for i in range(N):
        donja_m += (func(a +i*dx))*dx
        gornja_m += (func(a+(i+1)*dx))*dx
    return donja_m, gornja_m

#zad2, druga metoda
def trapez(func,a,b,N):
    dx=(b-a)/N
    integral =0
    for i in range(N):
        lijeva_visina = func(a +i*dx)
        desna_visina = func(a +(i+1)*dx)
        pravokutnik = lijeva_visina * dx
        trokut = ((desna_visina- lijeva_visina) * dx)/2
        integral += pravokutnik+trokut
    return integral 

         



