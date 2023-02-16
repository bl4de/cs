#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/decompress-run-length-encoded-list/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        """
        Solution function goes here
        """
        result = []
        return []


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.decompressRLElist([1, 2, 3, 4]), [2, 4, 4, 4])
solution.test(solution.decompressRLElist([1, 1, 2, 3]), [1, 3, 3])
