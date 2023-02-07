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

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Solution function goes here
        """
        return sum([stones.count(jewel) for jewel in jewels])

solution = Solution()
solution.test(solution.numJewelsInStones("aA", "aAAbbbb"), 3)
solution.test(solution.numJewelsInStones("z","ZZ"), 0)

