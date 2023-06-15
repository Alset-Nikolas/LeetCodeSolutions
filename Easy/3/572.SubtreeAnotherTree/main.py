# Definition for a binary tree node.
from typing import * 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_subtree(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1:
                return node2 is None
            if not node2:
                return node1 is None

            l = check_subtree(node1.left, node2.left)
            r = check_subtree(node1.right, node2.right)
            return node1.val == node2.val and l and r