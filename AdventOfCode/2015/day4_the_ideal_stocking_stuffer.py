#!/usr/bin/env python3
'''
AdventOfCode Challenge Template
https://adventofcode.com/events
'''

import hashlib


def part_one_solution(key) -> int:
    '''
        Solution for Part 1.
    '''
    result = 0
    md5_hash = ''
    while True:
        md5_hash = hashlib.md5(f"{key}{result}".encode('utf-8')).hexdigest()
        if md5_hash.startswith('00000'):
            return result
        result += 1
        if result % 100000 == 0:
            print(f"checked {result} combinations...")


def part_two_solution(key) -> int:
    '''
        Solution for Part 2.
    '''
    result = 0
    md5_hash = ''
    while True:
        md5_hash = hashlib.md5(f"{key}{result}".encode('utf-8')).hexdigest()
        if md5_hash.startswith('000000'):
            return result
        result += 1
        if result % 100000 == 0:
            print(f"checked {result} combinations...")

    # process data here...

    return result


DAY = 1
DEBUG = True  # False

# Part 1. solution
# print(part_one_solution('bgvyzdsv'))

# Part 2. solution
print(part_two_solution('bgvyzdsv'))
