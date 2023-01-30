#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
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

    def countKDifference(self, nums: List[int], k: int) -> int:
        """
        Solution function goes here
        """
        result = 0
        for n in nums:
            if n + k in nums:
                result += 1
            if k - n in nums:
                result += 1
        return result

solution = Solution()
solution.test(solution.countKDifference([1, 2, 2, 1], 1), 4)
solution.test(solution.countKDifference([1, 3], 3), 0)
solution.test(solution.countKDifference([3, 2, 1, 5, 4], 2), 3)
