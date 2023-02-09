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

    def minimumSum(self, num: int) -> int:
        """
        Solution function goes here
        """
        result = 0
        digits = [int(digit) for digit in list(str(num))]
        print(digits)
        return result

solution = Solution()
solution.test(solution.minimumSum(2932), 52)
solution.test(solution.minimumSum(4009), 13)

