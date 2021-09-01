#!/usr/bin/env python

# pentagonal numbers formula: n(3n−1)/2


def generate(n):
    return n * (3 * n - 1) / 2


if __name__ == "__main__":
    for i in range(1, 11):
        print "wynik dla {}: {}".format(i, generate(i))
