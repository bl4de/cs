#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/longest-palindrome/
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
        self.test(self.solution(s="abccccdd"), 7)
        self.test(self.solution(s="a"), 1)
        self.test(self.solution(s="ccc"), 3)
        self.test(self.solution(s="bananas"), 5)

    def solution(self, s: str) -> int:
        """
        Solution function goes here
        """
        result = 0
        single = False
        characters_set = set(s)
        
        # if s contains only single character, it's always a palindrome
        if len(characters_set) == 1:
            return len(s)
        
        for c in set(s):
            character_counter = s.count(c)
            if character_counter % 2 != 0 and single is False:
                result += character_counter
                single = True # can be only one single character in palindrome
            else:
                if character_counter % 2 == 0:
                    result += character_counter
                else:
                    result += character_counter - 1
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
