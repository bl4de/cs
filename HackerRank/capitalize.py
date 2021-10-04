import math
import os
import random
import re
import sys

def solve(s):
    # first character is always upper:
    uppercased = s[0].upper()
    
    # every character precede by spase is also uppercased:
    for iterator in range(1, len(s)):
        if s[iterator - 1] == ' ' and s[iterator] != ' ':
            uppercased += s[iterator].upper()
        else:
            uppercased += s[iterator]
        iterator += 1
    return uppercased 

if __name__ == '__main__':
    s = input()
    print(solve(s))    
