//i/o exapmle
#include <iostream>
#include <string>
using namespace std;

int main()
{   

    float x1, y1, x2, y2;
    cout << "upisi x koordinatu 1. točke "; 
    cin >> x1; 
    cout <<'upisi y koordinatu 1. točke: ';
    cin >> y1;
    cout <<'upiši x koordinatu 2. točke: ';
    cin >> x2; 
    cout <<'upisi y koordinatu 2. točke: ';
    cin >> y2;
    float a,b;
        a = (y2-y1)/(x2-x1)
b = y1- a*x1
print('y=',a,'x','+',b)