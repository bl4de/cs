#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/count-the-number-of-consistent-strings/
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

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        Solution function goes here
        """
        result = 0
        for word in words:
            current_word = 0
            for c in word:
                if c in allowed:
                    current_word += 1
            if current_word == len(word):
                result += 1
        return result


solution = Solution()
solution.test(solution.countConsistentStrings("fstqyienx",
                                              ["n", "eeitfns", "eqqqsfs", "i", "feniqis", "lhoa", "yqyitei", "sqtn",
                                               "kug", "z", "neqqis"]), 8)
