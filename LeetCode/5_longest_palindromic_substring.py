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

    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        return s == s[::-1]

    def solution(self, s: str) -> str:
        """
        Solution function goes here
        """
        if self.isPalindrome(s):
            return s

        result = ""
        tmp = ""
        for i in range(len(s)):
            for iterator in range(1, len(s)):
                tmp = s[i:i+iterator]
                if self.isPalindrome(tmp) is True and len(tmp) > len(result):
                    result = tmp
                    tmp = ""

        return result


sys.setrecursionlimit(1000)
profiler = cProfile.Profile()
solution = Solution()

solution.timer_start()
profiler.enable()
for i in range(0, 100):
    profiler.run("solution.solve()")
solution.timer_stop()

profiler.print_stats(sort='calls')
profiler.disable()
