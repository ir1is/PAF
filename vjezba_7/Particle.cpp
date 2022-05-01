#include <Particle.h>
#include <math.h>
Particle::Particle(double v,double theta, double x0, double y0,double step)
{x =x0;
y = y0;
vx = v*cos(theta * (M_PI/180));
vy = v*sin(theta* (M_PI/180));
t = 0;
dt = step;
}
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
    evolve();
    return x;
}
double Particle::time()
{
    evolve();
    return t;
}
