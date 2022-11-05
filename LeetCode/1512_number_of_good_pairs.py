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

    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0

        return good_pairs


solution = Solution()
# 4 ->  (0,3), (0,4), (3,4), (2,5)
print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(solution.numIdenticalPairs([1, 1, 1, 1]))  # 6 -> all pairs
