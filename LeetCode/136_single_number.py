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

    def singleNumber(self, nums: List[int]) -> int:
        existings = {
            "1": [],
            "2": []
        }
        while len(nums) > 0:
            n = nums.pop()
            if n in existings["1"]:
                existings["2"].append(n)
                existings["1"].remove(n)
            else:
                existings["1"].append(n)
        # should be only one element
        return existings["1"][0]

solution = Solution()
print(solution.singleNumber([2, 2, 1]))  # 1
print(solution.singleNumber([4, 1, 2, 1, 2]))  # 1
print(solution.singleNumber([1]))  # 1
