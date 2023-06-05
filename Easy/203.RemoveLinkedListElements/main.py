from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = head
        new_head = None
        while node:
            if node.val != val and new_head is None:
                new_head = node
            if node.next and node.next.val == val:
                node.next = node.next.next

            node = node.next

        


