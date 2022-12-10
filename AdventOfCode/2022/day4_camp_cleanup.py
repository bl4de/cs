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


def check_pairs(pairs) -> bool:
    '''
    Check if ranges contains each other
    '''
    pairs[0] = pairs[0].split('-')
    pairs[1] = pairs[1].split('-')
    first_in_second = int(pairs[0][0]) <= int(
        pairs[1][0]) and int(pairs[0][1]) >= int(pairs[1][1])
    second_in_first = int(pairs[1][0]) <= int(
        pairs[0][0]) and int(pairs[1][1]) >= int(pairs[0][1])
    return True if (first_in_second is True or second_in_first is True) else False


@timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    data = data.split('\n')
    result = 0

    for d in data:
        pairs = d.split(',')
        if check_pairs(pairs) is True:
            result += 1
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


DAY = 4
DEBUG = True if len(sys.argv) > 1 and sys.argv[1] else False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
