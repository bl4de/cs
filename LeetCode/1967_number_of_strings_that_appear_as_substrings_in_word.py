#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """
        Solution function goes here
        """
        result = 0
        for pattern in patterns:
            if pattern in word:
                result += 1
        return result


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.numOfStrings(
    patterns=["a", "abc", "bc", "d"], word="abc"), 3)
solution.test(solution.numOfStrings(
    patterns=["a", "b", "c"], word="aaaaabbbbb"), 2)
solution.test(solution.numOfStrings(patterns=["a", "a", "a"], word="ab"), 3)

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
