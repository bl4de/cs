#!/usr/bin/env python3
#
# Project Euler - Problem 25 solution
import time
import sys


def cached_fib(n, f_cache):
    if n in [1, 2]:
        sum = 1
    else:
        f_cache[n-1] = cached_fib(n-1, f_cache) if f_cache[n -
                                                           1] == 0 else f_cache[n-1]
        f_cache[n-2] = cached_fib(n-2, f_cache) if f_cache[n -
                                                           2] == 0 else f_cache[n-2]
        sum = f_cache[n-1] + f_cache[n-2]
    return sum


def fib(n):
    if n in [1, 2]:
        sum = 1
    else:
        sum = fib(n-1) + fib(n-2)
    return sum

# cached version of Fibonaci sequence for n elements
def measure_cached_fib(n):
    f_cache = [0] * n
    s = time.time()
    res = cached_fib(n, f_cache)
    # print some diagnostic output
    print("\n{}-th Fibonnaci number: {}".format(n, res))
    print("Length: {} digits".format(len(str(res))))
    t = time.time() - s
    print("measure_cached_fib() for {}: {:.10f} ms.\n".format(n, t))

# non-cached version of Fibonnaci sequence for n elements
def measure_fib(n):
    s = time.time()
    res = fib(n)
    print("\n{}-th Fibonnaci number: {}".format(n, res))
    print("Length: {} digits".format(len(str(res))))
    t = time.time() - s
    print("measure_fib() for {}: {:.10f} ms.\n".format(n, t))


n = int(sys.argv[1])
measure_cached_fib(n)

# Runs unbelievable slow when n > 35
measure_fib(n)
