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
    gamma_rate = ''
    epsilon_rate = ''
    # process data here...
    data = data.split('\n')
    bits_len = len(data[0])
    for pos in range(0, bits_len):
        for bits in data.split('\n'):

    return result


def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    result = 0
    # process data here...
    return result


# challenge input data
daily_input = pathlib.Path("./input.txt").read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
