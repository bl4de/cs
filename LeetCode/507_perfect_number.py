#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/perfect-number/description/
"""
from typing import List, Optional
import string
import sys
import math
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def checkPerfectNumber(self, num: int) -> bool:
        """
        Solution function goes here
        """
        divisors = [1]
        iterations = 0
        for d in range(2, round(num / 2)):
            if d not in divisors and num % d != 0:
                continue
            divisors.append(d)
            divisors.append(num//d)
            iterations += 1
        print(f"\n{num} : {set(divisors)}  -> {iterations}")
        return sum(set(divisors)) == num


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.checkPerfectNumber(num=28), True)
solution.test(solution.checkPerfectNumber(num=7), False)
solution.test(solution.checkPerfectNumber(num=6), True)
solution.test(solution.checkPerfectNumber(num=99999993), False)  # test case: 59 / 98
