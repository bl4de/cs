#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/delete-greatest-value-in-each-row/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        """
        Solution function goes here
        """
        result = 0
        while len(grid[0]) > 0:
            max_val = 0
            for row in grid:
                max_row_val = max(row)
                max_val = max_row_val if max_row_val > max_val else max_val
                row.pop(row.index(max_row_val))
            result += max_val
        return result


sys.setrecursionlimit(1000)
solution = Solution()

# solution.test(solution.deleteGreatestValue(grid=[[1, 2, 4], [3, 3, 1]]), 8)
# solution.test(solution.deleteGreatestValue(grid=[[10]]), 10)

solution.timer_start()
for i in range(0, 100000):
    solution.deleteGreatestValue(grid=[[1, 2, 4], [3, 3, 1]])
solution.timer_stop()
