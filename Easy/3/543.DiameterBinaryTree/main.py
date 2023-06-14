from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode], h=0, ans=None):
            if not node:
                ans.append(0)
                return 0
            hl = dfs(node.left, h+1,ans)
            hr = dfs(node.right, h+1,ans)
            mass.append(hl +hr)
            return max(hl, hr) + 1
        mass = []
        dfs(root, ans=mass)
        print(mass)
        return max(mass)