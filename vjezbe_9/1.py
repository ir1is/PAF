from bungee import BungeeJumping
import matplotlib.pyplot as plt
BJ=BungeeJumping(100,20,0,250,50,False)
BJ.jump(50)

plt.figure("Bungee jumping", figsize=(15, 10), dpi=80)
fig = plt.subplot()

plt.subplot(2,2,1)
plt.plot(BJ.t_,BJ.h_)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("Graf bez otpora zraka")
#plt.show()

plt.subplot(2,2,2)
plt.plot(BJ.t_, BJ.E_, label = "ukupna energija")
plt.plot(BJ.t_, BJ.K_, label = "kineticka energija")
plt.plot(BJ.t_, BJ.U_, label = "potencijalna energija")
plt.plot(BJ.t_, BJ.Ee_, label = "elasticna energija")
plt.title("Energija bez otpora zraka")
plt.legend(loc = "upper right", prop={'size': 10} )
#plt.show()

BJ.reset()

BJ=BungeeJumping(100,20,0,250,50,True)    
BJ.jump(50)

plt.subplot(2,2,3)
plt.plot(BJ.t_,BJ.h_)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("Graf s otporom zraka")
#plt.show()

plt.subplot(2,2,4)
plt.plot(BJ.t_, BJ.E_, label = "ukupna energija")
plt.plot(BJ.t_, BJ.K_, label = "kineticka energija")
plt.plot(BJ.t_, BJ.U_, label = "potencijalna energija")
plt.plot(BJ.t_, BJ.Ee_, label = "elasticna energija")
plt.title("Energija s otporom zraka")
plt.legend(loc = "upper right", prop={'size': 10} )
plt.show()