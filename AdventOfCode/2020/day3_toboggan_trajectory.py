#!/usr/bin/env python3
# AdventOfCode Template

import pathlib


def part_one(data) -> int:
    print(data)
    slop = 0
    trees = 0
    iter = 0
    for lvl in data:
        print(iter, lvl)
        trees = trees + 1 if lvl[slop] == '#' else trees
        print(slop, lvl[slop], trees, '\n\n')
        slop = slop + 3 if (slop < len(lvl) - 3) else (slop + 3 - len(lvl))
        iter = iter + 1
        if iter == 10:
            break

    # process data here...
    return trees


def part_two(data) -> int:
    result = 0
    # process data here...
    return result


data = pathlib.Path("./tt_input.txt").read_text().split('\n')[:-1]
print(part_one(data))  # Part 1. solution
print(part_two(data))  # Part 2. solution
