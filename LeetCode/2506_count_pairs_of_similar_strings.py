#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/count-pairs-of-similar-strings/description/
"""
from typing import List, Optional
import string


class Solution:
    """
    LeetCode solution class
    """
    endline = '\33[0m'
    green = '\33[32m'
    red = '\33[31m'
    PASS = f"{green}[+] PASS {endline}"
    FAIL = f"{red}[+] FAIL {endline}"

    def test(self, provided, expected) -> bool:
        """
        Compares provided result to expected
        """
        print(f"\n output  : {provided}\n expected: {expected}")
        print(f" {self.PASS if provided == expected else self.FAIL}")
        return provided == expected

    def similarPairs(self, words: List[str]) -> int:
        """
        Solution function goes here
        """
        result = 0
        for index_one, word_one in enumerate(words):
            word_one_character_set = set(list(word_one))
            for index_two, word_two in enumerate(words):
                if index_one != index_two:
                    word_two_character_set = set(list(word_two))
                    result = result + 1 if word_one_character_set == word_two_character_set else result
        return result // 2


solution = Solution()
solution.test(solution.similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]), 2)
solution.test(solution.similarPairs(["aabb", "ab", "ba"]), 3)
solution.test(solution.similarPairs(["nba", "cba", "dba"]), 0)
solution.test(solution.similarPairs(
    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
     "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
     "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
     "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
     "a", "a", "a", "a", "a", "a", "a", "a"]), 4950)
