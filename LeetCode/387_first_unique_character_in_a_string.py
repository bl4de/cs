#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/first-unique-character-in-a-string/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def firstUniqChar(self, s: str) -> int:
        """
        Solution function goes here
        """
        result = -1
        for c in s:
            if s.count(c) == 1:
                return s.index(c)
        return result


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.firstUniqChar(s="leetcode"), 0)
solution.test(solution.firstUniqChar(s="loveleetcode"), 2)
solution.test(solution.firstUniqChar(s="aabb"), -1)
