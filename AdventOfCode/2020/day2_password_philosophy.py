#!/usr/bin/env python3
# https://adventofcode.com/2020/day/2

import pathlib


def main(data):
    correct_passwords = 0
    criteria = [(p.split(' ')) for p in data.split('\n')]
    for pwd in criteria:
        min_occurences, max_occurences = pwd[0].split('-')
        character = pwd[1][0:1]
        if int(min_occurences) <= pwd[2].count(character) <= int(max_occurences):
            correct_passwords += 1

    return correct_passwords


data = pathlib.Path("./input.txt").read_text().strip()
correct_passwords = main(data)
print(correct_passwords)
