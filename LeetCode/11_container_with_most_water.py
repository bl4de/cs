#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/container-with-most-water/
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
        self.test(self.solution(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.test(self.solution(height=[1, 1]), 1)

    def solution(self, height: List[int]) -> int:
        """
        Solution function goes here
        """
        sums = {}
        for i in range(0, len(height)):
            for j in range(i, len(height)):
                sums[(height[i], height[j], j-i)] = height[i] * \
                    (j - i) if height[i] < height[j] else height[j] * (j - i)
        return max(sums.values())


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