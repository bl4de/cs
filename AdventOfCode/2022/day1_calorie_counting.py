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


def process_elves(data) -> List[int]:
    '''
    Process elves
    '''
    data = data.split('\n')
    elves = []
    current_elf = 0
    for calories_count in data:
        if calories_count != '':
            current_elf += int(calories_count)
        else:
            elves.append(current_elf)
            current_elf = 0
    return elves


@timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    return max(process_elves(data))


@timer
def part_two_solution(data) -> int:
    '''
    Solution for Part 2.
    '''
    elves = process_elves(data)
    top_three = 0
    for _i in range(0, 3):
        top_three += elves.pop(elves.index(max(elves)))
    return top_three


DAY = 1
DEBUG = True if len(sys.argv) > 1 and sys.argv[1] else False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
