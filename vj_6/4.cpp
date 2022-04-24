#include <iostream>
#include <string>
using namespace std;
int main()
{
    float a1,b1,c1,a2,b2,c2;
    cout<< "a1: ";
    cin >> a1;
    cout << "b1: ";
    cin >> b1;
    cout<< "c1: ";
    cin >> c1;
    cout<< "a2: ";
    cin >> a2;
    cout<< "b2: ";
    cin >> b2;
    cout<< "c2: ";
    cin >> c2;
    float x,y ;
    y= (c2/a2-c1/a1)/(b2/a2-b1/a1);
    x = (c1-y*b1)/a1;
    cout <<"(x,y) =("<< x <<","<<y<<")"<< endl;
    return 0;
}