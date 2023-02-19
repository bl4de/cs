#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/count-the-digits-that-divide-a-number/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def countDigits(self, num: int) -> int:
        """
        Solution function goes here
        """
        result = 0
        for digit in [int(d) for d in str(num)]:
            if num % digit == 0:
                result += 1
        return result


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.countDigits(7), 1)
solution.test(solution.countDigits(121), 2)
solution.test(solution.countDigits(1248), 4)
