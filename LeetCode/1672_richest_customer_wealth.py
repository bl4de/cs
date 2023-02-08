#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/richest-customer-wealth/description/
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

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Solution function goes here
        """
        result = 0
        return max([sum(account) for account in accounts if sum(account) > result])


solution = Solution()
solution.test(solution.maximumWealth([[1, 2, 3], [3, 2, 1]]), 6)
solution.test(solution.maximumWealth([[1, 5], [7, 3], [3, 5]]), 10)
solution.test(solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 17)
