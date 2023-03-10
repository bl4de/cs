#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/capitalize-the-title/description/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def capitalizeTitle(self, title: str) -> str:
        """
        Solution function goes here
        """
        result = []
        for word in title.split(" "):
            result.append(word.lower() if len(word) <=
                          2 else word.lower().capitalize())
        return " ".join(result)


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.capitalizeTitle(
    title="capiTalIze tHe titLe"), "Capitalize The Title")
solution.test(solution.capitalizeTitle(
    title="First leTTeR of EACH Word"), "First Letter of Each Word")
solution.test(solution.capitalizeTitle(
    title="i lOve leetcode"), "i Love Leetcode")

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
