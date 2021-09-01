#include <iostream>

using namespace std;

unsigned long int MacCarthy(int x) {
	static int count = 0;

	count++;
	if (x > 100) {
		cout<<"\ncount: "<< count;
		return x-10;
	} else {
		cout<<"\ncount: "<< count;
		return MacCarthy( MacCarthy(x+11) );
	}
}
int main(int argc, char* argv[]) {

	MacCarthy( atoi(argv[1]));

	return 0;
}