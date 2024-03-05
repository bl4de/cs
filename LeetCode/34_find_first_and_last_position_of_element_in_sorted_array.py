#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""
from typing import List, Optional
import string
import sys
import cProfile
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):

    def __init__(self, show_output=True) -> None:
        self.SHOW_OUTPUT = show_output
        super().__init__()

    def solve(self):
        """
        Solution runner called from profiler
        """
        self.test(self.solution(nums = [5,7,7,8,8,10], target = 8), [3,4])
        self.test(self.solution(nums = [5,7,7,8,8,10], target = 6), [-1, -1])
        self.test(self.solution([], 0), [-1, -1])

    def solution(self,  nums: List[int], target: int) -> List[int]:
        """
        Solution function goes here
        """
        result = [-1, -1]
        # edge cases: target not in nums or nums has less than 2 elements:
        if target not in nums or len(nums) <= 2:
            return result
        for i in nums:
            if i < target:
                continue
            if i == target:
                result[0] = nums.index(i)
                for index, j in enumerate(nums):
                    if j > target:
                        result[1] = index - 1
                        break
        return result


SHOW_OUTPUT = True
NUMS_OF_EXECUTION = 1
SHOW_PROFILER_STATS = True

sys.setrecursionlimit(1000)
profiler = cProfile.Profile()
solution = Solution(SHOW_OUTPUT)

solution.timer_start()
profiler.enable()
print(f"\nRUNNING:\t{NUMS_OF_EXECUTION} iterations")
print(f"OUTPUT:\t\t{'disabled' if SHOW_OUTPUT is False else 'enabled'}")
for i in range(0, NUMS_OF_EXECUTION):
    profiler.run("solution.solve()")
solution.timer_stop()

if SHOW_PROFILER_STATS:
    profiler.print_stats(sort='calls')
profiler.disable()
