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


def contains(code: str, num: int) -> bool:
    '''
    Checks if code contains two letters 
    '''
    cont = {}
    for c in range(1, len(code)):
        if code[c] not in cont.keys():
            cont[code[c]] = 1
        cont[code[c]] = cont[code[c]] + 1

    for _, c in enumerate(cont):
        if int(cont[c]) == num:
            return True
    return False


@timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    data = data.split('\n')
    result = [0, 0]

    # process data here...
    for p in data:
        if contains(p, 2) is True:
            result[0] += 1
        if contains(p, 3) is True:
            result[1] += 1
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


DAY = 2
DEBUG = True if len(sys.argv) > 1 and sys.argv[1] else False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
part1 = part_one_solution(daily_input)
print(part1, part1[0] * part1[1])


# Part 2. solution
print(part_two_solution(daily_input))
