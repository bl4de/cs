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

    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(d) for d in str(int(''.join([str(d) for d in digits])) + 1)]


solution = Solution()
print(solution.plusOne([1, 2, 3]))
print(solution.plusOne([4, 3, 2, 1]))
print(solution.plusOne([9]))
