import numpy as np

def derivacija(func,x,dx):
    return (func(x+ dx)-func(x))/dx

def three_point (func,x,dx):
    return ((func(x+dx))-(func(x-dx)))/(2*dx)


# def odredeni_integral(func,a,b,N):
#     dx = (b-a)/N
#     for i in range N:
#         liva =[]
#         liva = dx*(func(b))
