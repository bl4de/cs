#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/word-pattern/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Solution function goes here
        """

        return True


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.wordPattern(pattern="abba", s="dog cat cat dog"), True)
solution.test(solution.wordPattern(
    pattern="abba", s="dog cat cat fish"), False)
solution.test(solution.wordPattern(pattern="aaaa", s="dog cat cat dog"), False)
