#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def reverseWords(self, s: str) -> str:
        """
        Solution function goes here
        """
        result = []
        for word in s.split():
            r = [c for c in word]
            r.reverse()
            result.append("".join(r))
        return " ".join(result)


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.reverseWords(
    s="Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")
solution.test(solution.reverseWords(s="God Ding"), "doG gniD")
