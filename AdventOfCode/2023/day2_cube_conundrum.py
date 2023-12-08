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

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


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
            color_details = color.strip().split(' ')
            if color_details[1] == 'blue' and int(color_details[0]) > blue:
                blue = int(color_details[0])
            if color_details[1] == 'red' and int(color_details[0]) > red:
                red = int(color_details[0])
            if color_details[1] == 'green' and int(color_details[0]) > green:
                green = int(color_details[0])
    return {
        'blue': blue,
        'red': red,
        'green': green
    }


def extract_game_number(game: str) -> int:
    '''
    returns integer representing Game number
    '''
    return int(game.split(' ')[1])


def check_game(game) -> bool:
    '''
    checks if game is possible
    '''
    if game['red'] > MAX_RED or game['blue'] > MAX_BLUE or game['green'] > MAX_GREEN:
        return False
    return True


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
        cubes = extract_cubes(game=game[1])
        if check_game(cubes):
            result += extract_game_number(game=game[0])
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
