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
        words = s.split(' ')
        return len(words[len(words) - 1])


solution = Solution()
print(solution.lengthOfLastWord("Hello World!"))
