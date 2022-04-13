#!/usr/bin/env python3
'''
AdventOfCode Challenge Template
https://adventofcode.com/events
'''

import pathlib
import functools
import time
from xmlrpc.client import boolean


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


def enough_vowels(naughty_string) -> boolean:
    '''
        Checks if there are enough vowels in string
    '''
    enough = 3
    counter = 0
    vowels = list('aeiou')
    for (i, character) in enumerate(naughty_string):
        if character in vowels:
            counter += 1
    return counter >= enough


def two_in_a_row(naughty_string) -> boolean:
    '''
        Checks if there are two the same characters in a row
    '''
    return True


def not_contain(naughty_string) -> boolean:
    '''
        Checks if string does not contain ['ab', 'cd', 'pq', 'xy']:
    '''
    return True


@timer
def part_one_solution(data) -> int:
    '''
        Solution for Part 1.
    '''
    data = data.split('\n')
    result = 0

    # process data here...
    for naughty_string in data:
        if enough_vowels(naughty_string) and two_in_a_row(naughty_string) and not_contain(naughty_string):
            result += 1
        # is_nice = True
        # print(f"{naughty_string}")
        # # does not contain the strings ab, cd, pq, or xy,
        # # even if they are part of one of the other requirements:
        # for not_contain in ['ab', 'cd', 'pq', 'xy']:
        #     if not_contain in naughty_string:
        #         print(f"[-] contains {not_contain}")
        #         is_nice = False
        # print(f"{naughty_string}: {is_nice}")
        # # contains at least one letter that appears twice in a row OR
        # # contains at least three vowels (aeiou only)

        # if is_nice is True:
        #     is_nice = False
        #     for (i, character) in enumerate(naughty_string):
        #         if naughty_string[i] == naughty_string[i - 1]:
        #             print(
        #                 f"two characters in a row: {naughty_string[i]}{ naughty_string[i - 1]}")
        #             is_nice = True
        # print(f"{naughty_string}: {is_nice}")
        # print("-"*40)

        # if is_nice is True:
        #     print("IS NICE!")
        #     result = result + 1
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
# DEBUG = True
DEBUG = False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()


daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
# print(part_one_solution(daily_input))

# Part 2. solution
# print(part_two_solution(daily_input))
print(enough_vowels('sdfaaiooodsf') is False)
