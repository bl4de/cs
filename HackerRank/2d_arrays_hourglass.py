#!/usr/bin/env python3

import math
import os
import random
import re
import sys

# Given a  2D Array, :
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

# a b c
#   d
# e f g

# There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.

# Task :

# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

# sample input:

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

# sample output:
# 19

# -1 -1 0 -9 -2 -2
# -2 -1 -6 -8 -2 -5
# -1 -1 -1 -2 -3 -4
# -1 -9 -2 -4 -4 -5
# -7 -3 -3 -2 -9 -9
# -1 -3 -1 -2 -4 -5

# -6

if __name__ == '__main__':

    # define 'hourglass' matrix as a relative coords
    # from starting [row,col] of hourglass:
    hourglass = [
        (0, 0), (0, 1), (0, 2),     # 1 1 1
        (1, 1),                     # 0 1 0
        (2, 0), (2, 1), (2, 2)      # 1 1 1
    ]

    arr = []

    # take the input:
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # taking each row and cols from 0 to 3 as a start
    # position, we "apply" our hourglass and calculate
    # the sum of all cells as midsum
    # max is the hightest midsum found across all possible
    # hourglasses:

    max = None
    midsum = 0
    
    # time complexity: O(n^2):
    for row in range(0, 4):
        for col in range(0, 4):
            # arr[row][col] is a starting position
            for (x, y) in hourglass:
                midsum = midsum + (arr[row + x][col + y])
                if max is None:
                    max = midsum
            
            if midsum > max:
                max = midsum

            midsum = 0

    print(max)
