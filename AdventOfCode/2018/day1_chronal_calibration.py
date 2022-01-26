#!/usr/bin/env python3
# AdventOfCode Challenge Template
#
# https://adventofcode.com/events
#

import pathlib


def part_one_solution(data) -> int:
    '''
        Solution for Part 1.
    '''
    result = 0
    # process data here...
    for frequency in data.split('\n'):
        result += int(frequency)
    return result


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
