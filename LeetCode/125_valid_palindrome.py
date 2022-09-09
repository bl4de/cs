#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, no-self-use,missing-function-docstring, unused-wildcart-import
'''
    LeetCode solution class
'''
from typing import List, Optional
import re


class Solution:
    '''
    LeetCode solution class
    '''

    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        s = re.sub("[^a-z0-9]", "", s.lower())
        return s == s[::-1]


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome("0P"))
