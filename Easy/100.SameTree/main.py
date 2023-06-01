# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        val_items = []
        left_ch = []
        right_ch = []
        node = root
        if node:
            val_items.append(node.val)
            if node.left:
                left_ch = self.inorderTraversal(node.left)
            if node.right:
                right_ch = self.inorderTraversal(node.right)
        return left_ch + val_items  + right_ch

