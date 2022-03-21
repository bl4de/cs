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
    pos_x = 0  # starting point X
    pos_y = 0  # starting point Y
    visited = [(pos_x, pos_y)]
    for direction in data:
        if direction == '^':
            pos_x -= 1
        if direction == '>':
            pos_y += 1
        if direction == '<':
            pos_y -= 1
        if direction == 'v':
            pos_x += 1
        # process data here...
        if (pos_x, pos_y) not in visited:
            visited.append((pos_x, pos_y))
    return len(visited)


def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    pos_x = 0  # starting point X
    pos_y = 0  # starting point Y
    visited_by_santa = [(pos_x, pos_y)]
    visited_by_robot = [(pos_x, pos_y)]
    iterator = 0
    combined = 0
    for direction in data:
        if direction == '^':
            pos_x -= 1
        if direction == '>':
            pos_y += 1
        if direction == '<':
            pos_y -= 1
        if direction == 'v':
            pos_x += 1
        if iterator % 2 == 0 and (pos_x, pos_y) not in visited_by_santa:
            visited_by_santa.append((pos_x, pos_y))
        else:
            if (pos_x, pos_y) not in visited_by_robot:
                visited_by_robot.append((pos_x, pos_y))
        iterator += 1
        breakpoint()
    for house in visited_by_santa:
        if house not in visited_by_robot:
            combined += 1
    for house in visited_by_robot:
        if house not in visited_by_santa:
            combined += 1

    return combined


DAY = 3
DEBUG = True  # False

# read challenge input data
INPUT_PATH = f"test_input{DAY}.txt" if DEBUG is True else f"input{DAY}.txt"
daily_input = pathlib.Path(INPUT_PATH).read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
