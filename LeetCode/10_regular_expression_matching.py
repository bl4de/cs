#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/regular-expression-matching/
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
        self.test(self.solution(s="aa", p="a"), False)
        self.test(self.solution(s="aa", p="a*"), True)
        self.test(self.solution(s="ab", p=".*"), True)

    def solution(self, s: str, p: str) -> bool:
        """
        Solution function goes here
        """
        # edge cases
        if p == ".*" and len(s) > 0:
            return True
        if p == "." and len(s) == 1:
            return True
        
        result = True
        prev_c = ''
        iterator = 0
        while result:
            # take the character from the string
            c = s[iterator]

            # determine current condition for regex:
            # 1. character - exact match
            # 2. . - match
            # 3. * -  check if previous character was c or .
            # 4. save c as prev_c for next iteration
            
            # check if character matches the condition
            prev_c = c
            
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
