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


def extract_cubes(game: str) -> dict:
    '''
    extracts max cubes and returns list of color:qty
    '''
    blue = 0
    red = 0
    green = 0
    for g in game.split(';'):
        for color in g.split(','):
            print(color)

    return {
        'blue': blue,
        'red': red,
        'green': green
    }


@timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    data = data.split('\n')
    result = 0

    # process data here...
    for game in data:
        game = game.split(':')
        extract_cubes(game=game[1])
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
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
