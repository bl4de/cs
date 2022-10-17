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

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        island_perimeter = 0

        return island_perimeter


solution = Solution()
print(solution.islandPerimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))  # 16
print(solution.islandPerimeter([[1]]))  # 4
print(solution.islandPerimeter([[[1, 0]]]))  # 4
