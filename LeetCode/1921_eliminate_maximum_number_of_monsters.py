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

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        eliminated_monsters = 0

        return eliminated_monsters


solution = Solution()
print(solution.eliminateMaximum(dist=[1, 3, 4], speed=[1, 1, 1]))  # 3
print(solution.eliminateMaximum(dist=[1, 1, 2, 3], speed=[1, 1, 1, 1]))  # 1
print(solution.eliminateMaximum(dist=[3, 2, 4], speed=[5, 3, 2]))  # 1
