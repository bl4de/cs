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

    def solution(self, arr: List[int]) -> bool:
        """
        Solution function goes here
        """
        trend = []
        current = arr[0]
        for i in range(1, len(arr)):
            if arr[i] == current:
                return False
            
            if arr[i] < current and (len(trend) == 1 and 'down' not in trend and trend[0] == 'up'):
                trend.append('down')
            else:
                if arr[i] > current and 'up' not in trend:
                    trend.append('up')
                else:
                    return False
            current = arr[i]
        print(trend)
        return len(trend) == 2 and trend == ['up', 'down']


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
