#!/usr/bin/env python3
'''
AdventOfCode Challenge Template
https://adventofcode.com/events
'''

import pathlib
import functools
import time


def timer(func):
    '''
        @timer decorator to measure execution time
        of solution functions
    '''
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return _wrapper


@timer
def part_one_solution(data) -> int:
    '''
        Solution for Part 1.
    '''
    data = data.split(',')
    result = 0
    orientations = ['N', 'E', 'S', 'W']
    orientation_index = 0
    orientation = orientations[orientation_index]
    print(orientation_index, orientations[orientation_index])

    for move in data:
        move = move.strip()
        direction = move[0]
        distance = int(move[1])

        if direction == 'L':
            orientation_index = 0 if orientation_index - 1 < 0 else orientation_index - 1
            orientation = orientations[orientation_index]
        if direction == 'R':
            orientation_index = 0 if orientation_index + 1 > 3 else orientation_index + 1
            orientation = orientations[orientation_index]

        if orientation == 'N' or orientation == 'L':
            result += distance
        else:
            result -= distance
    return result


@timer
def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    data = data.split('\n')
    result = 0

    # process data here...

    return result


DAY = 1
DEBUG = True  # UNCOMMENT FOR DEBUG
# DEBUG = False # UNCOMMENT FOR PRODUCTION

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()


daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
