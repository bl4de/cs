#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/valid-mountain-array/description/
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
        self.test(self.solution(arr=[2, 1]), False)
        self.test(self.solution(arr=[3, 5, 5]), False)
        self.test(self.solution(arr=[0, 3, 2, 1]), True)
        self.test(self.solution(arr=[0,1,2,1,2]), False)
        self.test(self.solution(arr=[0,1,2,4,2,1]), True)

    def solution(self, arr: List[int]) -> bool:
        """
        Solution function goes here
        """
        trend = ""
        current = arr[0]
        for i in range(1, len(arr)):
            if current == arr[i]:
                return False
            
            if current > arr[i]:
                if trend == "":
                    trend = "up"
                else:
                    if trend == "down":
                        return False
            if current < arr[i]:
                if trend == "":
                    return False
                trend = "down"
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
