#!/usr/bin/env python3
# AdventOfCode Template

import pathlib


def part_one(data) -> int:
    result = 0
    for direction in data:
        result = result + 1 if direction == '(' else result - 1
    return result


def part_two(data) -> int:
    result = 0
    iterator = 1
    for direction in data:
        result = result + 1 if direction == '(' else result - 1
        if result == -1:
            return iterator
        iterator += 1

    return result


data = pathlib.Path("./input.txt").read_text().strip()
print(part_one(data))  # Part 1. solution
print(part_two(data))  # Part 2. solution
