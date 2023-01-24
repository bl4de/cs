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
        spec = words.pop()
        common_characters = list(spec)
        for word in words:
            for c in spec:
                if c not in word and c in common_characters:
                    common_characters.remove(c)

        return common_characters


solution = Solution()
solution.test(solution.commonChars(["bella", "label", "roller"]), ["e", "l", "l"])
solution.test(solution.commonChars(["cool", "lock", "cook"]), ["c", "o"])
