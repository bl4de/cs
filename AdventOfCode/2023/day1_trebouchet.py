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
import string
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


def convert_word_to_numbers(word: str) -> str:
    '''
    converts word to number representation
    '''
    word = word.lower().replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace(
        'five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9').replace('zero', '0')
    return word


@timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    data = data.split('\n')
    result = 0

    # process data here...
    for c in data:
        first = 0
        second = 0
        for i in c:
            if i.isdigit():
                first = i
                break
        for i in c[::-1]:
            if i.isdigit():
                second = i
                break
        result += int(f"{first}{second}")
    return result


@timer
def part_two_solution(data) -> int:
    '''
    Solution for Part 2.
    '''
    data = data.split('\n')
    result = 0

    # process data here...
    # process data here...
    for c in data:
        first = 0
        second = 0
        c = convert_word_to_numbers(c)
        for i in c:
            if i.isdigit():
                first = i
                break
        for i in c[::-1]:
            if i.isdigit():
                second = i
                break
        result += int(f"{first}{second}")
    return result


DAY = 1
DEBUG = True  # if len(sys.argv) > 1 and sys.argv[1] else False

# read challenge input data
INPUT_PATH = f"/Users/bl4de/playground/cs/AdventOfCode/2023/test_input{DAY}.txt" if DEBUG is True else f"/Users/bl4de/playground/cs/AdventOfCode/2023/input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
