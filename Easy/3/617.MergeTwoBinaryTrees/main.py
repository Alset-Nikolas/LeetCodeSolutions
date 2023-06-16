from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return root1
        v1 =0
        v2 = 0
        if root1:
            v1 =  root1.val
        else:
            root1 = TreeNode(val=0)

        if root2:
            v2 = root2.val
        root1.val = v1+v2

        if root1.left or (root2 and root2.left):
            root1.left = self.mergeTrees(root1.left, root2.left) if  root2 else self.mergeTrees(root1.left, None)


        if root1.right or (root2 and root2.right):
            root1.right = self.mergeTrees(root1.right, root2.right) if root2 else self.mergeTrees(root1.right, None)
        return root1
