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
        is_nice = 0
        print(f"{naughty_string}")
        # does not contain the strings ab, cd, pq, or xy,
        # even if they are part of one of the other requirements:
        for not_contain in ['ab', 'cd', 'pq', 'xy']:
            if not_contain in naughty_string:
                print(f"[-] contains {not_contain}")
                continue
        # contains at least one letter that appears twice in a row OR
        # contains at least three vowels (aeiou only)
        vowels_counter = 0
        for (i, character) in enumerate(naughty_string):
            if character in list('aeiou'):
                vowels_counter += 1
                if vowels_counter > 2:
                    print(f"vowels counter: {vowels_counter}")
                    is_nice += 1
        for (i, character) in enumerate(naughty_string):
            if naughty_string[i] == naughty_string[i - 1]:
                print(
                    f"two characters in a row: {naughty_string[i]}{ naughty_string[i - 1]}")
                is_nice += 1
        print("-"*40)

        if not is_nice:
            pass
        else:
            if is_nice == 3:
                print("IS NICE!")
                result = result + 1 if is_nice == 3 else result
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
