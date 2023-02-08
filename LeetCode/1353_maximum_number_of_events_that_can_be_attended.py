#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/
"""
from array import array
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

    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Solution function goes here
        """
        result = 0
        end_day = 0
        for event in events:
            end_day = event[1] if event[1] > end_day else end_day
        available_days = {i: True for i in range(1, end_day + 1)}
        for event in events:
            if available_days[event[1]]:
                available_days[event[1]] = False
            else:
                if available_days[event[0]]:
                    available_days[event[0]] = False
        for d in available_days.values():
            if d is False:
                result += 1
        return result


solution = Solution()
solution.test(solution.maxEvents([[1, 2], [2, 3], [3, 4]]), 3)
solution.test(solution.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]]), 4)
solution.test(solution.maxEvents([[1, 2], [2, 2], [3, 3], [3, 4], [3, 4]]), 4)
