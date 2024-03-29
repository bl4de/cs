#!/usr/bin/env python3
'''
AdventOfCode Challenge Template

https://adventofcode.com/events

https://www.reddit.com/r/adventofcode/wiki/solution_megathreads/
'''

from array import array
from ast import Delete
import pathlib
import functools
from re import split
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


def process_command(command):
    '''
    parses command and returns what needs to be done, start and end coords
    '''
    cmd = 'TOGGLE'
    parts = split(' ', command)
    coords = {
        'from': [int(c) for c in split(',', parts[-3])],
        'to':  [int(c) for c in split(',', parts[-1])]
    }
    if 'toggle' not in command:
        cmd = 'ON' if 'turn on' in command else 'OFF'
    return [cmd, coords]


@timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    MATRIX = []
    data = data.split('\n')
    result = 0

    for command in data:
        [cmd, coords] = process_command(command)
        for x in range(coords['from'][0], coords['to'][0] + 1):
            for y in range(coords['from'][1], coords['to'][1] + 1):
                pos = (x, y)
                if cmd == 'ON' and pos not in MATRIX:
                    MATRIX.append(pos)
                if cmd == 'OFF' and pos in MATRIX:
                    MATRIX.remove(pos)
                if cmd == 'TOGGLE':
                    if pos in MATRIX:
                        MATRIX.remove(pos)
                    else:
                        MATRIX.append(pos)
        print(len(MATRIX))
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


DAY = 6
DEBUG = True if len(sys.argv) > 1 and sys.argv[1] else False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
