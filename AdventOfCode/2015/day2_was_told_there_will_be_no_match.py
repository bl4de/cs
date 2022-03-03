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
    for data_item in data.split('\n'):
        present = data_item.split('x')
        l = int(present[0])
        h = int(present[1])
        w = int(present[2])
        current = (2*l*h) + (2*w*h) + (2*l*w) + min([w*h, l*h, l*w])
        result += current
    return result


def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    result = 0
    # process data here...
    for data_item in data.split('\n'):
        ribbon = 0
        present = data_item.split('x')
        l = int(present[0])
        h = int(present[1])
        w = int(present[2])
        maxval = int(max(present))
        if l == maxval:
            ribbon = (2*h) + (2*w) + (l*h*w)
        if h == maxval:
            ribbon = (2*l) + (2*w) + (l*h*w)
        if w == maxval:
            ribbon = (2*h) + (2*l) + (l*h*w)
        result += ribbon

    return result


DEBUG = False  # False

# read challenge input data
if DEBUG:
    daily_input = pathlib.Path(
        "/Users/bl4de/playground/cs/AdventOfCode/2015/test_input.txt").read_text('utf_8').strip()
else:
    daily_input = pathlib.Path(
        "/Users/bl4de/playground/cs/AdventOfCode/2015/input.txt").read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
