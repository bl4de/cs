# !/usr/bin/env python3 pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,
# missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
"""
from typing import List, Optional


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

    def addDigits(self, num: int) -> int:
        """
        Solution function goes here
        """
        while num > 9:
            num = sum([int(number) for number in [d for d in str(num)]])
        return num


solution = Solution()
solution.test(solution.addDigits(38), 2)
solution.test(solution.addDigits(0), 0)
