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

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if kid + extraCandies >=
                max(candies) else False for kid in candies]


solution = Solution()
# [true,true,true,false,true]
print(solution.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))

# [true,false,false,false,false]
print(solution.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
