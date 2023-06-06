# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """104. Maximum Depth of Binary Tree
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l =0
        r = 0
        if root.left:
            l = self.maxDepth(root.left) + 1
        if root.right:
            r = self.maxDepth(root.right) + 1
        return max(max(l, r), 1)