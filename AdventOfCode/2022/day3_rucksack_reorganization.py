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

# split comparment in half
# find shared item
# add its priority to result


@timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    data = data.split('\n')
    result = 0
    for rucksacks in data:
        first = rucksacks[:len(rucksacks)//2]
        second = rucksacks[len(rucksacks)//2:]
        for c in first:
            if c in second:
                if ord(c) > 96:
                    result += int(ord(c) - 96)
                else:
                    result += int(ord(c) - 38)
                break
    return result


@timer
def part_two_solution(data) -> int:
    '''
    Solution for Part 2.
    '''
    data = data.split('\n')
    result = 0
    counter = 0
    trinity = []
    for rucksacks in data:
        if counter == 3:
            counter = 0
            trinity.clear()
            trinity.append(rucksacks)
        else:
            trinity.append(rucksacks)
            counter += 1

        if len(trinity) == 3:
            for c in trinity[0]:
                if c in trinity[1] and c in trinity[2]:
                    if ord(c) > 96:
                        result += int(ord(c) - 96)
                    else:
                        result += int(ord(c) - 38)
                    break
    return result


DAY = 3
DEBUG = True if len(sys.argv) > 1 and sys.argv[1] else False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
