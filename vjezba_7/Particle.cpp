#include <Particle.h>
#include <math.h>
void Particle::evolve()
{
    while(y>=0)
    {
        vx += 0.;
        vy += g*dt;
        x += vx*dt;
        y += vy*dt;
        t += dt;

    }
}
double Particle::range()
{
    while(y>=0)
    evolve();
    return x;
        
}

Particle::Particle(double v,double theta, double x0, double y0,double step)
{10,40,0,0;}