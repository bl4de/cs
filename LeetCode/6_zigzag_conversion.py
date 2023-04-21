#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/zigzag-conversion/
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
        # self.test(self.solution(s="PAYPALISHIRING",
        #           numRows=3), "PAHNAPLSIIGYIR")
        # P   A   H   N
        # A P L S I I G
        # Y   I   R

        # self.test(self.solution(s="PAYPALISHIRING",
        #           numRows=4), "PINALSIGYAHRPI")
        # # P     I    N
        # # A   L S  I G
        # # Y A   H R
        # # P     I

        # self.test(self.solution(s="A", numRows=1), "A")
        # # A

        self.test(self.solution(s="AB", numRows=1), "AB")
        
    def solution(self, s: str, numRows: int) -> str:
        """
        Solution function goes here
        """
        result = ""
        rows = [None] * numRows
        for row in range(len(rows)):
            rows[row] = [None] * ((len(s) // 2) + 1)

        print(rows)
        c = 0
        row = 0
        col = 0
        direction = 'down'
        for c in s:
            if direction == 'up':
                col = col + 1
            rows[row][col] = c

            if row == (numRows - 1):
                direction = 'up'
            if row == 0:
                direction = 'down'
            row = row + 1 if direction == 'down' else row - 1

        for r in rows:
            result += "".join([c for c in r if c is not None])
        return result


NUMS_OF_EXECUTION = 1
SHOW_PROFILER_STATS = False

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
