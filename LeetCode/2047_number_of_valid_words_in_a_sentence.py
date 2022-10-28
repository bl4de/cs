#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, unused-import, no-self-use,missing-function-docstring,consider-using-enumerate
'''
    LeetCode solution class
'''
from typing import List, Optional
import re
import string

class Solution:
    '''
    LeetCode solution class
    '''

    def check_if_word_is_valid(self, word: str) -> bool:
        valid_characters = string.ascii_lowercase + "0123456789" + "!,. "

        return True


    def countValidWords(self, sentence: str) -> int:
        valid_words = 0
        words = sentence.split(' ')
        for word in words:
            if self.check_if_word_is_valid(word):
                valid_words += 1
        return valid_words


solution = Solution()
print(solution.countValidWords("cat and  dog"))  # 3
print(solution.countValidWords("!this  1-s b8d!"))  # 0
print(solution.countValidWords("alice and  bob are playing stone-game10"))  # 5
