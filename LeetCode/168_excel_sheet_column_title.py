#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, no-self-use,missing-function-docstring, unused-wildcart-import
'''
    LeetCode solution class
'''
from typing import List, Optional
import string


class Solution:
    '''
    LeetCode solution class
    '''

    UPPERCASES = list(string.ascii_uppercase)

    def convertToTitle(self, column_number: int) -> str:
        column_name = ''
        number_of_characters = len(self.UPPERCASES)
        r = number_of_characters

        c = (column_number % number_of_characters) - 1
        r = column_number // number_of_characters
        column_name += self.UPPERCASES[c]

        if r > number_of_characters:
            c = (column_number % number_of_characters) - 1
            r = column_number // number_of_characters
            column_name += self.UPPERCASES[c]
        return column_name


solution = Solution()
print(solution.convertToTitle(1))  # 'A'
print(solution.convertToTitle(26))  # 'Z'
print(solution.convertToTitle(52))  # AZ'
print(solution.convertToTitle(53))  # BA'
# print(solution.convertToTitle(28))  # 'AB'
# print(solution.convertToTitle(701))  # 'ZY'
