#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/sign-of-the-product-of-an-array
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
        self.test(self.solution(nums=[-1, -2, -3, -4, 3, 2, 1]), 1)
        self.test(self.solution(nums=[1, 5, 0, 2, -3]), 0)
        self.test(self.solution(nums=[-1, 1, -1, 1, -1]), -1)

    def solution(self, nums: List[int]) -> int:
        """
        Solution function goes here
        """
        product = nums[0]
        for i in nums[1:]:
            product *= i
        if product == 0:
            return 0
        if product < 0:
            return -1
        return 1

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
