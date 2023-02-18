#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/create-target-array-in-the-given-order/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        """
        Solution function goes here
        """
        result = []
        for i, n in enumerate(nums):
            result.insert(index[i], n)
        return result


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]), [0, 4, 1, 3, 2])
solution.test(solution.createTargetArray(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]), [0, 1, 2, 3, 4])
solution.test(solution.createTargetArray([1], [0]), [1])
