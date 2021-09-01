#include <iostream>

using namespace std;

// x(n) = (x-1) + (x-2)
int fibo(int x) {
	return (x < 2) ? x  : fibo(x-1) + fibo(x-2);
}

int main(int argc, char* argv[]) {
	cout << fibo( atoi(argv[1]) ) << endl;

}