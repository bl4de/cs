#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Solution function goes here
        """
        character_map = {}
        for index, c in enumerate(s):
            if c not in character_map.keys() and t[index] not in character_map.values():
                character_map[c] = t[index]

            if c not in character_map.keys() and t[index] in character_map.values():
                return False

            if c in character_map.keys() and character_map[c] != t[index]:
                return False

        return True


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.isIsomorphic(s="egg", t="add"), True)
solution.test(solution.isIsomorphic(s="foo", t="bar"), False)
solution.test(solution.isIsomorphic(s="paper", t="title"), True)
solution.test(solution.isIsomorphic(s="badc", t="baba"), False)
solution.test(solution.isIsomorphic(s="foo", t="bar"), False)
