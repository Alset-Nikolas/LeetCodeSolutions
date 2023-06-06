# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        items = set()
        node = head
        while node:
            if node not in items:
                items.add(node)
            else:
                return False
            node = node.next
        return True


if __name__ == "__main__":
    values = [3, 2, 0, -4]
    pos = 1
    nodes = []
    for x in values:
        node = ListNode(x=3)
        if len(nodes)>0:
            last_node = nodes[-1]
            last_node.next = node
        nodes.append(node)
    last_node = nodes[-1]
    last_node.next = nodes[1]
    s = Solution()
    s.hasCycle(nodes[0])
