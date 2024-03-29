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

    def debug(self, provided, expected) -> bool:
        '''
        Compares provided result to expected
        Returns true if equal
        '''
        print(f"\n output  : {provided}\n expected: {expected}")
        print(f" {self.PASS if provided == expected else self.FAIL}")
        return provided == expected

    def checkOnesSegment(self, s: str) -> bool:
        if not '0' in s:
            return True

        no_previous_ones = False
        for i in range(1, len(s)):
            if s[i - 1] == '1' and s[i] == '0' and no_previous_ones is False:
                no_previous_ones = True

            if no_previous_ones is True:
                if s[i - 1] == '0' and s[i] == '1':
                    return False
        return True


solution = Solution()
solution.debug(solution.checkOnesSegment("1"), True)
solution.debug(solution.checkOnesSegment("1001"), False)
solution.debug(solution.checkOnesSegment("110"), True)
solution.debug(solution.checkOnesSegment("10"), True)
solution.debug(solution.checkOnesSegment("11"), True)
solution.debug(solution.checkOnesSegment("1000"), True)
solution.debug(solution.checkOnesSegment("10110000"), False)
