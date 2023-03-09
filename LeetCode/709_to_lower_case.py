#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/to-lower-case/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def toLowerCase(self, s: str) -> str:
        return s.lower()


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.toLowerCase("Hello"), "hello")
# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
