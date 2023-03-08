#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        Solution function goes here
        """
        return "".join(word1) == "".join(word2)


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.arrayStringsAreEqual(
    word1=["ab", "c"], word2=["a", "bc"]), True)
solution.test(solution.arrayStringsAreEqual(
    word1=["a", "cb"], word2=["ab", "c"]), False)
solution.test(solution.arrayStringsAreEqual(
    ["abc", "d", "defg"], word2=["abcddefg"]), True)


solution.timer_start()
for i in range(0, 1000000):
    solution.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"])
    solution.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"])
    solution.arrayStringsAreEqual(["abc", "d", "defg"], word2=["abcddefg"])
solution.timer_stop()
