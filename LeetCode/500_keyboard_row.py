#!/usr/bin/env python3
# pylint: disable=invalid-name, missing-class-docstring, import-error, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate,consider-iterating-dictionary
"""
    LeetCode solution class
    https://leetcode.com/problems/keyboard-row/
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
        self.test(self.solution(
            words=["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])
        self.test(self.solution(words=["omk"]), [])
        self.test(self.solution(words=["adsdf", "sfd"]), ["adsdf", "sfd"])

    def solution(self, words: List[str]) -> List[str]:
        """
        Solution function goes here
        """
        result = []
        keyboard = {
            "q": 0,
            "w": 0,
            "e": 0,
            "r": 0,
            "t": 0,
            "y": 0,
            "u": 0,
            "i": 0,
            "o": 0,
            "p": 0,

            "a": 1,
            "s": 1,
            "d": 1,
            "f": 1,
            "g": 1,
            "h": 1,
            "j": 1,
            "k": 1,
            "l": 1,

            "z": 2,
            "x": 2,
            "c": 2,
            "v": 2,
            "b": 2,
            "n": 2,
            "m": 2
        }

        for word in words:
            if len(set([keyboard[c] for c in word.lower()])) == 1:
                result.append(word)
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
