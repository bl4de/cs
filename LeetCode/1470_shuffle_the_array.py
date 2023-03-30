#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/shuffle-the-array/
"""
from typing import List, Optional
import string
import sys
import cProfile
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    
    def solve(self):
        """
        Solution runner called from profiler
        """
        self.test(self.shuffle(nums = [2,5,1,3,4,7], n = 3),  [2,3,5,4,1,7] )
        self.test(self.shuffle(nums = [1,2,3,4,4,3,2,1], n = 4), [1,4,2,3,3,2,4,1])
        self.test(self.shuffle(nums = [1,1,2,2], n = 2),  [1,2,1,2])

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Solution function goes here
        """
        result = []
        nums1 = nums[0:n]
        nums2 = nums[n:]
        for i in range(0, n):
            result.append(nums1[i])
            result.append(nums2[i])
        return result


sys.setrecursionlimit(1000)
profiler = cProfile.Profile()
solution = Solution()

solution.timer_start()
profiler.enable()
for i in range(0, 1):
    profiler.run("solution.solve()")
solution.timer_start()

profiler.print_stats()
profiler.disable()
