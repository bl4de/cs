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

    def __init__(self) -> None:
        self.uppercases = string.ascii_uppercase
        self.number_of_characters = len(self.uppercases)

    def get_letter_by_column(self, column_number: int) -> str:
        '''
        returns column letter
        '''
        return self.uppercases[column_number]

    def convertToTitle(self, column_number: int) -> str:
        column_name = ''

        return column_name


solution = Solution()
print(solution.convertToTitle(1))  # 'A'
print(solution.convertToTitle(26))  # 'Z'
print(solution.convertToTitle(52))  # 'AZ'
# print(solution.convertToTitle(53))  # BA'
# print(solution.convertToTitle(28))  # 'AB'
# print(solution.convertToTitle(701))  # 'ZY'
