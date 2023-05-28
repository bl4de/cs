#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/power-of-three/
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
        self.test(self.solution(27), True)
        self.test(self.solution(0), False)
        self.test(self.solution(9), True)
        self.test(self.solution(-1), False)
        self.test(self.solution(1), True)
        self.test(self.solution(3), True)
        
        

    def solution(self, n: int) -> bool:
        """
        Solution function goes here
        """
        p = 0
        while p < 31:
            if pow(3, p) == n:
                return True
            p += 1
        return False

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
