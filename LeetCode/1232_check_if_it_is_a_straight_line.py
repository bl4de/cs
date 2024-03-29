#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/check-if-it-is-a-straight-line
"""
from typing import List, Optional
import string
import sys
import cProfile
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):

    def __init__(self, show_output=True) -> None:
        self.SHOW_OUTPUT = show_output
        super().__init__()

    def solve(self):
        """
        Solution runner called from profiler
        """
        self.test(self.solution(coordinates=[[1, 2], [2, 3], [
                  3, 4], [4, 5], [5, 6], [6, 7]]), True)
        self.test(self.solution(coordinates=[[1, 1], [2, 2], [
                  3, 4], [4, 5], [5, 6], [7, 7]]), False)
        self.test(self.solution(coordinates=[[0, 0], [0, 1], [0, -1]]), True)
        self.test(self.solution(coordinates=[[2, 1], [4, 2], [6, 3]]), True)

    def solution(self, coordinates: List[List[int]]) -> bool:
        """
        Solution function goes here
        """
        # if one of the coords is 0 in all points, line lies on X or Y
        X = True
        Y = True
        for coordinate in coordinates:
            if coordinate[0] != 0:
                X = False
            if coordinate[1] != 0:
                Y = False

        if X is True or Y is True:
            return True

        # if not, the line is straight if all of points are the solution
        # to the equation y = x - diff, where diff is the difference between
        # X and Y of first point:
        diff = coordinates[0][1] - coordinates[0][0]

        for coordinate in coordinates[1:]:
            if coordinate[1] - coordinate[0] != diff:
                return False
        return True


SHOW_OUTPUT = True
NUMS_OF_EXECUTION = 1
SHOW_PROFILER_STATS = True

sys.setrecursionlimit(1000)
profiler = cProfile.Profile()
solution = Solution(SHOW_OUTPUT)

solution.timer_start()
profiler.enable()
print(f"\nRUNNING:\t{NUMS_OF_EXECUTION} iterations")
print(f"OUTPUT:\t\t{'disabled' if SHOW_OUTPUT is False else 'enabled'}")
for i in range(0, NUMS_OF_EXECUTION):
    profiler.run("solution.solve()")
solution.timer_stop()

if SHOW_PROFILER_STATS:
    profiler.print_stats(sort='calls')
profiler.disable()
