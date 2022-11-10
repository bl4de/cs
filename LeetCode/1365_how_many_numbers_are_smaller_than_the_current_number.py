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

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller = []

        return smaller


solution = Solution()
print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  # [8,1,2,2,3]
print(solution.smallerNumbersThanCurrent([6, 5, 4, 8]))  # [2,1,0,3]
print(solution.smallerNumbersThanCurrent([7, 7, 7, 7]))  # [0,0,0,0]
