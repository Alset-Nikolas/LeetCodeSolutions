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
        
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1:
                return node2 is None
            if not node2:
                return node1 is None
            
            flag = check_subtree(node1, node2)
            return dfs(node1.left, node2) or flag or dfs(node1.right, node2)
        return dfs(root, subRoot)

            