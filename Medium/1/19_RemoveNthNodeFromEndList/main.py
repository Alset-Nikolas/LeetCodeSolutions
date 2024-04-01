from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		len_ = 0
		start = head
		while start:
			len_ += 1
			start = start.next
		if len_ == n :
			return head.next
		n_delete = len_ - n + 1
		start = head
		i = 0
		while start:
			i += 1
			if i + 1 == n_delete:
				start.next = start.next.next
				break
			start = start.next
		return head