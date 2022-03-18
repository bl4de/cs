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
    pos_x = 0  # starting point X
    pos_y = 0  # starting point Y
    visited = [(pos_x, pos_y)]
    for direction in data:
        if direction == '^':
            pos_x -= 1
        if direction == '>':
            pos_y += 1
        if direction == '<':
            pos_y -= 1
        if direction == 'v':
            pos_x += 1
        # process data here...
        if (pos_x, pos_y) not in visited:
            visited.append((pos_x, pos_y))
    return len(visited)


def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    data = data.split('\n')
    result = 0

    # process data here...

    return result


DAY = 3
DEBUG = False  # False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
