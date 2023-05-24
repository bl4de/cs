#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/longest-valid-parentheses/
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
        self.test(self.solution(s="(()"), 2)
        self.test(self.solution(s=")("), 0)
        self.test(self.solution(s=")()())"), 4)
        self.test(self.solution(s=""), 0)

    def solution(self, s: str) -> int:
        """
        Solution function goes here
        """
        if len(s) < 2:
            return 0

        result = longest = 0

        _next = "("

        for pos in range(1, len(s)):
            if _next == "(":
                if s[pos] == "(":
                    result += 1
                    _next = ")"
                else:
                    _next = "("
                continue
            if _next == ")":
                if s[pos] == ")":
                    result += 1
                    _next = "("
                else:
                    _next = ")"
                continue
            if (_next == ")" and s[pos] == "(") or (_next == "(" and s[pos] == ")"):
                longest = result if result > longest else longest

        return longest


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
