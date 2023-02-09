#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
"""
from typing import List, Optional
import string
import itertools

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

    def smallest_sum_of_pair(self, digits:List[int]) -> int:
        possible_pairs = [
            (digits[0], int(f"{digits[1]}{digits[2]}{digits[3]}")),
            (int(f"{digits[0]}{digits[1]}"),int(f"{digits[2]}{digits[3]}")),
            (int(f"{digits[0]}{digits[1]}{digits[2]}"), digits[3])
        ]
        smallest_sum = 1008 # 9 + 999 -> maximum sum
        for pair in possible_pairs:
            current_sum = pair[0] + pair[1]
            smallest_sum = current_sum if current_sum < smallest_sum else smallest_sum
        return smallest_sum

    def minimumSum(self, num: int) -> int:
        """
        Solution function goes here
        """
        result = 1008
        digits = [int(digit) for digit in list(str(num))]
        for subset in itertools.permutations(digits):
            current_sum = self.smallest_sum_of_pair(list(subset))
            result = current_sum if current_sum < result else result
        return result

solution = Solution()
solution.test(solution.minimumSum(2932), 52)
solution.test(solution.minimumSum(4009), 13)

