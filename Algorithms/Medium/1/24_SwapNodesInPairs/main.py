from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
		first = head
		if not first:
			return
		second = first.next
		if not second:
			return head
		head = second
		link_ = None
		while second:
			first.next = second.next
			second.next = first
			if link_:
				link_.next = second
			link_ = first
			first = first.next
			second = first.next if first else None
		return head


print(Solution().generateParenthesis(3))