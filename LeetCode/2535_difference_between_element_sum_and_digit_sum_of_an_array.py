#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
"""
from typing import List, Optional
import string
import sys


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

    def differenceOfSum(self, nums: List[int]) -> int:
        """
        Solution function goes here
        """
        result = 0
        return result


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.differenceOfSum([1, 15, 6, 3]), 9)
solution.test(solution.differenceOfSum([1, 2, 3, 4]), 0)
