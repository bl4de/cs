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
        index = len(s)
        for digit in s:
            if digit == '1':
                intval += pow(2, int(index - 1))
            index -= 1
        return intval

    def addBinary(self, a: str, b: str) -> str:
        intval_a = self.calculatemValueFromBinary(a)
        intval_b = self.calculatemValueFromBinary(b)
        return bin(intval_a + intval_b)[2:]


solution = Solution()
print(solution.addBinary("11", "1"))
print(solution.addBinary("1010", "1011"))
