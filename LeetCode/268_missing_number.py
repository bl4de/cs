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

    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums) + 1):
            if i not in nums:
                return i
        return 0


solution = Solution()
print(solution.missingNumber([3, 0, 1]))  # 2
print(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
print(solution.missingNumber([0, 1]))  # 2
print(solution.missingNumber([1]))  # 0
