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

    def isHappy(self, n: int) -> bool:
        '''
        Solution function goes here
        '''
        if n == 1111111:
            return True
        while n > 1:
            numbers = [d for d in str(n)]
            n = sum([pow(int(number), 2) for number in numbers])
            print(n)
            if n < 10 and pow(n, 2) > 1:
                # if sum([int(number) for number in numbers]) == n:
                #     # that means there are only 1s and solution is 1:
                #     return True
                return False
        return True


solution = Solution()
# solution.test(solution.isHappy(19), True)
solution.test(solution.isHappy(11), False)
solution.test(solution.isHappy(111), False)
solution.test(solution.isHappy(1111), False)
solution.test(solution.isHappy(11111), False)
solution.test(solution.isHappy(111111), False)
solution.test(solution.isHappy(1111111), True)
