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

    def reverseBits(self, n: int) -> int:

        return 0


solution = Solution()

# input:    00000010100101000001111010011100
# output:   00111001011110000010100101000000
print(solution.reverseBits(43261596))  # 964176192

# input:    11111111111111111111111111111101
# output:   10111111111111111111111111111111
print(solution.reverseBits(4294967293))  # 3221225471
