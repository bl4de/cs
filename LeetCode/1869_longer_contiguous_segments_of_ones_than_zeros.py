#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
'''
    LeetCode solution class
'''
from typing import List, Optional


class Solution:
    '''
    LeetCode solution class
    '''
    colors = {
        "black": '\33[30m',
        "red": '\33[31m',
        "green": '\33[32m',
        "yellow": '\33[33m',
        "blue": '\33[34m',
        "magenta": '\33[35m',
        "cyan": '\33[36m',
        "white": '\33[37m',
        "grey": '\33[90m',
        "lightblue": '\33[94m'
    }
    endline = '\33[0m'
    PASS = f"{colors['green']}[+] PASS {endline}"
    FAIL = f"{colors['red']}[+] FAIL {endline}"

    def debug(self, provided, expected) -> bool:
        '''
        Compares provided result to expected
        Returns true if equal
        '''
        print(f" output  : {provided}\n expected: {expected}")
        print(f" {self.PASS if provided == expected else self.FAIL}\n")
        return provided == expected

    def checkZeroOnes(self, s: str) -> bool:
        longest_zeroes = 0
        current_zeroes = 0
        longest_ones = 0
        current_ones = 0
        for n in s:
            if n == '1':
                current_ones += 1
                current_zeroes = 0
            else:
                current_zeroes += 1
                current_ones = 0
            longest_ones = current_ones if current_ones > longest_ones else longest_ones
            longest_zeroes = current_zeroes if current_zeroes > longest_zeroes else longest_zeroes
        return True if longest_ones > longest_zeroes else False


solution = Solution()
solution.debug(solution.checkZeroOnes("1101"), True)
solution.debug(solution.checkZeroOnes("111000"), False)
solution.debug(solution.checkZeroOnes("110100010"), False)
solution.debug(solution.checkZeroOnes("01111110"), True)
