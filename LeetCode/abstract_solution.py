#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode abstract solution class
    Implements some common methods used to solve challenges in LeetCode,
    ProjectEuler, Advent Of Code etc.
"""
from typing import List, Optional
import string
import sys
import time


class AbstractSolution:
    """
    LeetCode solution class
    """
    endline = '\33[0m'
    green = '\33[32m'
    red = '\33[31m'
    GREEN = f"{green}"
    ENDL = f"{endline}"
    PASS = f"{green}[+] PASS {endline}"
    FAIL = f"{red}[+] FAIL {endline}"

    t_start = 0
    t_stop = 0

    def timer_start(self):
        """
        Starts the timer
        """
        self.t_start = time.time()

    def timer_stop(self) -> int:
        """
        Stops the timer and prints the result
        """
        self.t_stop = time.time()
        print(f"\n{self.GREEN} [+] Total execution time: {((self.t_stop - self.t_start)):.4f}s{self.ENDL}\n")

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
