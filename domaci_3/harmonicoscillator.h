#include <iostream>

class HarmonicOscillator {

public: 

        double t,x,v,a,dt;

        HarmonicOscillator(double x0,double y0,double k, double m);


        ~HarmonicOscillator();

        void titranje(double t_f);
}
;