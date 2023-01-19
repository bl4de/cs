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

    def maximumDifference(self, nums: List[int]) -> int:
        """
        Solution function goes here
        """
        max_diff = -1
        current_max = -1

        while len(nums) > 2:
            max_num = max(nums)
            max_pos = nums.index(max_num)
            min_num = min(nums)
            min_pos = nums.index(min_num)
            if min_pos < max_pos:
                current_max = max_num = min_num
                max_diff = current_max if (
                    current_max > max_diff) else max_diff
            nums.remove(max_num)
            nums.remove(min_num)
            print(current_max)

        return max_diff


solution = Solution()
solution.test(solution.maximumDifference([7, 1, 5, 4]), 4)
solution.test(solution.maximumDifference([9, 4, 3, 2]), -1)
solution.test(solution.maximumDifference([1, 5, 2, 10]), 9)
