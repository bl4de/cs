#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/perfect-number/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def checkPerfectNumber(self, num: int) -> bool:
        """
        Solution function goes here
        """
        return sum([d for d in range(1, round(num / 2) + 1) if num % d == 0]) == num


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.checkPerfectNumber(num=28), True)
solution.test(solution.checkPerfectNumber(num=7), False)
