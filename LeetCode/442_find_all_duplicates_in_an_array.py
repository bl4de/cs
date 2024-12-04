#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
"""
import cProfile
import sys
from typing import List

from abstract_solution import AbstractSolution


class Solution(AbstractSolution):

    def __init__(self, show_output=True) -> None:
        self.SHOW_OUTPUT = show_output
        super().__init__()

    def solve(self, nums: List[int]) -> List[int]:
        """
        Solution runner called from profiler
        """
        self.test(self.solution(nums=[4, 3, 2, 7, 8, 2, 3, 1]), [2, 3])
        self.test(self.solution(nums=[1, 1, 2]), [1])
        self.test(self.solution([1]), [])

    def solution(self):
        """
        Solution function goes here
        """
        result = 0
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
