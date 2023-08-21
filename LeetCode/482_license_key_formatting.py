#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/license-key-formatting/
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
        self.test(self.solution(s = "5F3Z-2e-9-w", k = 4), "5F3Z-2E9W")
        self.test(self.solution(s = "2-5g-3-J", k = 2), "2-5G-3J")
        self.test(self.solution(s = "2-4A0r7-4k", k = 4), "24A0-R74K")

    def solution(self, s: str, k: int) -> str:
        """
        Solution function goes here
        """
        result = s.split("-")[0] + "-"
        start = s.index("-") + 1
        
        counter = 0
        for i in range(start, len(s)):
            counter += 1
            
            if s[i] != "-":
                result += s[i]
                
            if counter == k:
                result += "-"
                counter = 0
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
