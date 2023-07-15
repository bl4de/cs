#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/fizz-buzz/
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
        self.test(self.solution(n=3), ["1", "2", "Fizz"])
        self.test(self.solution(n=5), ["1", "2", "Fizz", "4", "Buzz"])
        self.test(self.solution(n=15), ["1", "2", "Fizz", "4", "Buzz", "Fizz",
                  "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])

    def solution(self, n: int) -> List[str]:
        """
        Solution function goes here
        """
        result = []
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
