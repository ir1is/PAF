//i/o exapmle
#include <iostream>
#include <string>
using namespace std;

int main()
{   

    float x1, y1, x2, y2;
    cout << "x1: "; 
    cin >> x1; 
    cout <<'y1 : ';
    cin >> y1;
    cout <<'x2 : ';
    cin >> x2; 
    cout <<'y2 : ';
    cin >> y2;
    float a,b;
    a = (y2-y1)/(x2-x1);
    b = y1- a*x1;
    cout << "y="<<a<< "x +" << b << endl;
    return 0;
}