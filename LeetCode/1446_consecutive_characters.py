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
        print(f"\n output  : {provided}\n expected: {expected}")
        print(f" {self.PASS if provided == expected else self.FAIL}")
        return provided == expected

    def maxPower(self, s: str) -> int:
        i = 1
        iterations = 0
        max_power = 1
        current_power = 1

        while i < len(s):
            # we do need to go over entire string when there is less characters
            # left than max_power:
            if s[i] == s[i-1]:
                current_power += 1
                max_power = current_power if current_power >= max_power else max_power
            else:
                current_power = 1
            i += 1
            iterations += 1
        return max_power


solution = Solution()
solution.debug(solution.maxPower("leetcode"), 2)
solution.debug(solution.maxPower("tourist"), 1)
solution.debug(solution.maxPower("abbcccddddeeeeedcba"), 5)
solution.debug(solution.maxPower("triplepillooooow"), 5)
