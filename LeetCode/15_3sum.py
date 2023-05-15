#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/3sum/
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
        self.test(self.solution(
            nums=[-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.test(self.solution(nums=[0, 1, 1]), [])
        self.test(self.solution(nums=[0, 0, 0]), [[0, 0, 0]])

    def solution(self, nums: List[int]) -> List[List[int]]:
        """
        Solution function goes here
        """
        result = []
        l = len(nums)
        for i in range(0, l):
            for j in range(0, l):
                for k in range(0, l):
                    if i != j and j != k and k != i:
                        if nums[i] + nums[j] + nums[k] == 0:
                            result.append([nums[i], nums[j], nums[k]])
        return result


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
