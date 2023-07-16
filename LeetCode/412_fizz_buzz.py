#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/fizz-buzz/
"""
from typing import List, Optional
import string
import sys
import cProfile
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):

    def __init__(self, show_output=True) -> None:
        self.SHOW_OUTPUT = show_output
        super().__init__()

    def solve(self):
        """
        Solution runner called from profiler
        """
        self.test(self.solution(n=3), ["1", "2", "Fizz"])
        self.test(self.solution(n=5), ["1", "2", "Fizz", "4", "Buzz"])
        self.test(self.solution(n=15), ["1", "2", "Fizz", "4", "Buzz", "Fizz",
                  "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])

    def solution(self, n: int) -> List[str]:
        """
        Solution function goes here
        """
        result = []
        for num in range(1, n + 1):
            if num % 3 != 0 and num % 5 != 0:
                result.append(str(num))
                continue

            if num % 3 == 0 and num % 5 == 0:
                result.append("FizzBuzz")
                continue

            if num % 3 == 0:
                result.append("Fizz")
                continue

            if num % 5 == 0:
                result.append("Buzz")

        return result


SHOW_OUTPUT = True
NUMS_OF_EXECUTION = 1
SHOW_PROFILER_STATS = True

sys.setrecursionlimit(1000)
profiler = cProfile.Profile()
solution = Solution(SHOW_OUTPUT)

solution.timer_start()
profiler.enable()
print(f"\nRUNNING:\t{NUMS_OF_EXECUTION} iterations")
print(f"OUTPUT:\t\t{'disabled' if SHOW_OUTPUT is False else 'enabled'}")
for i in range(0, NUMS_OF_EXECUTION):
    profiler.run("solution.solve()")
solution.timer_stop()

if SHOW_PROFILER_STATS:
    profiler.print_stats(sort='calls')
profiler.disable()
