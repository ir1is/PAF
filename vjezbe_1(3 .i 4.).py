#3. zadatak
while True:
    x1 = (input('upisi x koordinatu 1. točke: '))
    y1 = (input('upisi y koordinatu 1. točke: '))
    x2 = (input('upiši x koordinatu 2. točke: '))
    y2 = (input('upiši y koordinatu 2. točke: '))
    try: 
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        break;
    except:
        print('unesite numericku vrijednost')



#4. zadatak
a = (y2-y1)/(x2-x1)
b = y1 - a*x1
print('y=',a,'x+', b)


def pravac(x1,y1,x2,y2):
    a=(y2-y1)/(x2-x1)
    b= y1 - a*x1 
    print('y=', a, 'x +', b)

pravac(2,3,1,5)

