#!/usr/bin/env python3
# https://adventofcode.com/2020/day/2

import pathlib


def part_one(data) -> int:
    correct_passwords = 0
    for pwd in [(p.split(' ')) for p in data.split('\n')]:
        min_occurences, max_occurences = pwd[0].split('-')
        character = pwd[1][0:1]
        correct_passwords = (correct_passwords + 1) if (int(min_occurences) <=
                                                        pwd[2].count(character) <= int(max_occurences)) else correct_passwords

    return correct_passwords


def part_two(data) -> int:
    result = 0
    # process data here...
    return result


data = pathlib.Path("./input.txt").read_text().strip()
print(part_one(data))  # Part 1. solution
print(part_two(data))  # Part 2. solution
