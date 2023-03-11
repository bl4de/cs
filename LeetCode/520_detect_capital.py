#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/detect-capital/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def detectCapitalUse(self, word: str) -> bool:
        """
        Solution function goes here
        """
        result = 0
        return result


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.detectCapitalUse(word="USA"), True)
solution.test(solution.detectCapitalUse(word="FlaG"), False)

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
