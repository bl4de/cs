#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/word-pattern/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):

    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Solution function goes here
        """
        dictionary = {}

        characters = list(pattern)
        words = s.split()

        if len(characters) != len(words):
            return False

        for index, character in enumerate(characters):
            if words[index] not in dictionary.keys() and character not in dictionary.values():
                dictionary[words[index]] = character
            if words[index] in dictionary.keys() and dictionary[words[index]] != character:
                return False
            if words[index] not in dictionary.keys() and character in dictionary.values():
                return False
        return True


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.wordPattern(pattern="abba", s="dog cat cat dog"), True)
solution.test(solution.wordPattern(
    pattern="abba", s="dog cat cat fish"), False)
solution.test(solution.wordPattern(pattern="aaaa", s="dog cat cat dog"), False)
