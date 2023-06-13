from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, h=0, ans=None):
            if ans is None:
                ans = []
            
            if not node:
                ans.append(0)
                return h
            hl = dfs(node.left, h+1)
            hr = dfs(node.right, h+1)
            ans.append(hl+hr-h)
            return h + 1
        mass = []
        dfs(root, ans=mass)
        return max(mass)