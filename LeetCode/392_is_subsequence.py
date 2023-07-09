#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/is-subsequence/
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
        self.test(self.solution(s="abc", t="ahbgdc"), True)
        self.test(self.solution(s="axc", t="ahbgdc"), False)
        self.test(self.solution(s="acb", t="ahbgdc"), False)

    def solution(self, s: str, t: str) -> bool:
        """
        Solution function goes here
        """
        s_arr = list(s)
        t_arr = list(t)

        t_len = len(t)
        s_len = len(s)

        result = []

        for j in range(0, s_len):
            for i in range(j, t_len):
                if s_arr[j] == t_arr[i]:
                    result.append(s_arr[j])
                    continue
        return "".join(result) == s


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
