from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        sorted = ListNode()

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                sorted.next = ListNode(l1.val)
                sorted = sorted.next
                l1 = l1.next
            else:
                sorted.next = ListNode(l2.val)
                sorted = sorted.next
                l2 = l2.next

        while(l2):
            sorted.next = ListNode(l2.val)
            sorted = sorted.next
            l2 = l2.next

        while(l1):
            sorted.next = ListNode(l1.val)
            sorted = sorted.next
            l1 = l1.next

        return sorted.next
