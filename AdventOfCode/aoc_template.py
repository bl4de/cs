#!/usr/bin/env python3
# https://adventofcode.com/2020/day/2

import pathlib


def main(data):
    print(data)


data = pathlib.Path("./input.txt").read_text().strip()
main(data)
