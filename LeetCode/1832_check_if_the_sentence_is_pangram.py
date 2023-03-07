#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/check-if-the-sentence-is-pangram/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Solution function goes here
        """
        result = 0
        return result


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.checkIfPangram(
    sentence="thequickbrownfoxjumpsoverthelazydog"), True)
solution.test(solution.checkIfPangram(sentence="leetcode"), False)
