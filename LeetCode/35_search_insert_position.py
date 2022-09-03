#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, no-self-use,missing-function-docstring
'''
    LeetCode solution class
'''
from typing import List


class Solution:
    '''
    LeetCode solution class
    '''

    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0

        if len(nums) == 1:
            return 0 if target <= nums[0] else 1

        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        for _index, num in enumerate(nums):
            if num == target:
                return _index
            if num > target and num < nums[_index + 1]:
                return _index
            i = _index
        return i + 1


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))  # 2
print(solution.searchInsert([1, 3, 5, 6], 2))  # 1
print(solution.searchInsert([1, 3, 5, 6], 7))  # 4
print(solution.searchInsert([1], 0))  # 0
print(solution.searchInsert([1, 3], 2))  # 1
print(solution.searchInsert([1, 3], 0))  # 0
print(solution.searchInsert([1, 3, 5], 2))  # 1
