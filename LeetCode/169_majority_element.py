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

    def count_elements(self, nums: List[int], element: int) -> int:
        '''
        Counts occurences of element in nums
        '''
        occurences = 0
        for i in nums:
            if i == element:
                occurences += 1
        return occurences

    def majorityElement(self, nums: List[int]) -> int:
        majority_element = 0
        elements = {}
        occurences = 0
        for i in nums:
            if i not in elements:
                elements[i] = self.count_elements(nums, i)

        for element, occurence in elements.items():
            if occurence > occurences:
                majority_element = element
                occurences = occurence

        return majority_element


solution = Solution()
print(solution.majorityElement([3, 2, 3]))  # 3
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
