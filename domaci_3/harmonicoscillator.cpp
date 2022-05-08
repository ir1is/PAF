#include <harmonicoscillator.h>
#include <iostream>
#include <fstream>
#include <math.h>

HarmonicOscillator::HarmonicOscillator(double x0,double v0, double k,double m)
{
    t = 0;
    x = x0;
    v = v0;
    a = sqrt(k/m);
    dt = 0.01;
}

void HarmonicOscillator::titranje(double t_f)
{
    double t_lista [int(t_f/dt)+1];
    double x_lista [int(t_f/dt)+1];   
    double v_lista [int(t_f/dt)+1];
    double a_lista [int(t_f/dt)+1];
int i = 0;
while (t <= t_f){
    t = t+dt;
    a = sqrt(k/m)*x;
    v = v+a*dt;
    x = x+ v*dt;
    t_lista[i] = t;
    a_lista[i] = a;
    v_lista[i] = v;
    x_lista[i] = x;
i ++ ;
}
ofstream ho_file;
ho_file.open("ho.txt");
for (int j=0; j<i;j++)
{
    ho_file << t_lista[j] << ","<< x_lista[j] << ","<< v_lista[j] << "," << a_lista[j] << "\n";
}
ho_file.close();
}
