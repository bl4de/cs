#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/add-strings/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Solution function goes here
        """
        return str(int(num1) + int(num2))


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.addStrings(num1="11", num2="123"), "134")
solution.test(solution.addStrings(num1="456", num2="77"), "533")
solution.test(solution.addStrings(num1="0", num2="0"), "0")

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
