#!/usr/bin/env python3
# pylint: disable=invalid-name, too-few-public-methods, no-self-use,missing-function-docstring
'''
    LeetCode solution class
'''
from typing import List, Optional

# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    '''
    LeetCode solution class
    '''

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Removes duplicates from linked list
        '''
        no_dups = []
        current_val = head.next()
        while current_val is not None:
            if current_val not in no_dups:
                no_dups.append(current_val)
                current_val = head.next()

        return no_dups


solution = Solution()
print(solution.deleteDuplicates([1, 1, 2]))
