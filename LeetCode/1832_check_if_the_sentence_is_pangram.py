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
        if len(set(sentence)) < 26:
            return False
        for c in string.ascii_lowercase:
            if c not in sentence:
                return False
        return True


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.checkIfPangram(
    sentence="thequickbrownfoxjumpsoverthelazydog"), True)
solution.test(solution.checkIfPangram(sentence="leetcode"), False)
