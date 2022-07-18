#!/usr/bin/env python3
'''
AdventOfCode Challenge Template
https://adventofcode.com/events
'''

import pathlib
import functools
import time
import sys

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


def at_least_three_vowels(naughty_string) -> boolean:
    '''
    Checks if there are enough vowels in string
    '''
    enough = 3
    counter = 0
    vowels = list('aeiou')
    for (_, character) in enumerate(naughty_string):
        if character in vowels:
            counter += 1
    return counter >= enough


def two_in_a_row(naughty_string) -> boolean:
    '''
    Checks if there are two the same characters in a row
    '''
    for (i, _) in enumerate(naughty_string):
        if i < len(naughty_string) - 1 and (naughty_string[i + 1] == naughty_string[i]):
            return True
    return False


def not_contain(naughty_string) -> boolean:
    '''
    Checks if string does not contain ['ab', 'cd', 'pq', 'xy']:
    '''
    for not_allowed in ['ab', 'cd', 'pq', 'xy']:
        if not_allowed in naughty_string:
            return False
    return True


def pair_twice_no_overlap(naughty_string) -> boolean:
    '''
    It contains a pair of any two letters that appears at least twice in the string without overlapping
    '''
    characters = {}
    at_least_twice = False

    for (i, c) in enumerate(naughty_string):
        if i > 1:
            if (naughty_string[i] == naughty_string[i - 1]) and (naughty_string[i - 1] == naughty_string[i - 2]):
                return False
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
        if characters[c] > 1:
            at_least_twice = c

    return bool(at_least_twice)


def repats_with_one_letter_between(naughty_string) -> boolean:
    '''
    wIt contains at least one letter which repeats with exactly one letter between them
    '''
    for (i, _) in enumerate(naughty_string):
        if i > 1:
            if (naughty_string[i] == naughty_string[i - 1]) and (naughty_string[i - 1] == naughty_string[i - 2]):
                return False
            if i < len(naughty_string):
                print(
                    f"{naughty_string[i - 1]} {naughty_string[i]} {naughty_string[i + 1]}")
                if naughty_string[i - 1] == naughty_string[i + 1]:
                    return True
    return False


@timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    data = data.split('\n')
    result = 0

    # process data here...
    for naughty_string in data:
        if at_least_three_vowels(naughty_string) and two_in_a_row(naughty_string) and not_contain(naughty_string):
            result = result + 1
    return result


@timer
def part_two_solution(data) -> int:
    '''
    Solution for Part 2.
    '''
    data = data.split('\n')
    result = 0

    # process data here...
    for naughty_string in data:
        if pair_twice_no_overlap(naughty_string) and repats_with_one_letter_between(naughty_string):
            result = result + 1
    return result


DAY = 5
DEBUG = True if len(sys.argv) > 1 and sys.argv[1] else False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()


daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
# print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
