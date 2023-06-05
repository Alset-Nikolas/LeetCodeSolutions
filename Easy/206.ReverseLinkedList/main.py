from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        last_node = None
        new_head = None
        while node:
            if node.next is None:
                new_head = node
            next_node = node.next
            node.next = last_node
            last_node = node
            node = next_node
        