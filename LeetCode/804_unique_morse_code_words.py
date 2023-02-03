#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
"""
    LeetCode solution class
    https://leetcode.com/problems/unique-morse-code-words/
"""
from typing import List, Optional
import string


class Solution:
    """
    LeetCode solution class
    """
    endline = '\33[0m'
    green = '\33[32m'
    red = '\33[31m'
    PASS = f"{green}[+] PASS {endline}"
    FAIL = f"{red}[+] FAIL {endline}"

    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    lowercases = string.ascii_lowercase

    def __init__(self):
        self.morse = dict(zip(self.lowercases, self.morse))
        print(self.morse)

    def test(self, provided, expected) -> bool:
        """
        Compares provided result to expected
        """
        print(f"\n output  : {provided}\n expected: {expected}")
        print(f" {self.PASS if provided == expected else self.FAIL}")
        return provided == expected

    def morse_word(self, word: str) -> str:
        """
        Morses word
        :param word:
        :return: str
        """
        result = ""
        for c in word:
            result += self.morse[c]
        return result

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """
        Solution function goes here
        """
        result = 0
        morsed = []
        for word in words:
            morsed.append(self.morse_word(word))
        return len(set(morsed))


solution = Solution()
solution.test(solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]), 2)
solution.test(solution.uniqueMorseRepresentations(["a"]), 1)
