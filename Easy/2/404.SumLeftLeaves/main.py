from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, res=0, p=None):
            if not node:
                return res
            if not node.left and not node.right:
                if p == 'l':
                    res += node.val
                return res
            res += dfs(node.left,p='l')
            res += dfs(node.right,p='r')
            return res
        
        return dfs(root)