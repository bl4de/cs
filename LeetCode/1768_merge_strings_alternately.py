#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/merge-strings-alternately/
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
        self.test(self.solution(word1 = "abc", word2 = "pqr"), "apbqcr")
        self.test(self.solution(word1 = "ab", word2 = "pqrs"), "apbqrs")
        self.test(self.solution(word1 = "abcd", word2 = "pq"), "apbqcd")

    def solution(self, word1: str, word2: str) -> str:
        """
        Solution function goes here
        """
        result = ""
        l = word2 if len(word1) > len(word2) else word1
        for i in range(0, l):
            result += word1[i]
            result += word2[i]
        if len(word1) > len(word2):
            result += word1[l:]
        else:
            result += word2[l:]
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
