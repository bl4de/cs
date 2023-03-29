#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/shuffle-the-array/
"""
from typing import List, Optional
import string
import sys
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Solution function goes here
        """
        result = []
        return result


sys.setrecursionlimit(1000)
solution = Solution()

solution.test(solution.shuffle(nums = [2,5,1,3,4,7], n = 3),  [2,3,5,4,1,7] )
solution.test(solution.shuffle(nums = [1,2,3,4,4,3,2,1], n = 4), [1,4,2,3,3,2,4,1])
solution.test(solution.shuffle(nums = [1,1,2,2], n = 2),  [1,2,1,2])

# solution.timer_start()
# for i in range(0, 1000000):
#     pass
# solution.timer_stop()
