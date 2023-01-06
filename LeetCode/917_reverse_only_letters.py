#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
'''
    LeetCode solution class
'''
from typing import List, Optional
import string

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

    def reverseOnlyLetters(self, s: str) -> str:
        '''
        Solution function goes here
        '''
        rev = ""
        counter = 0
        for c in range(len(s) - 1, -1, -1):
            if s[c] in string.ascii_letters:
                rev += s[c]
            else:
                rev += s[counter]
            counter += 1
        return rev


solution = Solution()
solution.test(solution.reverseOnlyLetters("ab-cd"), "dc-ba")
solution.test(solution.reverseOnlyLetters("a-bC-dEf-ghIj"), "j-Ih-gfE-dCba")
solution.test(solution.reverseOnlyLetters(
    "Test1ng-Leet=code-Q!"), "Qedo1ct-eeLg=ntse-T!")
