#!/usr/bin/env python3
'''
AdventOfCode Challenge Template
https://adventofcode.com/events
'''

import pathlib


def part_one_solution(data) -> int:
    '''
        Solution for Part 1.
    '''
    data = data.split('\n')
    result = 0

    # process data here...

    return result


def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    data = data.split('\n')
    result = 0

    # process data here...

    return result


DEBUG = True  # False

# read challenge input data
if DEBUG:
    INPUT_PATH = "test_input.txt"
else:
    INPUT_PATH = "input.txt"

daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
