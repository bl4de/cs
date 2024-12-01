#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
"""
import cProfile
import sys
from itertools import count
from typing import List

from abstract_solution import AbstractSolution


class Solution(AbstractSolution):

    def __init__(self, show_output=True) -> None:
        self.SHOW_OUTPUT = show_output
        super().__init__()

    def solve(self):
        """
        Solution runner called from profiler
        """
        self.test(self.solution(nums=[0, 1, 1, 0]), [0, 1])
        self.test(self.solution(nums=[0, 3, 2, 1, 3, 2]), [2, 3])
        self.test(self.solution(nums=[7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]), [4, 5])

    def solution(self, nums: List[int]) -> List[int]:
        """
        Solution function goes here
        """
        result = []
        for n in nums:
            if nums.count(n) > 1 and n not in result:
                result.append(n)
        return result


SHOW_OUTPUT = True
NUMS_OF_EXECUTION = 1
USE_PROFILER = False
SHOW_PROFILER_STATS = True

profiler = None
sys.setrecursionlimit(1000)

if USE_PROFILER:
    profiler = cProfile.Profile()
solution = Solution(SHOW_OUTPUT)

solution.timer_start()
if USE_PROFILER:
    profiler.enable()
print(f"\nRUNNING:\t{NUMS_OF_EXECUTION} iterations")
print(f"OUTPUT:\t\t{'disabled' if SHOW_OUTPUT is False else 'enabled'}")

for i in range(0, NUMS_OF_EXECUTION):
    if USE_PROFILER:
        profiler.run("solution.solve()")
    else:
        solution.solve()
solution.timer_stop()

if USE_PROFILER:
    if SHOW_PROFILER_STATS:
        profiler.print_stats(sort='calls')
    profiler.disable()
