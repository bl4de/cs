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
        if len(nums) == 1:
            if nums[0] - 1 > -1:
                return nums[0] - 1
            else:
                return nums[0] + 1
        missing_number = 0
        nums = sorted(nums)
        nums.append(1000000)  # fill last element
        for i, _ in enumerate(nums):
            if (nums[i] + 1) != nums[i+1]:
                missing_number = nums[i] + 1
                return missing_number
        return missing_number


solution = Solution()
print(solution.missingNumber([3, 0, 1]))  # 2
print(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
print(solution.missingNumber([0, 1]))  # 2
print(solution.missingNumber([1]))  # 0
