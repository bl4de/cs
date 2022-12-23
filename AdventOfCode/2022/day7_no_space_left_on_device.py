#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, no-self-use, global-statement
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


TREE = {'/': {}}  # contains full directory tree
POINTER = '/'  # current location after executig latest command
PREV_LOCATION = '/'


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


def cmd_cd(path: str):
    '''
    Moves pointer across directory tree
    '''
    global POINTER, PREV_LOCATION
    if path == '/':
        POINTER = '/'
    if path == '..':
        tmp = POINTER
        POINTER = PREV_LOCATION
        PREV_LOCATION = tmp


def cmd_ls():
    '''
    Parses current directory listing
    '''


def execute_command(command: str, arg=None):
    '''
    Executes command and updates TREE
    '''
    if command == 'cd':
        cmd_cd(path=arg)
    if command == 'ls':
        cmd_ls()
    pass


def parse_directory_listing():
    '''
    Parses lines after ls command and updates TREE
    '''
    pass


@timer
def part_one_solution(data) -> int:
    '''
    Solution for Part 1.
    '''
    data = data.split('\n')
    result = 0

    for command in data:
        if command.startswith('$'):
            cmd_args = command.split(' ')
            if len(cmd_args) > 2:
                execute_command(command=cmd_args[1], arg=cmd_args[2])
            else:
                execute_command(command=cmd_args[1])

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


DAY = 7
DEBUG = True if len(sys.argv) > 1 and sys.argv[1] else False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
