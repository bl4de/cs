#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
'''
    LeetCode solution class
'''
from typing import List, Optional


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

    def debug(self, provided, expected) -> bool:
        '''
        Compares provided result to expected
        Returns true if equal
        '''
        print(f"\n output  : {provided}\n expected: {expected}")
        print(f" {self.PASS if provided == expected else self.FAIL}")
        return provided == expected

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller = []
        for num in nums:
            smaller.append(0)
            for n in nums:
                if n < num:
                    smaller[-1] = smaller[-1] + 1
        return smaller


solution = Solution()
assert solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
assert solution.smallerNumbersThanCurrent([6, 5, 4, 8]) == [2, 1, 0, 3]
assert solution.smallerNumbersThanCurrent([7, 7, 7, 7]) == [0, 0, 0, 0]

solution.debug(solution.smallerNumbersThanCurrent(
    [8, 1, 2, 2, 3]), [4, 0, 1, 1, 3])
