import math
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_minh(root, h=0):
            if not root:
                return h
            if not root.left and not root.right:
                return h + 1
            if root.left and root.right:
                return min(get_minh(root.left, h+1), get_minh(root.right, h+1))
            if root.left:
                return get_minh(root.left, h+1)
            return get_minh(root.right, h+1)
        return get_minh(root)
            
