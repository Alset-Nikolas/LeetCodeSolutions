# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        flag_l = False
        flag_r = False
        if root.left:
            flag_l = self.hasPathSum(root.left, targetSum-root.val)
        if root.right:
            flag_r = self.hasPathSum(root.right, targetSum-root.val)
        return flag_l or flag_r
            