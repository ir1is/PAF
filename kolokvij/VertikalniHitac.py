import numpy as np
class VertikalniHitac:
    def __init__(self,h0,v0):
        self.h0 = h0
        self.v0 = v0
        print('objekt uspješno stvoren, početna visina:',self.h0,'početna brzina:',self.v0)

    def promjena_visine(self,h0_new):
        self.h0 = h0_new
        return self.h0

        
    def promjena_brzine(self,v0_new):
        self.v0 = v0_new
        return self.v0

    def vertikalni(self,dt = 0.01):
        #self.theta = np.radians(theta)
        self.h = [self.h0]
        self.t = [0]
        self.vy =[self.v0]
        g = 9.81
        while self.h[-1]>0:
            self.vy.append(self.vy[-1]-g*dt)
            self.h.append(self.h[-1]+self.vy[-1]*dt)
            self.t.append(self.t[-1]+dt)
        return self.h,self.vy,self.t
    
    def max_h(self):
        while True:
            self.vertikalni()
            if self.vy[-1]<0:
                break
            return self.h[-1]

    def vrijeme_trajanja(self):
        self.vertikalni()
        t = self.t[1]
        return t

    def max_h_otporz(self,k):
        


