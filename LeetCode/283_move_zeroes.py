#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/move-zeroes/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Solution function goes here
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
        print(nums)


sys.setrecursionlimit(1000)
solution = Solution()
solution.moveZeroes([0, 1, 0, 3, 12])  # [1,3,12,0,0]
solution.moveZeroes([0])  # [0]
