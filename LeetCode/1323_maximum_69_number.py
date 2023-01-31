#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/maximum-69-number/
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

    def maximum69Number(self, num: int) -> int:
        """
        Solution function goes here
        """
        num = list(str(num))
        for index, digit in enumerate(num):
            if digit == '6':
                num[index] = '9'
                return int("".join(num))
        return int("".join(num))


solution = Solution()
solution.test(solution.maximum69Number(9669), 9969)
solution.test(solution.maximum69Number(9996), 9999)
solution.test(solution.maximum69Number(9999), 9999)
