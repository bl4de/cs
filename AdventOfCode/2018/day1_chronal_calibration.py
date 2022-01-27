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
    for frequency in data.split('\n'):
        result += int(frequency)
    return result


def check_frequency(data, freq: int, existing) -> int:
    '''
        helper for Part 2
    '''
    print(f'starts new iteration from: {freq}')
    for frequency in data.split('\n'):
        freq += int(frequency)
        if freq in existing:
            return (True, freq, existing)
        existing.append(freq)
    return (False, freq, existing)


def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    existing = []
    found, result, existing = check_frequency(data, 0, existing)
    while found is not True:
        found, result, existing = check_frequency(
            data, result, existing)
        print(found, result)

    return result


# challenge input data
data = pathlib.Path("./input.txt").read_text().strip()

# Part 1. solution
print(part_one_solution(data))

# Part 2. solution
print(part_two_solution(data))
