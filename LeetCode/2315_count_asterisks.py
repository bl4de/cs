#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/count-asterisks/
"""
from typing import List, Optional
import string

class Solution:
    """
    LeetCode solution class
    """
    endline = '\33[0m'
    green = '\33[32m'
    red = '\33[31m'
    PASS = f"{green}[+] PASS {endline}"
    FAIL = f"{red}[+] FAIL {endline}"

    def test(self, provided, expected) -> bool:
        """
        Compares provided result to expected
        """
        print(f"\n output  : {provided}\n expected: {expected}")
        print(f" {self.PASS if provided == expected else self.FAIL}")
        return provided == expected

    def countAsterisks(self, s: str) -> int:
        """
        Solution function goes here
        """
        result = 0
        pair = False
        for c in s:
            if c == '|':
                pair = not pair
            if c == '*' and not pair:
                result += 1
        return result

solution = Solution()
solution.test(solution.countAsterisks("l|*e*et|c**o|*de|"), 2)
solution.test(solution.countAsterisks("iamprogrammer"), 0)
solution.test(solution.countAsterisks("yo|uar|e**|b|e***au|tifu|l"), 5)

