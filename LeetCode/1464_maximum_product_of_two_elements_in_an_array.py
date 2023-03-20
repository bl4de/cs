#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def maxProduct(self, nums: List[int]) -> int:
        """
        Solution function goes here
        """
        return (nums.pop(nums.index(max(nums))) - 1) * (nums.pop(nums.index(max(nums))) - 1)


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.maxProduct(nums=[3, 4, 5, 2]), 12)
solution.test(solution.maxProduct(nums=[1, 5, 4, 5]), 16)
solution.test(solution.maxProduct(nums=[3, 7]), 12)

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
