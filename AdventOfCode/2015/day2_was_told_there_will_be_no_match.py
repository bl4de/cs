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
        box_length = int(present[0])
        box_height = int(present[1])
        box_width = int(present[2])
        current = (2*box_length*box_height) + (2*box_width*box_height) + (2*box_length *
                                                                          box_width) + min([box_width*box_height, box_length*box_height, box_length*box_width])
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
        box_size = 0
        sizes = [int(s) for s in data_item.split('x')]

        maxval = max(sizes)
        print(sizes, maxval)
        for s in sizes:
            if s != maxval:
                print(s, s+s)
                box_size += s+s
        ribbon = sizes[0] * sizes[1] * sizes[2]
        print(box_size, ribbon)
        ribbon = ribbon + box_size
        print(ribbon)
        result = result + ribbon

    return result


DEBUG = True
# DEBUG = False

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
