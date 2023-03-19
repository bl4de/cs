#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/find-the-pivot-integer/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def pivotInteger(self, n: int) -> int:
        """
        Solution function goes here
        """
        result = 0

        return result


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.pivotInteger(8), 6)
solution.test(solution.pivotInteger(1), 1)
solution.test(solution.pivotInteger(4), -1)

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
