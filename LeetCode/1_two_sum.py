#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/two-sum/
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
        self.test(self.solution(nums=[2, 7, 11, 15], target=9), [0, 1])
        self.test(self.solution(nums=[3, 2, 4], target=6), [1, 2])
        self.test(self.solution(nums=[3, 3], target=6), [0, 1])
        self.test(self.solution(nums=[3, 2, 3], target=6), [0, 2])

    def solution(self, nums: List[int], target: int) -> List[int]:
        """
        Solution function goes here
        """
        result = []
        if len(nums) == 2:
            return [0,1]
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i + 1:]:
                return [nums.index(nums[i]), nums.index(target - nums[i])]
        return result


sys.setrecursionlimit(1000)
profiler = cProfile.Profile()
solution = Solution()

solution.timer_start()
profiler.enable()
for i in range(0, 1):
    profiler.run("solution.solve()")
solution.timer_stop()

# profiler.print_stats()
profiler.disable()
