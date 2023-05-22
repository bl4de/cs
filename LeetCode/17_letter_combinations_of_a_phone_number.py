#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List, Optional
import string
import sys
import cProfile
from abstract_solution import AbstractSolution


class Solution(AbstractSolution):

    def solve(self):
        """
        Solution runner called from profiler
        """
        self.test(self.solution(digits="23"), [
                  "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.test(self.solution(digits=""), [])
        self.test(self.solution(digits="2"), ["a", "b", "c"])

    KEYPAD = {
        "1": [],
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z']
    }

    def solution(self, digits: str) -> List[str]:
        """
        Solution function goes here
        """
        # test case 1: empty digits
        if len(digits) == 0:
            return []

        # test case 2: one digit:
        if len(digits) == 1:
            return self.KEYPAD[digits]

        # test case 3: two or more digits
        result = []
        digits = [d for d in digits]
        chars = []
        for d in digits:
            chars.append(self.KEYPAD[d])

        if len(chars) == 2:
            for c1 in chars[0]:
                for c2 in chars[1]:
                    result.append(f"{c1}{c2}")
            return result

        if len(chars) == 3:
            for c1 in chars[0]:
                for c2 in chars[1]:
                    for c3 in chars[2]:
                        result.append(f"{c1}{c2}{c3}")
            return result

        if len(chars) == 4:
            for c1 in chars[0]:
                for c2 in chars[1]:
                    for c3 in chars[2]:
                        for c4 in chars[3]:
                            result.append(f"{c1}{c2}{c3}{c4}")
            return result
        return result


NUMS_OF_EXECUTION = 1
SHOW_PROFILER_STATS = True

sys.setrecursionlimit(1000)
profiler = cProfile.Profile()
solution = Solution()

solution.timer_start()
profiler.enable()
for i in range(0, NUMS_OF_EXECUTION):
    profiler.run("solution.solve()")
solution.timer_stop()

if SHOW_PROFILER_STATS:
    profiler.print_stats(sort='calls')
profiler.disable()
