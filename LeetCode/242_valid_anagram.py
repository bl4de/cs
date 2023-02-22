#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/valid-anagram/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Solution function goes here
        """
        return sorted(s) == sorted(t)


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.isAnagram(s="anagram", t="nagaram"), True)
solution.test(solution.isAnagram(s="rat", t="car"), False)
