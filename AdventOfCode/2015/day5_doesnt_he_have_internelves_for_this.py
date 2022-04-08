#!/usr/bin/env python3
'''
AdventOfCode Challenge Template
https://adventofcode.com/events
'''

import pathlib


def part_one_solution(data) -> int:
    '''
        Solution for Part 1.
    '''
    data = data.split('\n')
    result = 0

    # process data here...
    for naughty_string in data:
        is_naughty = False
        # does not contain the strings ab, cd, pq, or xy,
        # even if they are part of one of the other requirements:
        for not_contain in ['ab', 'cd', 'pq', 'xy']:
            if not_contain in naughty_string:
                is_naughty = True
        # contains at least one letter that appears twice in a row OR
        # contains at least three vowels (aeiou only)
        vowels_counter = 0
        for (i, character) in enumerate(naughty_string):
            if character in 'aeiou':
                vowels_counter += 1
                if vowels_counter == 3:
                    break
            if naughty_string[i] == naughty_string[i - 1]:
                break

        result = result + 1 if not is_naughty else result

    return result


def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    data = data.split('\n')
    result = 0

    # process data here...

    return result


DAY = 5
DEBUG = False  # False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()


daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
