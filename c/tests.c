#include <stdio.h>
#include <stdlib.h>

int main() {
    int a = 10, b = 20;
    int how_many_bytes;

    printf("This is how many bytes: XX%n; address of a: %.4x, value of b: %.4x, value of c: %x\n", &how_many_bytes, a, b, how_many_bytes);

    printf("bytes: %d", how_many_bytes);

    exit(0);
}