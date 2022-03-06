x1 = int(input('upisi x koordinatu 1.točke: '))
y1 = int(input('upisi y koordinatu 1. točke: '))
x2 = int(input('upiši x koordinatu 2. točke: '))
y2 = int(input('upiši y koordinatu 2. točke: '))
a = (y2-y1)/(x2-x1)
b = y1 - a*x1
print('y=',a,'x+', b)


def pravac(x1,y1,x2,y2):
    a=(y2-y1)/(x2-x1)
    b= y1 - a*x1 
    print('y=', a, 'x +', b)

pravac(2,3,1,5)
