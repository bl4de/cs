#!/usr/bin/env python3
# AdventOfCode Challenge Template
#
# https://adventofcode.com/events
#

from array import array
import pathlib


def binary_array_to_integer(binary_array: array) -> int:
    '''
        converts binary array into integer
    '''
    return int(''.join(binary_array), 2)


def part_one_solution(data) -> int:
    '''
        Solution for Part 1.
    '''
    result = 0
    gamma_rate = []
    epsilon_rate = []
    # process data here...
    data = data.split('\n')
    bits_len = len(data[0])
    for pos in range(0, bits_len):
        zeros = 0
        ones = 0
        for bits in data:
            if bits[pos] == '1':
                ones += 1
            else:
                zeros += 1
        print(zeros, ones)
        if zeros > ones:
            gamma_rate.append('0')
            epsilon_rate.append('1')
        else:
            gamma_rate.append('1')
            epsilon_rate.append('0')

    result = binary_array_to_integer(
        gamma_rate) * binary_array_to_integer(epsilon_rate)
    return result


def part_two_solution(data) -> int:
    '''
        Solution for Part 2.
    '''
    result = 0
    # process data here...
    return result


# challenge input data
daily_input = pathlib.Path("./input.txt").read_text('utf_8').strip()

# Part 1. solution
print(part_one_solution(daily_input))

# Part 2. solution
print(part_two_solution(daily_input))
