#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/sorting-the-sentence/
"""
from typing import List, Optional
import string

class Solution:
    """
    LeetCode solution class
    """
    colors = {
        "black": '\33[30m',
        "red": '\33[31m',
        "green": '\33[32m',
        "yellow": '\33[33m',
        "blue": '\33[34m',
        "magenta": '\33[35m',
        "cyan": '\33[36m',
        "white": '\33[37m',
        "grey": '\33[90m',
        "lightblue": '\33[94m'
    }
    endline = '\33[0m'
    PASS = f"{colors['green']}[+] PASS {endline}"
    FAIL = f"{colors['red']}[+] FAIL {endline}"

    def test(self, provided, expected) -> bool:
        """
        Compares provided result to expected
        Returns true if equal
        """
        print(f"\n output  : {provided}\n expected: {expected}")
        print(f" {self.PASS if provided == expected else self.FAIL}")
        return provided == expected

    def sortSentence(self, s: str) -> str:
        """
        Solution function goes here
        """
        d = {}
        for word in s.split(" "):
            d[int(word[-1:])] = word[0:-1]
        return " ".join([word for index, word in (sorted(d.items()))])



solution = Solution()
solution.test(solution.sortSentence("is2 sentence4 This1 a3"), "This is a sentence")
solution.test(solution.sortSentence("Myself2 Me1 I4 and3"), "Me Myself and I")
