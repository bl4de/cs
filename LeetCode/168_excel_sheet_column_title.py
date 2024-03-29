#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, no-self-use,missing-function-docstring, unused-wildcart-import
'''
    LeetCode solution class
'''
from cmath import sqrt
from typing import List, Optional
import string

# 26      1
# 676     2
# 17576   3
# 456976  4


class Solution:
    '''
    LeetCode solution class
    '''

    def __init__(self) -> None:
        self.uppercases = string.ascii_uppercase
        self.number_of_characters = len(self.uppercases)
        self.column_name = ''

    def get_letter_by_column(self, column_number: int) -> str:
        '''
        returns column letter
        '''
        return self.uppercases[column_number]

    def convertToTitle(self, column_number: int) -> str:
        if column_number <= 26:
            return self.get_letter_by_column(column_number - 1) + self.column_name

        while column_number // self.number_of_characters > 0:
            r = column_number % self.number_of_characters
            self.column_name = self.get_letter_by_column(r) + self.column_name
            column_number = column_number // 26

        return self.column_name


solution = Solution()

print(solution.convertToTitle(1))  # 'A'
print(solution.convertToTitle(26))  # 'Z'
print(solution.convertToTitle(28))  # 'AB'

# print(solution.convertToTitle(52))  # 'AZ'
# print(solution.convertToTitle(53))  # BA'

# print(solution.convertToTitle(701))  # 'ZY'
