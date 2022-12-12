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


def create_starting_point(initial_crates_layout):
    '''
    Creates stacks of crates from challenge input
    '''
    _stacks = []
    for line in initial_crates_layout.split("\n"):
        _stacks.append([])
        for stack, crate in enumerate(line.split(" ")):
            if crate not in "1234567890":
                _stacks[stack].append(crate)
    _stacks.pop()
    for s in _stacks:
        s.reverse()
    return _stacks


@timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    data = data.split('\n')
    result = 0

    # process data here...

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


DAY = 5
DEBUG = True if len(sys.argv) > 1 and sys.argv[1] else False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()
stacks = create_starting_point(daily_input.split("\n\n")[0])
print(stacks)
# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
