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
        rods = {}
        for rod in range(0, 10):
            if rings.count(str(rod)) < 3:
                continue
            rods[str(rod)] = []

        rings = list(rings)
        rings.reverse()

        for iterator in range(0, len(rings), 2):
            if rings[iterator] in rods.keys():
                rods[rings[iterator]].append(rings[iterator + 1])

        for rod, rings in rods.items():
            if len(set(rings)) == 3:
                result += 1
        return result


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.countPoints(
    rings="B0B6G0R6R0R6G9"), 1)
solution.test(solution.countPoints(
    rings="B0R0G0R9R0B0G0"), 1)
solution.test(solution.countPoints("G4"), 0)
