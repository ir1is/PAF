import numericko_rac as num

def F_const(v,x,t):
    return 1

def F1(v,x,t):
    k=3
    return -k*x

#print(num.gibanje(F_const,2,10))
print(num.gibanje(F1,2,10,2,2))