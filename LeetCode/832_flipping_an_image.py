#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/flipping-an-image/
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
        self.test(self.solution(image=[[1, 1, 0], [1, 0, 1], [0, 0, 0]]), [
                  [1, 0, 0], [0, 1, 0], [1, 1, 1]])
        self.test(self.solution(image=[[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [
                  1, 0, 1, 0]]), [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]])

    def solution(self, image: List[List[int]]) -> List[List[int]]:
        """
        Solution function goes here
        """
        result = []
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
