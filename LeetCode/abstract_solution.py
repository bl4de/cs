#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode abstract solution class
"""
from typing import List, Optional
import string
import sys


class AbstractSolution:
    """
    LeetCode solution class
    """
    endline = '\33[0m'
    green = '\33[32m'
    red = '\33[31m'
    PASS = f"{green}[+] PASS {endline}"
    FAIL = f"{red}[+] FAIL {endline}"

    def test(self, provided, expected) -> bool:
        """
        Compares provided result to expected
        """
        print(f"\n output  : {provided}\n expected: {expected}")
        print(f" {self.PASS if provided == expected else self.FAIL}")
        return provided == expected

    def convertNumberToCharactersArray(self, number: int, elementType='char') -> List:
        """
        convertNumberToCharactersArray(123, 'char') => ['1', '2', '3']
        convertNumberToCharactersArray(123, 'int') => [1, 2, 3]
        """
        if elementType == 'int':
            return [int(c) for c in str(number)]
        return [c for c in str(number)]
