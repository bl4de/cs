#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/longest-uncommon-subsequence-i/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def findLUSlength(self, a: str, b: str) -> int:
        """
        Solution function goes here
        """
        result = 0
        return result


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.findLUSlength(a="aba", b="cdc"), 3)
solution.test(solution.findLUSlength(a="aaa", b="bbb"), 3)
solution.test(solution.findLUSlength(a="aaa", b="aaa"), -1)

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
