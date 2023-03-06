#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def areOccurrencesEqual(self, s: str) -> bool:
        """
        Solution function goes here
        """
        result = 0
        return result


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.areOccurrencesEqual(s="abacbc"), True)
solution.test(solution.areOccurrencesEqual(s="aaabb"), False)
