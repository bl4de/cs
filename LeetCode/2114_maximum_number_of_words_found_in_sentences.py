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

    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for sentence in sentences:
            words = len(sentence.split(" "))
            max_words = words if words > max_words else max_words
        return max_words


solution = Solution()
print(solution.mostWordsFound(["alice and bob love leetcode",
      "i think so too", "this is great thanks very much"]))  # 6
print(solution.mostWordsFound(
    ["please wait", "continue to fight", "continue to win"]))  # 3
