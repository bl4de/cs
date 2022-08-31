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

    def calculatemValueFromBinary(self, s: str) -> bin:
        '''
        Converts binary string into int
        '''
        intval = 0
        for (_, index) in enumerate(s[::-1]):
            intval += pow(2, int(index))
        return intval

    def addBinary(self, a: str, b: str) -> str:
        intval_a = self.calculatemValueFromBinary(a)
        intval_b = self.calculatemValueFromBinary(b)
        return bin(intval_a + intval_b)


solution = Solution()
print(solution.addBinary("1010", "1011"))
