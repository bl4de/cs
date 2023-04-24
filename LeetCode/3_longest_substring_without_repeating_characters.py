#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
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
        self.test(self.solution(s = "abcabcbb"), 3)
        self.test(self.solution(s = "bbbbb"), 1)
        self.test(self.solution(s = "pwwkew"), 3)

    def solution(self, s: str) -> int:
        """
        Solution function goes here
        """
        longest_substring = s[0]
        for iterator in range(1, len(s)):
            for length in range(2, len(s) - iterator):
                print(s[iterator:length])
                if (set(s[iterator:length])) == s[iterator:length]:
                    longest_substring = s[iterator:length]
        return len(longest_substring)

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
