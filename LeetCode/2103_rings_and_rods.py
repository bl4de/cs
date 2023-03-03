#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/rings-and-rods/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def countPoints(self, rings: str) -> int:
        """
        Solution function goes here
        """
        result = 0
        return result


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.countPoints("B0B6G0R6R0R6G9"), 1)
solution.test(solution.countPoints("G4"), 0)
