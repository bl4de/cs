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
    decreased = 0
    increased = 0
    prev_val = 0
    for measurement in data.split('\n'):
        measurement = int(measurement)
        if prev_val != 0 and measurement > prev_val:
            increased += 1
        else:
            decreased += 1
        prev_val = measurement

    result = increased
    # process data here...
    return result


def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    result = 0
    # process data here...
    return result


# challenge input data
input_data = pathlib.Path("./input.txt").read_text('utf-8').strip()

# Part 1. solution
print(part_one_solution(input_data))

# Part 2. solution
print(part_two_solution(input_data))
