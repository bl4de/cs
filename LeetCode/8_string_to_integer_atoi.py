#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/string-to-integer-atoi/
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
        self.test(self.solution(s = "42"), 42)
        self.test(self.solution(s = "   -42"), -42)
        self.test(self.solution(s = "4193 with words"), 4193)
        

    def solution(self, s: str) -> int:
        """
        Solution function goes here
        """
        result = []
        is_negative = False
        for c in s:
            if c not in string.digits:
                if c == '-':
                    is_negative = True
                continue
            result.append(c)
        result = int("".join(result))
        return result if is_negative is False else result * -1

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
