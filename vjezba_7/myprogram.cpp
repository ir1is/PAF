#include <Particle.h>
#include <iostream>
//#include "Particle.h"

using namespace std;
int main()
{
    Particle p1(100,45,0,0,0.001);
    Particle p2(10,60,0,0);
    cout << p1.range()<< endl;
    cout <<p1.time()<< endl;
    cout << p2.range()<< endl;
    cout <<p2.time()<< endl;
    return 0;
    }
