#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/first-letter-to-appear-twice/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def repeatedCharacter(self, s: str) -> str:
        """
        Solution function goes here
        """
        characters = []
        for c in s:
            if c in characters:
                return c
            characters.append(c)
        return ''

sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.repeatedCharacter("abccbaacz"), "c")
solution.test(solution.repeatedCharacter("abcdd"), "d")
