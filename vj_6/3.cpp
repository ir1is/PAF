#include <iostream>
#include <list>
#include <iterator>

using namespace std;

void polje(list <int> lista){

    list <int> :: iterator it;
    for(it = lista.begin(); it != lista.end(); ++it)
        cout << '\t' << *it;
    cout << '\n';
    
}

void interval(list<int> lista, int a, int b) {
    
    list <int> :: iterator it;
    for(it = lista.begin(); it != lista.end(); ++it)
        if (a <= *it && *it <= b) {
            cout << '\t' << *it;
        }
    cout << '\n'; 
}

int main() {

    list<int> lista;
    int a = 1;
    int b = 9;

    lista.push_back(3);
    lista.push_back(0);
    lista.push_back(5);
    lista.push_back(7);
    lista.push_back(2);
    lista.push_back(12);
    lista.push_back(4);

    cout << "\nOriginalna lista: ";
    polje(lista);

    cout << "\nElementi liste iz intervala [a,b]: ";
    interval(lista, a, b);

    cout << "\nLista nakon mijenjanja redoslijeda: ";
    lista.reverse();
    polje(lista);

    cout << "\nLista nakon zamjene 1. i 3. elementa: ";
    

    cout << "\nLista nakon sortiranja po velicini : ";
    lista.sort();
    polje(lista);

    return 0;
}
