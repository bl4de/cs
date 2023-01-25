#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/
"""
from typing import List, Optional
import string
import re


class Solution:
    """
    LeetCode solution class
    """
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

    def test(self, provided, expected) -> bool:
        """
        Compares provided result to expected
        Returns true if equal
        """
        print(f"\n output  : {provided}\n expected: {expected}")
        print(f" {self.PASS if provided == expected else self.FAIL}")
        return provided == expected

    def areNumbersAscending(self, s: str) -> bool:
        """
        Solution function goes here
        """
        numbers = re.findall("\d+", s)
        for index in range(1, len(numbers)):
            if int(numbers[index]) <= int(numbers[index - 1]):
                return False
        return True


solution = Solution()
solution.test(solution.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"), True)
solution.test(solution.areNumbersAscending("hello world 5 x 5"), False)
