import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join(w[0].upper() + w[1:] for w in s.split(' '))

if __name__ == '__main__':
    s = input()
    print(solve(s))    
