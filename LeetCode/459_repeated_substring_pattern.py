#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/repeated-substring-pattern/description/
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
        self.test(self.solution(s = "abab"), True)
        self.test(self.solution(s = "aba"), False)
        self.test(self.solution(s = "abcabcabcabc"), True)

    def solution(self, s: str) -> bool:
        """
        Solution function goes here
        """
        result = False
        # can't create repeated string from substring if string len is odd:
        if len(s) % 2 != 0:
            return False
            
        return result

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
