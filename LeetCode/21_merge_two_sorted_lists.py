from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass


s = Solution()

list1 = []
list2 = []

s.mergeTwoLists(list1, list2)  # []


list1 = [1, 2, 4]
list2 = [1, 3, 4]

s.mergeTwoLists(list1, list2)  # [1,1,2,3,4,4]


list1 = []
list2 = [0]

s.mergeTwoLists(list1, list2)  # [0]


list1 = [2, 5, 7, 9]
list2 = [-1, 12, 34]

s.mergeTwoLists(list1, list2)  # [-1,2,5,7,9,12,34]
