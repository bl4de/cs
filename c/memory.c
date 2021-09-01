#include <stdlib.h>
#include <stdio.h>

int sum(int a, int b) {
    int s = a + b;
    return s;
}

int main(int argc, char* argv[]) {
    int x = 10;
    int y;

    y = 20;

    int s = sum(x,y);
    printf("The sum of %d and %d = %d\n", x, y, s);

    exit(0);
}
