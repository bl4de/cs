#include <iostream>

using namespace std;

long silnia(long x) {
	if (x == 0) {
		return 1;
	}
	return x * silnia(x-1);
}

int main(int argc, char* argv[]) {
	cout << silnia( atoi(argv[1]) ) << endl;	
	return 0;
}

