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

    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        mid_sum = 0
        for i in range(0, len(nums)):
            mid_sum = mid_sum + nums[i]
            running_sum.append(mid_sum)
        return running_sum


solution = Solution()
print(solution.runningSum([1, 2, 3, 4]))  # [1,3,6,10]
print(solution.runningSum([1, 1, 1, 1, 1]))  # [1,2,3,4,5]
print(solution.runningSum([3, 1, 2, 10, 1]))  # [3,4,6,16,17]
