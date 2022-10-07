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

    def hammingWeight(self, n: int) -> int:
        hamming_weight = 0
        for p in range(0, 32):
            if n & pow(2, p) > 0:
                hamming_weight += 1
        return hamming_weight


solution = Solution()
print(solution.hammingWeight(0b00000000000000000000000000001011))  # 3
print(solution.hammingWeight(0b00000000000000000000000010000000))  # 1
print(solution.hammingWeight(0b11111111111111111111111111111101))  # 31
