#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, no-self-use,missing-function-docstring, unused-wildcart-import
'''
    LeetCode solution class
'''
from typing import List, Optional


class Solution:
    '''
    LeetCode solution class
    '''

    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]


solution = Solution()
print(solution.buildArray([0, 2, 1, 5, 3, 4]))  # [0,1,2,4,5,3]
print(solution.buildArray([5, 0, 1, 2, 3, 4]))  # [4,5,0,1,2,3]
