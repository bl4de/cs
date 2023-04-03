#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/sort-the-people/
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
        self.test(self.solution(names=["Mary", "John", "Emma"], heights=[
                  180, 165, 170]), ["Mary", "Emma", "John"])
        self.test(self.solution(["Alice", "Bob", "Bob"], heights=[
                  155, 185, 150]), ["Bob", "Alice", "Bob"])

    def solution(self, names: List[str], heights: List[int]) -> List[str]:
        """
        Solution function goes here
        """
        people = sorted(zip(names, heights), key=lambda p: p[1])
        people.reverse()
        return [name for name, _ in people]


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
