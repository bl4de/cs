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
        if num == 0:
            return num
        result = 0
        while num > 1:
            if num % 2 != 0:
                num -= 1
                result += 1
            num = num / 2
            result += 1
        return result + 1


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.numberOfSteps(num=14), 6)
solution.test(solution.numberOfSteps(num=8), 4)
solution.test(solution.numberOfSteps(num=123), 12)

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
