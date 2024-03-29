#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/longest-palindromic-substring/
"""
from typing import List, Optional
import string
import re
import sys
import cProfile
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):

    def solve(self):
        """
        Solution runner called from profiler
        """
        self.test(self.solution(s="babad"), "bab")
        self.test(self.solution(s="cbbd"), "bb")
        self.test(self.solution(s="bb"), "bb")
        self.test(self.solution(s="abb"), "bb")

    def solution(self, s: str) -> str:
        if len(s) < 2:
            return s

        if (s == s[::-1]) is True:
            return s
        
        result = ""
        tmp = ""
        for i in range(len(s)):
            for iterator in range(i + 1, len(s) + 1):
                tmp = s[i:iterator]
                if len(tmp) > len(result):
                    if (tmp == tmp[::-1]) is True:
                        result = tmp
                        tmp = ""
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
