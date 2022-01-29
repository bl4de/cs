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
    iterator = 1
    while iterator < len(data):
        if int(data[iterator - 1]) == int(data[iterator]):
            result += int(data[iterator])
        iterator += 1
    if int(data[len(data) - 1]) == int(data[0]):
        result += int(data[0])
    return result


def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    result = 0
    # process data here...
    iterator = 0
    list_len = len(data)/2
    while iterator < len(data):
        position = int(iterator + list_len if iterator <
                       list_len else iterator - list_len)
        if int(data[iterator]) == int(data[position]):
            result += int(data[iterator])
        iterator += 1
    return result


# challenge input data
data = pathlib.Path("./input.txt").read_text().strip()

# Part 1. solution
print(part_one_solution(data))

# Part 2. solution
print(part_two_solution(data))
