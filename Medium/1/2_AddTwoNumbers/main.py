from typing import Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def get_number_by_list(l: Optional[ListNode]):
	number = []
	while l != None:
		number.append(l.val)
		l = l.next
	if number:
		return int(''.join(str(x) for x in number[::-1]))
	return 0

def create_link_by_number(number:int):
	root = ListNode(
		val=number%10,
	)
	number //= 10
	node = root
	while number>0:

		new_node = ListNode(
			val=number % 10,
		)
		node.next = new_node
		number //= 10
		node = new_node
	return root

class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		n1 = get_number_by_list(l1)
		n2 = get_number_by_list(l2)
		return create_link_by_number(n1+n2)
