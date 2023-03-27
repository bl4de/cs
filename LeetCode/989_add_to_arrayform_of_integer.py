#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/add-to-array-form-of-integer/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """
        Solution function goes here
        """
        return [int(c) for c in str((int(''.join([str(i) for i in num])) + k))]


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.addToArrayForm(num=[1, 2, 0, 0], k=34), [1, 2, 3, 4])
solution.test(solution.addToArrayForm(num=[2, 7, 4], k=181), [4, 5, 5])
solution.test(solution.addToArrayForm(num=[2, 1, 5], k=806), [1, 0, 2, 1])

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
