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

    def check_for_hypen(self, word: str) -> bool:
        '''
        There is at most one hyphen '-'. If present, it must be surrounded by 
        lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
        '''
        hyphen_index = word.rfind('-')
        print(hyphen_index)
        if hyphen_index == -1 or hyphen_index == 1 or hyphen_index == len(word - 1):
            return False
        return word[hyphen_index - 1] == 'a' and word[hyphen_index + 1] == 'b'

    def check_if_word_is_valid(self, word: str) -> bool:
        return False if re.match('[^-!,. abcdefghijklmnopqrstuwvxyz]', word) else True

    def countValidWords(self, sentence: str) -> int:
        valid_words = 0
        words = sentence.split(' ')
        for word in words:
            if self.check_if_word_is_valid(word) and self.check_for_hypen(word):
                valid_words += 1
        return valid_words


solution = Solution()
print(solution.countValidWords("cat and  dog"))  # 3
print(solution.countValidWords("!this  1-s b8d!"))  # 0
print(solution.countValidWords("alice and  bob are playing stone-game10"))  # 5
