# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        last_node = None
        while node:
            if last_node is None:
                node = head.next
                last_node = head
                continue
            if node.val == last_node.val:
                last_node.next= None
            else:
                last_node.next=node
                last_node = node
            node = node.next

        return head




if __name__ == "__main__":
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3

