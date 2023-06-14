#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/reverse-string/
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
        self.test(self.solution(s=["h", "e", "l", "l", "o"]), [
                  "o", "l", "l", "e", "h"])
        self.test(self.solution(s=["H", "a", "n", "n", "a", "h"]), [
                  "h", "a", "n", "n", "a", "H"])

    def solution(self, s: List[str]) -> None:
        """
        Solution function goes here
        """
        l = len(s) - 1
        i = 0
        while i < l:
            tmp = s[i]
            s[i] = s[l]
            s[l] = tmp
            l -= 1
            i += 1
        return s


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
