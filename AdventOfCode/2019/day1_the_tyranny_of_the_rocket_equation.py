#!/usr/bin/env python3
# AdventOfCode Challenge Template
#
# https://adventofcode.com/events
#

from math import floor
import pathlib


def part_one_solution(data) -> int:
    '''
        Solution for Part 1.
    '''
    fuels = list(data.split('\n'))
    fsum = 0
    for fuel in fuels:
        fuel = (floor(int(fuel)/3)) - 2
        fsum += fuel
    # process data here...
    return fsum


def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    result = 0
    # process data here...
    return result


# challenge input data
data = pathlib.Path("./input.txt").read_text().strip()

# Part 1. solution
print(part_one_solution(data))

# Part 2. solution
print(part_two_solution(data))
