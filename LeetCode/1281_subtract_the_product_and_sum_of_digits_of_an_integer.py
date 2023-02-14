#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""
from typing import List, Optional
import string
import sys


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

    def subtractProductAndSum(self, n: int) -> int:
        """
        Solution function goes here
        """
        digits = [int(d) for d in str(n)]
        product = digits[0]
        for d in digits[1:]:
            product = product * d
        return product - sum(digits)


sys.setrecursionlimit(1000)
solution = Solution()
solution.test(solution.subtractProductAndSum(234), 15)
solution.test(solution.subtractProductAndSum(4421), 21)
