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
        for i in range(len(nums), 0, -1):
            n = nums.pop()
            if target > n:
                return i
        return 0


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))  # 2
print(solution.searchInsert([1, 3, 5, 6], 2))  # 1
print(solution.searchInsert([1, 3, 5, 6], 7))  # 4
print(solution.searchInsert([1], 0))  # 0
print(solution.searchInsert([1, 3], 2))  # 1
print(solution.searchInsert([1, 3], 0))  # 0
print(solution.searchInsert([1, 3, 5], 2))  # 1
