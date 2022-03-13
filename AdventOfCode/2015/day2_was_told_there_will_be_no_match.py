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
        present = data_item.split('x')
        box_length = int(present[0])
        box_height = int(present[1])
        box_width = int(present[2])
        maxval = int(max(present))
        if box_length == maxval:
            ribbon = (2*box_height) + (2*box_width) + \
                (box_length*box_height*box_width)
        if box_height == maxval:
            ribbon = (2*box_length) + (2*box_width) + \
                (box_length*box_height*box_width)
        if box_width == maxval:
            ribbon = (2*box_height) + (2*box_length) + \
                (box_length*box_height*box_width)
        result += ribbon

    return result


DEBUG = True  # False

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
