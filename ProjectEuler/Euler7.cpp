#include <iostream>


using namespace std;

int main() {
    int i = 0;
    int number = 6;
    while ( i < 9999 ) {
        if ( number % 2 == 0 || number % 3 == 0 || number % 5 == 0 ) {
            // to nie jest liczba pierwsza
        } else {
            i++;
            cout<<i<<" prime number is "<<number<<endl;
        }
        number++;
    }
    
    cout<<"10001 prime factor is "<<number<<endl;
    return 0;
}