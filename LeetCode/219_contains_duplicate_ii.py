#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/contains-duplicate-ii/
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
        self.test(self.solution(nums=[1, 2, 3, 1], k=3), True)
        self.test(self.solution(nums=[1, 0, 1, 1], k=1), True)
        self.test(self.solution(nums=[1, 2, 3, 1, 2, 3], k=2), False)

    def solution(self, nums: List[int], k: int) -> bool:
        """
        Solution function goes here
        """
        d = {}
        for index, n in enumerate(nums):
            if n not in d:
                d[n] = [index]
            else:
                d[n].append(index)

        for n in d.items():
            if len(n[1]) > 1:
                for _i, x in enumerate(n[1]):
                    for _j, y in enumerate(n[1]):
                        if x != y and nums[x] == nums[y] and abs(x - y) <= k:
                            return True
        return False


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
