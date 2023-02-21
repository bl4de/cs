#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def digitCount(self, num: str) -> bool:
        """
        Solution function goes here
        """
        for i, c in enumerate(num):
            if num.count(str(i)) != int(c):
                return False
        return True


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.digitCount("1210"), True)
solution.test(solution.digitCount("030"), False)