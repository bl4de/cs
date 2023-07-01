#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/counting-bits/
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
        self.test(self.solution(n=2), [0, 1, 1])
        self.test(self.solution(n=5), [0, 1, 1, 2, 1, 2])

    def solution(self, n: int) -> List[int]:
        """
        Solution function goes here
        """
        bits = {}
        for i in range(1, n + 1):
            iterator = 0
            for bit in bin(i)[::-1]:
                if str(iterator) not in bits.keys():
                    bits[str(iterator)] = 0
                bits[str(iterator)] = bits[str(iterator)] + 1 if bit == '1' else bits[str(iterator)]
                iterator += 1
        result =  list(bits.values())
        result.reverse()
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
