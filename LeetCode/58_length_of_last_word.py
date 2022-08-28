#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, no-self-use
'''
    LeetCode solution class
'''


class Solution:
    '''
    LeetCode solution class
    '''

    def lengthOfLastWord(self, s: str) -> int:
        '''
        Returns lenght of the last word in str
        '''
        words = s.strip().split(' ')
        return len(words[len(words) - 1])


solution = Solution()
print(solution.lengthOfLastWord("Hello World!"))
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
print(solution.lengthOfLastWord("luffy is still joyboy"))
