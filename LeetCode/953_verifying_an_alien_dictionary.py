#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/verifying-an-alien-dictionary/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        Solution function goes here
        """
        result = True

        for word in words:

        return result


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.isAlienSorted(
    words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"), True)
solution.test(solution.isAlienSorted(
    words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"), False)
solution.test(solution.isAlienSorted(
    words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"), False)
