#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/self-dividing-numbers/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """
        Solution function goes here
        """
        result = []

        for number in range(left, right + 1):
            digits = [int(d) for d in str(number)]
            dividers = []
            if 0 in digits:
                continue

            for d in digits:
                if number % d == 0:
                    dividers.append(d)

            if len(digits) == len(dividers):
                result.append(number)

        return result


sys.setrecursionlimit(1000)
solution = Solution()
# solution.test(solution.selfDividingNumbers(left=11, right=12), [11, 12])

solution.test(solution.selfDividingNumbers(left=1, right=22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])
solution.test(solution.selfDividingNumbers(left=47, right=85), [48, 55, 66, 77])
