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
    horizontal_position = 0
    depth = 0
    for move in data.split('\n'):
        (direction, distance) = move.split(' ')
        if direction == 'forward':
            horizontal_position += int(distance)
        elif direction == 'up':
            depth -= int(distance)
        else:
            depth += int(distance)

    return horizontal_position * depth


def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    # process data here...
    horizontal_position = 0
    depth = 0
    aim = 0
    for move in data.split('\n'):
        (direction, distance) = move.split(' ')
        if direction == 'down':
            aim += int(distance)
        elif direction == 'up':
            aim -= int(distance)
        else:
            horizontal_position += int(distance)
            depth += aim * int(distance)

    return horizontal_position * depth


# challenge input data
daily_input = pathlib.Path("./input.txt").read_text('utf-8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
