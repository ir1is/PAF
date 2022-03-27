import calculus as cl 
import numpy as np

def f2(x):
    return x**3

def f3(x):
    return np.sin(x)
    
#print(cl.derivacija(f2,2,0.01))
print(cl.derivacija(f3,3,0.01))