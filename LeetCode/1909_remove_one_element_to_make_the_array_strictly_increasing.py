#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
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
        # self.test(self.solution([1, 2, 10, 5, 7]), True)
        # self.test(self.solution([2, 3, 1, 2]), False)
        # self.test(self.solution([1, 1, 1]), False)
        # self.test(self.solution([1, 1]), True)
        # self.test(self.solution([2, 1]), True)
        self.test(self.solution([105,924,32,968]), True)

    def solution(self, nums: List[int]) -> bool:
        """
        Solution function goes here
        """
        
        if len(nums) == 2:
            return True
        
        removed = False
        i = 1
        while i < len(nums):
            if nums[i] > nums[i - 1]:
                i += 1
                continue
            if nums[i] < nums[i - 1] and removed is False:
                del nums[i - 1]
                removed = True
                i = 1
                continue
            else:
                return False
        return True


NUMS_OF_EXECUTION = 1
SHOW_PROFILER_STATS = True

sys.setrecursionlimit(1000)
profiler = cProfile.Profile()
solution = Solution()

solution.timer_start()
profiler.enable()
for i in range(0, NUMS_OF_EXECUTION):
    profiler.run("solution.solve()")
solution.timer_stop()

if SHOW_PROFILER_STATS:
    profiler.print_stats(sort='calls')
profiler.disable()
