#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/count-operations-to-obtain-zero/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def countOperations(self, num1: int, num2: int) -> int:
        """
        Solution function goes here
        """
        if num1 == 0 or num2 == 0:
            return 0
        result = 0
        while num1 != num2:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            result += 1
        return result + 1  # last operation: num1 - num2


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.countOperations(num1=2, num2=3), 3)
solution.test(solution.countOperations(num1=10, num2=10), 1)

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
