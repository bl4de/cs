#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/power-of-four/description/
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
        self.test(self.solution(16), True)
        self.test(self.solution(5), False)
        self.test(self.solution(1), True)

    def solution(self, n: int) -> bool:
        """
        Solution function goes here
        """
        powersOfFour = [
            "00000000000000000000000000000001",
            "00000000000000000000000000000100",
            "00000000000000000000000000010000",
            "00000000000000000000000001000000",
            "00000000000000000000000100000000",
            "00000000000000000000010000000000",
            "00000000000000000001000000000000",
            "00000000000000000100000000000000",
            "00000000000000010000000000000000",
            "00000000000001000000000000000000",
            "00000000000100000000000000000000",
            "00000000010000000000000000000000",
            "00000001000000000000000000000000",
            "00000100000000000000000000000000",
            "00010000000000000000000000000000",
            "01000000000000000000000000000000"
        ]
        print('{:032b}'.format(n))
        return ('{:032b}'.format(n) in powersOfFour)

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
