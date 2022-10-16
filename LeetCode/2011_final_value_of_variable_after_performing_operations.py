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

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for operation in operations:
            result = result + 1 if '+' in operation else result - 1

        return result


solution = Solution()
print(solution.finalValueAfterOperations(["--X", "X++", "X++"]))  # 1
print(solution.finalValueAfterOperations(["++X", "++X", "X++"]))  # 3
print(solution.finalValueAfterOperations(["X++", "++X", "--X", "X--"]))  # 0
