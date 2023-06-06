from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        items = []
        node = head
        while node:
            items.append(node.val)
            node=node.next
        for i in range(len(items)//2):
            if items[i] != items[len(items)-i-1]:
                return False
        return True