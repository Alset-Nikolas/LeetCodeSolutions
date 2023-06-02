# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_h_node(node):
            if not node:
                return 0
            
            l = 0
            r = 0
            if node.left:
                l = get_h_node(node.left) + 1
            if node.right:
                r = get_h_node(node.right) + 1
            return max(1, max(l, r))
        if not root:
            return True
        return abs(get_h_node(root.left) - get_h_node(root.right)) <= 1