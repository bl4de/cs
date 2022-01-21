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
    decreased = 0
    increased = 0
    current_window = 0
    prev_window = 0

    measurements = list(data.split('\n'))
    position = 0
    # process data here...
    for position in range(0, len(measurements) - 2):
        current_window = int(measurements[position]) + int(
            measurements[position + 1]) + int(measurements[position + 2])
        position += 1
        if prev_window > 0 and current_window > prev_window:
            increased += 1
        elif prev_window == current_window:
            pass  # no change
        else:
            decreased += 1
        prev_window = current_window

    return increased


# challenge input data
input_data = pathlib.Path("./input.txt").read_text('utf-8').strip()

# Part 1. solution
print(part_one_solution(input_data))

# Part 2. solution
print(part_two_solution(input_data))
