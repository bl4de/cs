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

    def greatestLetter(self, s: str) -> str:
        greatest_letter = 0
        for l in s:
            if int(ord(l)) >= 97:
                if chr(int(ord(l)) - 32) in s:
                    if greatest_letter < int(ord(l)) - 32:
                        greatest_letter = int(ord(l)) - 32
            if int(ord(l)) <= 90:
                if chr(int(ord(l)) + 32) in s:
                    if greatest_letter < int(ord(l) + 32):
                        greatest_letter = int(ord(l) + 32)
        return '' if greatest_letter == 0 else chr(greatest_letter).upper()


solution = Solution()
solution.debug(solution.greatestLetter("lEeTcOdE"), 'E')
solution.debug(solution.greatestLetter("arRAzFif"), 'R')
solution.debug(solution.greatestLetter("AbCdEfGhIjK"), '')
solution.debug(solution.greatestLetter(
    "nzmguNAEtJHkQaWDVSKxRCUivXpGLBcsjeobYPFwTZqrhlyOIfdM"), 'Z')
