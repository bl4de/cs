#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def numberOfSteps(self, num: int) -> int:
        """
        Solution function goes here
        """
        result = 0
        return result


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.numberOfSteps(num=14), 6)
solution.test(solution.numberOfSteps(num=8), 4)
solution.test(solution.numberOfSteps(num=123), 12)

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
