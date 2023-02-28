#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/verifying-an-alien-dictionary/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        Solution function goes here
        """
        for iterator in range(1, len(words)):
            character_index = 0
            if order.index(words[iterator-1][character_index]) < order.index(words[iterator][character_index]):
                return True
            else:
                max_length = len(words[iterator]) if len(words[iterator]) < len(
                    words[iterator-1]) else len(words[iterator-1])

                while character_index < max_length:
                    if order.index(words[iterator-1][character_index]) < order.index(words[iterator][character_index]):
                        return True
                    character_index += 1
        return False


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.isAlienSorted(
    words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"), True)
solution.test(solution.isAlienSorted(
    words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"), False)
solution.test(solution.isAlienSorted(
    words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"), False)
