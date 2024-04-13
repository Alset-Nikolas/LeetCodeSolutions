# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

    @classmethod
    def get_head_list(cls, mass):
        node_head = None
        last_node = None
        for x in mass:
            node = cls(x)
            if node_head is None:
                node_head = node
            else:
                last_node.next = node
            last_node = node

        return node_head

    @classmethod
    def check_2_listnode(cls, ls1, ls2):
        while ls1 and ls2:
            if ls1.val != ls2.val:
                return False
            ls1 = ls1.next
            ls2 = ls2.next
        return ls1 is None and ls2 is None


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node_head = None
        last_node = None
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                node = ListNode(val=list1.val)
                if node_head is None:
                    node_head = node
                else:
                    last_node.next = node
                list1 = list1.next
                last_node = node

            else:
                node = ListNode(val=list2.val)
                if node_head is None:
                    node_head = node
                else:
                    last_node.next = node
                list2 = list2.next
                last_node = node
        for list in [list1, list2]:
            while list:
                node = ListNode(val=list.val)
                if node_head is None:
                    node_head = node
                else:
                    last_node.next = node
                list = list.next
                last_node = node
        return node_head


if __name__ == "__main__":
    s = Solution()

    assert ListNode.check_2_listnode(
        s.mergeTwoLists(ListNode.get_head_list([1, 2, 4]), ListNode.get_head_list([1, 3, 4])),
        ListNode.get_head_list([1, 1, 2, 3, 4, 4]))
    assert s.mergeTwoLists(None, None) == None
    assert not s.mergeTwoLists(None, ListNode(0)) == ListNode(0)
