from typing import * 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
        return slow