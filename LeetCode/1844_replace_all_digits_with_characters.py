#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/replace-all-digits-with-characters/
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
        self.test(self.solution(s = "a1c1e1"), "abcdef")
        self.test(self.solution(s = "a1b2c3d4e"), "abbdcfdhe")

    def solution(self, s: str) -> str:
        """
        Solution function goes here
        """
        result = ""
        for c in s:
            if c in string.digits:
                c = chr(ord(c) + 49)
            result += c
        return result


sys.setrecursionlimit(1000)
profiler = cProfile.Profile()
solution = Solution()

solution.timer_start()
profiler.enable()
for i in range(0, 1):
    profiler.run("solution.solve()")
solution.timer_stop()

profiler.print_stats()
profiler.disable()
