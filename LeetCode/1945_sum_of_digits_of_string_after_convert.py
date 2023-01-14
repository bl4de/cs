#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
'''
    LeetCode solution class
'''
from typing import List, Optional
import string


class Solution:
    '''
    LeetCode solution class
    '''
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

    def getLucky(self, s: str, k: int) -> int:
        """
        Solution function goes here
        """
        result = 0
        s = "".join([str(list(string.ascii_lowercase).index(letter) + 1) for letter in s])
        while k > 0:
            result = sum([int(d) for d in s])
            s = str(result)
            k -= 1
        return result


solution = Solution()
solution.test(solution.getLucky("iiii", 1), 36)
solution.test(solution.getLucky("leetcode", 2), 6)
solution.test(solution.getLucky("zbax", 2), 8)
