#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
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
        self.test(self.solution(), None)

    def solution(self):
        """
        Solution function goes here
        """
        result = 0
        return result

NUMS_OF_EXECUTION = 1

sys.setrecursionlimit(1000)
profiler = cProfile.Profile()
solution = Solution()

solution.timer_start()
profiler.enable()
for i in range(0, NUMS_OF_EXECUTION):
    profiler.run("solution.solve()")
solution.timer_stop()

profiler.print_stats()
profiler.disable()
