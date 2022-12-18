#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, no-self-use
'''
AdventOfCode Challenge Template

https://adventofcode.com/events

https://www.reddit.com/r/adventofcode/wiki/solution_megathreads/
'''

import pathlib
import functools
import time
import sys
from typing import List


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


def find_the_marker(signal: str, how_many_characters: int) -> int:
    '''
    Identifies marker position
    '''
    marker_position = 0
    marker = []
    for position, c in enumerate(signal):
        marker_position = position
        if c not in marker:
            if len(marker) == how_many_characters:
                return marker_position
        else:
            while c in marker:
                marker = marker[1:14]
        marker.append(c)
    return marker_position


@ timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    data = data.split('\n')
    result = 0
    for signal in data:
        print(find_the_marker(signal=signal, how_many_characters=4))

    return result


@ timer
def part_two_solution(data) -> int:
    '''
    Solution for Part 2.
    '''
    data = data.split('\n')
    result = 0
    for signal in data:
        print(find_the_marker(signal=signal, how_many_characters=14))

    return result


DAY = 6
DEBUG = True if len(sys.argv) > 1 and sys.argv[1] else False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))