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
    colors = {
        "black": '\33[30m',
        "red": '\33[31m',
        "green": '\33[32m',
        "yellow": '\33[33m',
        "blue": '\33[34m',
        "magenta": '\33[35m',
        "cyan": '\33[36m',
        "white": '\33[37m',
        "grey": '\33[90m',
        "lightblue": '\33[94m'
    }
    endline = '\33[0m'
    PASS = f"{colors['green']}[+] PASS {endline}"
    FAIL = f"{colors['red']}[+] FAIL {endline}"

    def test(self, provided, expected) -> bool:
        '''
        Compares provided result to expected
        Returns true if equal
        '''
        print(f"\n output  : {provided}\n expected: {expected}")
        print(f" {self.PASS if provided == expected else self.FAIL}")
        return provided == expected

    def generate(self, numRows: int) -> List[List[int]]:
        '''
        Solution function goes here
        '''
        triangle = [[1]]
        if numRows == 1:
            return triangle
        triangle.append([1, 1])
        if numRows == 2:
            return triangle

        for row in range(2, numRows):
            nextRow = [1]
            for elem in range(1, len(triangle[row - 1])):
                nextRow.append(triangle[row - 1][elem - 1] +
                               triangle[row - 1][elem])
            nextRow.append(1)
            triangle.append(nextRow)
        return triangle

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex > 0:
            return self.generate(rowIndex + 1)[rowIndex]
        return [1]


solution = Solution()
solution.test(solution.getRow(3), [1, 3, 3, 1])
solution.test(solution.getRow(0), [1])
solution.test(solution.getRow(1), [1, 1])
