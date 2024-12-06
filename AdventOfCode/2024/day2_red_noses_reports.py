#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, no-self-use
'''
AdventOfCode Challenge Template

https://adventofcode.com/events

https://www.reddit.com/r/adventofcode/wiki/solution_megathreads/
'''

import functools
import pathlib
import sys
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

def prepare_data(data) -> []:
    data = data.split('\n')
    reports = []
    for l in data:
        reports.append([int(i) for i in l.split(' ')])
    return reports

@timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    result = 0
    reports = prepare_data(data)
    for report in reports:
        safe = True
        up = True if report[1] > report[0] else False
        for i in range(1, len(report)):
            curr = report[i]
            prev = report[i - 1]
            if 1 <= abs(curr - prev) <= 3 and (curr > prev) == up:
                safe = True
            else:
                safe = False
                break
        result = result + 1 if safe == True else result
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
