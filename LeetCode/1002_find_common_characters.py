#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
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

    def commonChars(self, words: List[str]) -> List[str]:
        """
        Solution function goes here
        """
        common_characters = []
        for c in list(words[0]):
            i = 0
            for word in words:
                if c in word:
                    i += 1
            if i == (len(words) - 1):
                common_characters.append(c)
        return common_characters

solution = Solution()
solution.test(solution.commonChars(["bella","label","roller"]), ["e","l","l"])
solution.test(solution.commonChars(["cool","lock","cook"]), ["c","o"])
