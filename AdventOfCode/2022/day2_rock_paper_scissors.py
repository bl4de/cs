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

MOVES = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

GAMES = {
    'lose': 0,
    'draw': 3,
    'win': 6
}


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

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors


@timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    data = data.split('\n')
    result = 0
    for game in data:
        print(game)
        move = game.split(' ')
        if (move[0] == 'A' and move[1]) == 'X' or (move[0] == 'B' and move[1]) == 'Y' or (move[0] == 'C' and move[1] == 'Z'):
            print(f"draw: {move[0]} {move[1]}")
            result += GAMES['draw'] + MOVES[move[1]]
        else:
            if (move[0] == 'A' and move[1]) == 'Y' or (move[0] == 'B' and move[1]) == 'Z' or (move[0] == 'C' and move[1] == 'X'):
                print(f"win: {move[0]} {move[1]}")
                result += GAMES['win'] + MOVES[move[1]]
            else:
                print(f"lose: {move[0]} {move[1]}")
                result += MOVES[move[1]]

        print(result)
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
