import matplotlib.pyplot as plt
ho_file = open('ho.txt')
ho = ho_file.readlines()
ho_file.close()
 
x_l= []
t_l=[]
v_l = []
a_l=[]
for line in ho:
    t_l.append(line.split(',')[0])
    x_l.append(line.split(',')[1])
    v_l.append(line.split(',')[2])
    a_l.append(line.split(',')[3])
fig,(p1,p2,p3)=plt.subplots(1,3)
p1.plot(x_l,t_l)
p2.plot(v_l,t_l)
p3.plot(a_l,t_l)
plt.show()