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

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == 0 else 1

        max_c = 0
        current_c = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                current_c += 1
                max_c = current_c if current_c >= max_c else max_c
            else:
                current_c = 0
            i += 1
        return max_c


solution = Solution()
solution.debug(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)
solution.debug(solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]), 2)
solution.debug(solution.findMaxConsecutiveOnes([0]), 0)
solution.debug(solution.findMaxConsecutiveOnes([1]), 1)
