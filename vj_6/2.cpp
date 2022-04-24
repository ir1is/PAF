#include <iostream>
#include <cmath>
void  kruznica(int x1,int y1,int x2,int y2,int r)
{
    float d_korijen;
    d_korijen = pow((x1-x2),2) + pow((y1-y2),2);
    float d;
    d = sqrt(d_korijen);
    float diff = 0.01;
    if (d<r){
        std::cout << "Točka je unutar kružnice" << std::endl;
    }
    else if ( r-diff < d < r+diff){
        std::cout << "Točka je na kružnici" << std::endl;
    }
    else{
        std::cout << "Točka je van kružnice" << std::endl;
    }
}
int main(){
    kruznica(2,3,0,3,1);
    return 0;
}